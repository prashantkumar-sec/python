# Practice Task
# create venv and activate it.
# install requests and colorama.

import requests
from colorama import Fore, Style

url = input("Enter URL: ")
try:
    r = requests.get(url, timeout=5)
    color = Fore.GREEN if r.status_code == 200 else Fore.RED
    print(color + f"{url} -> {r.status_code}" + Style.RESET_ALL)
except requests.RequestException as e:
    print(Fore.RED + f"Failed: {e}" + Style.RESET_ALL)