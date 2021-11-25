import requests
import json
import urllib
import jsonpath

resp = requests.get("https://api-docs.growsimplee.com/#fe6e310b-0b31-43b2-8072-f73bf5ee104e")
code = resp.status_code
assert code == 200, "code doesn't match"
print(resp.text)

print(resp.content)

print(type(resp.headers))
print(resp.cookies)
print(resp.encoding)
print(resp.url)

