# ubersmith.util.parse.py
import requests
from typing import Union

from ubersmith.util.exceptions import UbersmithException

__all__ = [
    'parse_response',
]

# This module contains the items needed for parsing objects from Ubersmith's API in a centralized
# manner. This is imported into ubersmith.core.api.py for the `APIClient.request_parsed()` method

def parse_response(response: requests.Response) -> Union[dict|list]:
    """
    Parse a response from the returned `requests.Reponse` object per Ubersmith's API structure

    Args:
        response (requests.Response): The response from the Ubersmith API

    Returns:
        Union[dict|list]: The nested `data` field in the response, if returned
    Raises:
        ubersmith.core.exceptions.UbersmithException: Raised when the response has an error
    """
    
    # Base HTTP response exceptions
    response.raise_for_status()
    
    # Gather the response body from the Response object
    body = response.json()
    
    # Raise UbersmithException if the status is not successful
    if not body['status']:
        raise UbersmithException(
            error_code=int(body['error_code']),
            error_message=str(body['error_message']),
        )
    
    # Otherwise, return the `data` field from the body
    return body['data']
