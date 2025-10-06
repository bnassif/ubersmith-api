from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from os import getenv

__all__ = [
    'UbersmithConfig',
]

# Set the default .env file path -- this can be overridden upon instantiation with _env_file=<path>
default_dotenv_path = Path(
    getenv(
        key='UBERSMITH_API_ENV_FILE',  # Allows users to specify an env variable for the config file
        default=f"{str(Path.home())}/.ubersmith.env")  # Defaults to a home directory config file
)


class UbersmithConfig(BaseSettings):
    """
    A class to hold the configuration settings for the PowerDNS API client.
    """
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_prefix='UBERSMITH_',
        env_file=default_dotenv_path.resolve(),
    )
    
    username: str = Field(
        title="API Username",
        description="The API username to authenticate with.",
        repr=False
    )
    
    password: str = Field(
        title="API Password",
        description="The API password for the API Username.",
        repr=False,
    )
    
    host: str = Field(
        title="API Host",
        description="The IP address or hostname of the API server to connect to.",
        default='localhost'
    )
    port: int = Field(
        title="API Port",
        description="The Port number of the API server to connect to.",
        ge=1, le=65535, default=443
    )
    secure: bool = Field(
        title="HTTP Security",
        description="Whether to make secure (HTTPS) or insecure (HTTP) requests",
        default=True,
    )
    version: str = Field(
        title="API Version",
        description="The PowerDNS API verion to use.",
        default='2.0', repr=False
    )
    verify: bool = Field(
        title="Verify Certificate",
        description="Whether to verify the server certificate if secure is True",
        default=True,        
    )

    # API Client Settings
    api_delay: float = Field(
        title="API Delay",
        description="The time to wait between retries.",
        gt=0, le=60, default=15, repr=False
    )
    api_timeout: int = Field(
        title="API Timeout",
        description="The time to wait for a response after making a request before failing.",
        ge=1, le=900, default=30, repr=False
    )
    api_tries: int = Field(
        title="API Retries",
        description="The amount of times to (re)attempt call before failing.",
        gt=0, le=25, default=1, repr=False
    )
    
    @property
    def _schema(self):
        if self.secure:
            return 'https'
        return 'http'

    @property
    def api_url(self):
        return f"{self._schema}://{self.host}:{self.port}/api/{self.version}"

    def update(self, data: dict = None, **kwargs):
        if data and not isinstance(data, dict):
            raise RuntimeError(f'Input data must be a dict. Received: {data}')
        elif kwargs and not data:
            data = kwargs
        elif kwargs and data:
            data.update(kwargs)
        self.__dict__.update(data)
