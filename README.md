# Python Ubersmith
[![Pypi](https://img.shields.io/pypi/v/ubersmith-api)](https://pypi.org/project/ubersmith-api)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/bnassif/ubersmith-api/main/LICENSE)
![GitHub Release Date](https://img.shields.io/github/release-date/bnassif/ubersmith-api)

A fully-featured API wrapper for the [Ubersmith](https://ubersmith.com/) API

Python wrappers exist on PyPI and across GitHub for interacting with the Ubersmith API, but each of them fails to provide full compatibility.

In comes `ubersmith-api`...

## Overview

At its core, this package provides a generic API wrapper class, `UbersmithClient` which allows for uncontrolled calls to an Ubersmith instance.

Built atop this wrapper, a templating suite is available for generating classes for each API section in Ubersmith, specific to each Ubersmith version to maximize compatibility.

## Installation

```bash
# PyPi Installation
pip install ubersmith-api
# GitHub Installation
pip install git+'https://github.com/bnassif/ubersmith-api.git'
```

## Getting Started

### Instantiating the Base Client
```python
from ubersmith_api import *

config = UbersmithConfig(
    host='target-hostname-or-address',
    username='username-to-use',
    password='api-token-for-user',
)

client = UbersmithClient(config)
```

### Making Calls

```python
response_obj = client.request(
    'uber.method_get',
    data={
        'method_name': 'client.get',
    },
    #raw=True,
)
```

By default, the `request()` method will parse the response from the API, checking for HTTP error codes, as well as error messages from Ubersmith itself. If no errors are found, the returned `data` field is returned.

Alternatively, you can parse `raw=True` to return the `requests.Response` object for manual parsing and error checking.

### Shipped Methods
The `UbersmithClient` class comes with three (3) core methods shipped.  
These offer a simplified entrypoint to gathering parsed information of an Ubersmith system.

```python
# Get system information: calls `uber.system_info`
sys_info = client.system_info()

# Get all available methods: calls `uber.method_list`
all_methods = client.method_list()

# Get details of one method: calls `uber.method_get`
method_details = client.method_get('client.get')
```

## Future Compatibility

**NOTE**: 

Additional code is shipped in this repository, along with version-specific schemas for the Ubersmith API.  
These features will be enabled in later releases of the package.

## License
MIT - Feel free to use, extend, and contribute.