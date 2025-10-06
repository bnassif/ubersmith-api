from ubersmith.client.base import *

__all__ = [
    'UbersmithConfig',
    'UbersmithClient',
]

class UbersmithClient(BaseClient):
    """
    API Client for the Ubersmith API
    
    Args:
        config (UbersmithConfig): The configuration object for the client.
    """
    
    def method_list(self) -> dict:
        """
        Lists all methods available in the target Ubersmith instance.
        This is the `data` field as returned by `uber.method_list`
        
        Returns:
            list[dict]: The list of methods available in the instance. Keys are the methods/commands and values are short descriptions.
        """
        return self.request('uber.method_list')
    
    def method_get(self, method_name: str) -> dict:
        """
        Gets the details of a specific API method.

        Args:
            method_name (str): The method name to gather details on (i.e. `uber.method_get`)
        """
        return self.request('uber.method_get', data={'method_name': method_name})
    
    def system_info(self) -> dict:
        """
        Gets the Ubersmith service version and latest version available

        Returns:
            dict: The response dictionary containing the version and latest_version
        """
        return self.request('uber.system_info')