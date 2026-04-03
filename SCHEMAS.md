# API Schemas

The version-specific client generation in the `ubersmith-api` package relies on JSON schemas for the target version.

Available schemas are stored in the [schema directory](schema/).

Scripts used for managing schemas are located in the [tools directory](tools/).

## Contributor Guidelines

If you would like to contribute a schema for compatibility, please reference the [generation](#generating-a-schema) docs below.

At the very least, a PR looking to add a schema should include the schema file.  
If you would like to also submit the generated client(s) in the PR, that would be appreciated.

## Generating a Schema

To generate a schema you will need:

- An Ubersmith instance you have access to
- Administrative API credentials for the instance
- Python 3+ (only core libraries are used here)
- This `ubersmith-api` client installed


This should be executed from the repository root.
```bash
# Install the package
python3 -m pip install ./

# Generate the schema
./tools/generate_schema.py \
  --host 'ubersmith.example.com' \
  --username 'admin' \
  --password 'password'

# Additional parameters are provided in case they are needed
  # --port 443
  # --no-verify # Skips SSL verification
  # --insecure # Uses http (NOT RECOMMENDED)
  # --out-dir # Override the directory the schema file is saved to; used for development and testing
  # --filename # Override the schema file name; used for development and testing
```

> [!WARNING]
> Schema generation takes a while to complete.  
> It is recommended to perform this on a non-production instance or during off hours.

When executed, this script will do the following:
1. List all methods using the `uber.method_list` API method
2. Loop over the returned methods building a data structure
  1. First, details are gathered using the `uber.method_get` API method
  2. Next, fluff information is discarded, and parameters are filtered and sorted by required/optional
3. Finally, the data structure is written to the schema file in the output directory

> [!NOTE]
> By default, schema files will be output to the [schema directory](schema/), and named by the version Ubersmith is running.

## Using Schemas

Schemas in the repository at release time will be baked into the package, so no additional work will be required.

To generate a client from a schema, you will need:
- A schema file (see the [generation docs](#generating-a-schema) above)
- Python 3+, the following packages:
  - `jinja2`

A Makefile target is provided to easily generate classes from schemas.

Assuming the schema is already generated and available at `schema/<semantic-version>.json`:

```bash
# It is recommended to run this inside of a virtual environment
python3 -m pip install -r tools/requirements.txt

make generate_version SCHEMA_FILE=<semantic-version>.json
```

The generated client will be saved to `src/ubersmith/versions/v<semantic_version>/`.
