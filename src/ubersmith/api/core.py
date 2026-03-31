from ubersmith.client.api import *
from typing import Dict

__all__ = [
    'UbersmithClient',
    'UbersmithConfig',
    'Section',
]

class Section:
    """
    Base API Section Class
    
    This class is used to represent an API section in the Ubersmith API. It's a simple entry to binding
    a client to an arbitrary class, which will then have methods which call on the bound client.
    """
    _client: UbersmithClient
    
    def __init__(self, client: UbersmithClient = None, config: UbersmithConfig = None):
        """Instantiate a Client Section by binding a client to it.
        
        If a client is not supplied, attempt loading the configuration from the environment
        and binding a client bound to that configuration instead. Optionally, provide a configuration
        instead of a client.
        
        An error will be thrown if both a client and config are supplied.

        Args:
            client (UbersmithClient, optional): The client to bind to the class. Defaults to None.
            config (UbersmithConfig, optional): The config to instantiate a client from to bind to the class. Defaults to None.

        Raises:
            Exception: A base Exception is raised when both a client and config are supplied
        """
        if config and client:
            raise Exception("Both a client and config cannot be supplied")
        
        if client:
            # Bind the client, if supplied
            self._client = client
        else:
            # Binds a supplied config, or allows the underlying client to instantiate one
            self._client = UbersmithClient(config=config)
    
    def _request(self, method: str, **kwargs):
        """Sends a request using the underlying client
        
        This method takes the calling method at the first parameter to perform inspection on it.
        Locals are also passed from the calling parameter so they can be formed and passed to the API.

        Args:
            method (str): The calling method, passed through raw
        """
        
        if 'meta' in kwargs:
            meta: Dict = kwargs.pop('meta')
            for k, v in meta.items():
                kwargs.update({f'meta_{k}': v})
        
        return self._client.request(method, data=kwargs)