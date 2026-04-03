# Python Ubersmith
[![Pypi](https://img.shields.io/pypi/v/ubersmith-api)](https://pypi.org/project/ubersmith-api)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/bnassif/ubersmith-api/main/LICENSE)
![GitHub Release Date](https://img.shields.io/github/release-date/bnassif/ubersmith-api)

A fully-featured API wrapper for the [Ubersmith](https://ubersmith.com/) API

Python wrappers exist on PyPI and across GitHub for interacting with the Ubersmith API, but each of them fails to provide full compatibility.

In comes `ubersmith-api`...


## Installation
```bash
# PyPi Installation
pip install ubersmith-api
# GitHub Installation
pip install git+'https://github.com/bnassif/ubersmith-api.git'
```


## Overview
The `ubersmith-api` package ships two separate layers of usage, which offer varying levels of compatibility.

Both levels use the robust `UbersmithConfig` Pydantic Settings object, which exposes all settings for how to interact with the API.


### Universal Client
The universal client, `UbersmithClient` provides a generic object for interacting with any Ubersmith version using the version 2.0 API. This object ships with just three methods bound to it:

- `UbersmithClient.request()`: Method for making API calls
- `UbersmithClient.system_info()`: Calls `user.system_info`
- `UbersmithClient.method_list()`: Calls `user.method_list`
- `UbersmithClient.method_get()`: Calls `user.method_get`


#### Example Usage
```python
from ubersmith import *

config = UbersmithConfig(
    host='target-hostname-or-address',
    username='username-to-use',
    password='api-token-for-user',
)

api_client = UbersmithClient(config)

client_info = api_client.request(
    'client.get',
    data={
        'client_id': 1234,
        'metadata': True,
    },
    #raw=True, # Optionally return the unparsed `requests.Response` object
)
```


### Version Specific Clients
Built atop the universal client, version-specific clients are also shipped with `ubersmith-api` to provide more robust API interactions.

Version-specific clients extend the `UbersmithClient` object by binding API sections to it, with each section having functions that correspond to API methods.


#### Example Usage
```python
from ubersmith.versions import *

config = UbersmithConfig(
    host='target-hostname-or-address',
    username='username-to-use',
    password='api-token-for-user',
)

api_client = get_client(version='5.1.3-rc2', config=config)

client_info = api_client.client.get(
  client_id=1234,
  metadata=True,
)
```


> [!TIP]
> Version specific clients are built using JSON schema files generated with API calls against an Ubersmith instance running the target version.
> 
> If your version is not supported, you are encouraged to generate a schema and submit its schema in a PR.  
> See the [schema docs](SCHEMAS.md) for details on how to get started with generating and using schemas.


> [!IMPORTANT]
> Some API methods shipped by Ubersmith have unsafe parameter names.  
> In these cases, the parameters and sometimes methods are omitted from generation to prevent unwanted errors.


## License
MIT - Feel free to use, extend, and contribute.