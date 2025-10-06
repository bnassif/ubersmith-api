from ubersmith.client.api import *
import inspect

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
    
    def _get_parameters(self, method, inputs: dict) -> dict:
        """Returns the Signature of the target Method
        
        This method is used to simplify how parameters in a method are passed to the underlying client
        as keyword arguments to reduce templating/development work needed.

        Args:
            method (method): The method to inspect
        
        Returns:
            dict: The dictionary of *args **kwargs passed to a method
        """
        data = {}
        meta = None
        # Get the parameters of the provided method
        params = list(inspect.signature(method).parameters.keys())
        
        # If meta is in the parameters, remove it prior to looping
        # We'll add these with Ubersmith's desired structure after handlilng the initial bit
        if 'meta' in params:
            # Get the meta inputs separate from the rest
            meta = inputs.pop('meta')
            # Remove meta from the params to inspect
            params.remove('meta')
                
        for p in params:
            data.update({p: inputs[p]})
        
        if meta:
            # If meta is supplied, add those under the `meta_` arguments
            for k, v in meta.items():
                data.update({f'meta_{k}': v})
                
        return data
    
    def _get_section_name(self):
        return self.__class__.__name__.rstrip('API').lower()
    
    def _request(self, method, inputs):
        """Sends a request using the underlying client
        
        This method takes the calling method at the first parameter to perform inspection on it.
        Locals are also passed from the calling parameter so they can be formed and passed to the API.

        Args:
            method (method): The calling method, passed through raw
            data (dict, optional): _description_. Defaults to None.
        """
        data = self._get_parameters(method, inputs)
        command=f'{self._get_section_name()}.{method.__name__}'
        
        return self._client.request(command, data=data, parsed=True)