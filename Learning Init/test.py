# import module from a package
from connections import mobile
mobile.connect_to_mobile_data()


# import function from a module in a package
from connections.wifi import connect_to_wifi
connect_to_wifi()

# use alias for a module imported from a package
import connections.wifi as w
w.connect_to_wifi()

# import all from a package; requires __all__ to be setup in __init__.py of the package
from connections import *
connect_to_mobile_data()
wifi.connect_to_wifi()
