
import sys

def file_to_dict(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
            result_dict = {int(index + 1): value for index, value in enumerate(lines)}
        return result_dict
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return {}

def process_key(dict, key):
    try:
        key = int(key)
        line = dict[key]
        proxy, port, login, password = line.split(":")
        return proxy, port, login, password
    except KeyError:
        print(f"Key {key} not found")
        return None
    except ValueError:
        print(f"Error! Value {line} contains incorrect information")
        return None

file_path = input("Enter the address of proxy data file: ")
data = file_to_dict(file_path)
print("\n", data, "\n")


while True:
    linead = input("Enter proxy number ")
    proxy_type = int(input("Enter the type of proxies to use: 1 - HTTP, 2 - HTTPS "))
    if proxy_type != 1 and proxy_type != 2:
        print("Error! Only 1 or 2 can be entered here")
        sys.exit()
    result = process_key(data, linead)
    if result:
        proxy, port, login, password = result
        if proxy_type == 1:
            address_proxy = f"http://{login}:{password}@{proxy}:{port}"
        else:
            address_proxy = f"https://{login}:{password}@{proxy}:{port}"
        print(f"proxy = {proxy}, port = {port}, login = {login}, password = {password}")
        print(address_proxy)
    else:
        print("\n")
