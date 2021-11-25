import requests
import json
import jsonpath

class Myauth(requests.auth.AuthBase):
    def __call__(self,r):
        return r
url = 'https://xv24xrhpxa.execute-api.ap-south-1.amazonaws.com/v1/authToken'
requests.get(url, auth=Myauth())

