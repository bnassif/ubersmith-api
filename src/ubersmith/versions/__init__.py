from __future__ import annotations

from ubersmith.client import UbersmithClient, UbersmithConfig
from importlib import import_module
from pkgutil import iter_modules
from typing import Any, Callable

__all__ = [
    'UbersmithClient',
    'UbersmithConfig',
    'get_client',
    'list_supported_versions',
]

def normalize_version(version: str) -> str:
    """Normalize a version string to a module name

    Args:
        version (str): The version string. This can be returned from `UbersmithClient.system_info()['version']`

    Returns:
        str: The normalized version module name
    """
    version = version.strip().lower()

    version = version.removeprefix("v").replace(".", "_").replace('-', '_')
    return f"v{version}"

def get_client(version: str, client: UbersmithClient = None, config: UbersmithConfig = None) -> Any:
    if not (client or config):
        raise ValueError('Must supply either a client or config, not both')
    
    module_name = normalize_version(version)

    try:
        module = import_module(f"ubersmith.versions.{module_name}")
    except ModuleNotFoundError as exc:
        raise ValueError(
            f"Unsupported Ubersmith version '{version}'. "
            f"Expected one of: {', '.join(sorted(list_supported_versions()))}"
        ) from exc

    try:
        factory: Callable = module.get_full_client
    except AttributeError as exc:
        raise RuntimeError(
            f"Version module 'ubersmith.versions.{module_name}' "
            f"does not define get_full_client()."
        ) from exc

    return factory(client=client, config=config)

def list_supported_versions() -> list[str]:
    """Return a list of supported versions

    Returns:
        list[str]: The supported modules
    """
    return [m.name for m in iter_modules(__path__)]
