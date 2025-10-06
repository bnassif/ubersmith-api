# ubersmith/util/exceptions.py

# This module contains the core Exception class that is used to wrap error responses from
# the Ubersmith API. This includes the error_code and error_message as provided from the API

__all__ = [
    'UbersmithException',
]

class UbersmithException(Exception):
    def __init__(self, error_code: int, error_message: str):
        self.error_code = error_code
        self.error_message = error_message
        # Pass a formatted string up to the base Exception
        super().__init__(f"{error_code}; {error_message}")

    def __str__(self):
        # Controls how it prints when raised
        return f"UbersmithException: {self.error_code}; {self.error_message}"