def connect_to_wifi() -> None:
    print("Connected to Wifi/n")

# share a function in a different module in the same package
from .mobile import share_mobile_data
def access_mobile_data_via_wifi() -> None:
    share_mobile_data()