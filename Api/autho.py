import requests

payload = {
    "username":"sandeep.v",
    "password":"1234567"
}

create = requests.post('https://xv24xrhpxa.execute-api.ap-south-1.amazonaws.com/v1/authToken',data=payload)
print(create)
