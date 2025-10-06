#!/usr/bin/env python3

import argparse
import pathlib
import json

from jinja2 import Environment, FileSystemLoader, StrictUndefined

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
TEMPLATE_DIR = REPO_ROOT / "template"

def jinja_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=False,
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env

def sort_parameters(params: list[dict]) -> tuple[list[dict], list[dict]]:
    req_params = list()
    opt_params = list()
    for p in sorted(params, key=lambda x: x['param']):
        # Correct meta to remove the trailing '_*'
        if p['param'] in ['meta_*', '[any included custom field variable]']:
            p['param'] = 'meta'
        # Correct 'pass' parameters to avoid conflicts with Python directive
        if p['param'] == 'pass':
            p['param'] = 'passwd'
        # Correct 'from' parameters to avoid conflicts with Python directive
        if p['param'] == 'from':
            p['param'] = 'from_address'
        
        # TODO: Make actual logic for this with cleaners.
        # For now, we're just removing arguments that match this
        unsupported_strings = ['{', '[', '<']
        if any(substring in p['param'] for substring in unsupported_strings):
            continue
        
        # Sort required/not required parameters
        if p['required']:
            req_params.append(p)
        else:
            opt_params.append(p)
    return req_params, opt_params

# Still need a render function
def render_section(out_dir: pathlib.Path, section_name: str, section_data: dict) -> None:
    env = jinja_env()
    section_tpl = env.get_template("section.py.j2")
    
    # Write the section file
    out_path = out_dir / f"{section_name}.py"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(section_tpl.render(section_name=section_name, section_data=section_data), encoding='utf-8')

def render_init(init_file: pathlib.Path, sections: list[str]) -> None:
    env = jinja_env()
    init_tpl = env.get_template('api__init__.py.j2')
    init_file.write_text(init_tpl.render(sections=sections))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--out-dir", default="../src/ubersmith/api")
    ap.add_argument("-s", "--schema-dir", default='../schema')
    ap.add_argument("-f", "--filename", required=True)
    args = ap.parse_args()
    
    out_dir = pathlib.Path(args.out_dir)
    schema_dir = pathlib.Path(args.schema_dir)
    schema_file = (schema_dir / args.filename)
    
    print(f'Generating client from {schema_file}')
    
    with open(schema_file, 'r') as f:
        schema_data = json.load(f)
    
    init_file = out_dir / '__init__.py'    
    print(f'Rendering {init_file}')
    render_init(init_file, sections=list(schema_data.keys()))

    for section_name, section_data in schema_data.items():
        print(f'Rendering Section: {section_name}: {len(section_data)} methods')
        render_section(out_dir=out_dir, section_name=section_name, section_data=section_data)

if __name__ == "__main__":
    main()
