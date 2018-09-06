import requests, json
import subprocess
import sys

authorize_url = "https://api.codechef.com/oauth/authorize"
token_url = "https://api.codechef.com/oauth/token"

callback_uri = "http://127.0.0.1:8000/"

test_api_url = "https://api.codechef.com/contests/PRACTICE/problems/SALARY"

client_id = 'your client_id'
client_secret = 'your client_secret'

authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&state=xyz&redirect_uri=' + callback_uri 

#https://api.codechef.com/oauth/authorize?response_type=code&client_id=your_client_id&state=xyz&redirect_uri=http://yourdomain.com

print("go to the following url on the browser and enter the code from the returned url: ")
print("---  " + authorization_redirect_url + "  ---")
authorization_code = input('code: ')

headers = {
    'content-Type': 'application/json',
}
datas = {'grant_type': 'authorization_code', 'code': authorization_code, 'client_id': client_id, 'client_secret': client_secret, 'redirect_uri': callback_uri}
print("requesting access token")
access_token_response = requests.post('https://api.codechef.com/oauth/token', data=json.dumps(datas), headers=headers)

tokens = json.loads(access_token_response.text)
result = tokens["result"]
data = result["data"]
access_token = data["access_token"]

api_call_headers = {'Authorization': 'Bearer ' + access_token}
api_call_response = requests.get(test_api_url, headers=api_call_headers)

print(api_call_response.text)

