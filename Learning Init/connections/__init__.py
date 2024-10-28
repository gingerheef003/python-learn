print("Connections package imported\n")

# __all__ is required to import using *, specifying which modules/functions are imported
from .mobile import connect_to_mobile_data
__all__ = ['wifi', 'connect_to_mobile_data']