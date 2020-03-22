import requests

x_api_key = '<API-KEY>'          # from damcorp
group_id = '<GROUP-ID>'   # from damcorp


message = 'ini test saja'       # from you

postHeaders = {
    'Content-type': 'application/json', 
    'x-api-key': x_api_key
}

url = 'https://g7omggvlc7.execute-api.us-east-1.amazonaws.com/dev/send_group' # url

json_data = {
    'group_id': group_id,
    'message': message
}
response = requests.post(url, json=json_data, headers = postHeaders)

print("Status code: ", response.status_code)
print("Printing Entire Post Request")
print(response.json())

