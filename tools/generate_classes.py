#!/usr/bin/env python3

import argparse
import pathlib
import json

from typing import Dict
from jinja2 import Environment, FileSystemLoader, StrictUndefined

THIS_FILE = pathlib.Path(__file__)
REPO_ROOT = THIS_FILE.resolve().parents[1]
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
    
    # Sort the parameters for each method in the section
    for _, data in section_data.items():
        req, opt = sort_parameters(data['params'])
        data.update(req_params=req, opt_params=opt)
    
    if 'basic_search' in list(section_data.keys()):
        _ = section_data.pop('basic_search')
    
    # Write the section file
    out_path = out_dir / f"{section_name}.py"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(section_tpl.render(section_name=section_name, section_data=section_data), encoding='utf-8')

def render_init(init_file: pathlib.Path, sections: list[str], module: str) -> None:
    env = jinja_env()
    init_tpl = env.get_template('api__init__.py.j2')
    init_file.write_text(init_tpl.render(sections=sections, module=module))


def render(source: pathlib.Path, destination: pathlib.Path) -> bool:    
    version = source.name.rstrip(source.suffix)
    module = 'v' + version.replace('.', '_').replace('-', '_')
    
    print(f'Rendering Version {version} from {source} to {module}')
    
    out_dir : pathlib.Path = (destination / module)
    
    try:
        out_dir.mkdir()
    except FileExistsError:
        # Ignore errors when the directory exists
        ...
    
    with open(source, 'r') as f:
        schema_data: Dict[Dict] = json.load(f)
    
    init_file = (out_dir / '__init__.py')
    print(f'    {version} - Rendering {init_file}')
    render_init(init_file, sections=list(schema_data.keys()), module=module)
    
    for section_name, section_data in schema_data.items():
        print(f'        Rendering Section: {section_name}: {len(section_data)} methods')
        render_section(out_dir=out_dir, section_name=section_name, section_data=section_data)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--schema-dir", default='schema')
    ap.add_argument("-o", "--output-dir", default='src/ubersmith/versions')
    ap.add_argument("-f", "--filename", default=None)
    args = ap.parse_args()
    
    schema_dir = pathlib.Path(REPO_ROOT / args.schema_dir)
    output_dir = pathlib.Path(REPO_ROOT / args.output_dir)
    
    if args.filename:
        # Process a single schema file, if supplied
        schema_file: pathlib.Path = (schema_dir / args.filename)
        render(source=schema_file, destination=output_dir)
    else:
        # Otherwise, process all schema files
        for schema_file in schema_dir.iterdir():
            render(source=schema_file, destination=output_dir)


if __name__ == "__main__":
    main()
