import requests
import urllib3

from ubersmith.config import UbersmithConfig
from ubersmith.util.cleaners import *
from ubersmith.util.parse import parse_response
from ubersmith.util.files import get_files

__all__ = [
    'UbersmithConfig',
    'BaseClient',
]

class BaseClient:
    """
    API Client for the Ubersmith API
    
    Args:
        config (Config): The configuration object for the client.
    """
    
    def __init__(self, config: UbersmithConfig = None):
        """
        Initialize the client with the provided config.
        If a config is not supplied, attempt loading one from the environment.
        

        Args:
            config (Config, optional): The Config to bind to the client. If not supplied, one is loaded from the environment.
        """
        self.config = config if config else UbersmithConfig()
    
    def request(self, command: str, data: dict = None, files: dict = None, raw: bool = False) -> requests.Response:
        """
        Makes a request to the Ubersmith API
        
        Args:
            command (str): The Ubersmith API command to call
            data (dict, optional): The POST data to send in the request. Defaults to None.

        Returns:
            requests.Response: The resposne from the Ubersmith API
        """
        
        if not self.config.verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        # Clean input data, if provided
        if data:
            clean_all(data)
        
        tries = 0
        for _ in range(tries, self.config.api_tries):
            try:
                response = requests.post(
                    # API URL of the request
                    url=f"{self.config.api_url}/?method={command}",
                    # Pass through data, if supplied
                    data=data,
                    # Attach files, if supplied
                    files=get_files(files),
                    # Add basic authentication using the user/pass
                    auth=(self.config.username, self.config.password),
                    # Add the timeout from the config
                    timeout=self.config.api_timeout,
                    verify=self.config.verify,
                )
                if not raw:
                    return parse_response(response)
                return response
            except requests.exceptions.Timeout:
                # Increment the tries counter and continue remaining attempts
                tries += 1
                continue