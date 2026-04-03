from copy import deepcopy
from ubersmith.client.section import *

from ubersmith.versions.v4_6_1.client import ClientAPI
from ubersmith.versions.v4_6_1.device import DeviceAPI
from ubersmith.versions.v4_6_1.order import OrderAPI
from ubersmith.versions.v4_6_1.report import ReportAPI
from ubersmith.versions.v4_6_1.sales import SalesAPI
from ubersmith.versions.v4_6_1.support import SupportAPI
from ubersmith.versions.v4_6_1.uber import UberAPI

__all__ = [
    "ClientAPI",
    "DeviceAPI",
    "OrderAPI",
    "ReportAPI",
    "SalesAPI",
    "SupportAPI",
    "UberAPI",
    "UbersmithClient",
    "UbersmithConfig",
    "get_full_client",
]

def get_full_client(client: UbersmithClient = None, config: UbersmithConfig = None) -> UbersmithClient:
    if not (client or config):
        raise Exception('Must supply either a client or config, not both')
    
    if not client:
        # Get a client if config supplied
        c = UbersmithClient(config=config)
    else:
        # Otherwise, copy the provided client to not modify-in-place
        c = deepcopy(client)
        
    # Get the config if config not supplied
    if not config:
        config = c.config
    
    # Bind the sections to the client
    c.client = ClientAPI(config=config)
    c.device = DeviceAPI(config=config)
    c.order = OrderAPI(config=config)
    c.report = ReportAPI(config=config)
    c.sales = SalesAPI(config=config)
    c.support = SupportAPI(config=config)
    c.uber = UberAPI(config=config)
    
    return c