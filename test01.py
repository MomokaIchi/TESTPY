import requests

# https://openexchangerates.org/api/latest.json?app_id=Y7a637fc5eb0d4707a35076cfd7107eb9

response = requests.get("https://openexchangerates.org/api/latest.json?app_id=7a637fc5eb0d4707a35076cfd7107eb9")
data = response.json()
print(data)

