#!/usr/bin/env python3

import argparse
import pathlib
import json

from ubersmith.client import *

def get_method_details(client: UbersmithClient, method: str) -> dict:
    try:
        method_details = client.method_get(method)
    except Exception:
        return None
    # Throw out the 'output' field which isn't helpful for our needs
    _ = method_details.pop('output')
    return method_details

def get_sections(client: UbersmithClient) -> dict:
    print("Listing methods...")
    all_methods = client.method_list()
    method_count = len(all_methods)
    print(f"{len(all_methods)} Methods Found")
    print('')
    
    print("Gathering method details. This may take a while...")
    index = 1
    sections = dict()
    for method in all_methods.keys():
        print(f"Processing item {index}/{method_count}: {method}", end="\r", flush=True)
        sec, meth = method.split('.')
        if not sec in sections:
            sections[sec] = dict()
        method_details = get_method_details(client, method)
        if method_details:
            sections[sec][meth] = method_details
    return sections

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-h", "--host", required=True)
    ap.add_argument("-P", "--port", default=None)
    ap.add_argument("-u", "--username", required=True)
    ap.add_argument("-p", "--password", required=True)
    ap.add_argument("-v", "--no-verify", default=False, action="store_true")
    ap.add_argument("-k", "--insecure", default=False, action="store_true")
    ap.add_argument("-o", "--out-dir", default="../schema")
    ap.add_argument("-f", "--filename", default=None)
    args = ap.parse_args()
    
    if not args.port:
        if args.insecure:
            port = '80'
        else:
            port = '443'
    else:
        port = args.port

    cfg = UbersmithConfig(
        host=args.host,
        port=port,
        username=args.username,
        password=args.password,
        verify=not args.no_verify,
        secure=not args.insecure,
    )
    client = UbersmithClient(cfg)
    
    version = client.system_info()['version']
    print(f'Running generation against Ubersmith version: {version}')

    print(f"Gathering details from {cfg.host}...")
    all_sections = get_sections(client)
    
    
    out_dir = pathlib.Path(args.out_dir)
    if args.filename:
        filename = args.filename
    else:
        filename = f'{version}.json'
    out_file = (out_dir / filename)
    print(f'Writing files to {out_file}')
    
    with open(out_file, 'w') as f:
        json.dump(all_sections, f, indent=4)

if __name__ == "__main__":
    main()
