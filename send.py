import requests
import datetime

x_api_key = '<API-KEY>'          # from damcorp
group_id = '<GROUP-ID>'   # from damcorp
url = 'https://g7omggvlc7.execute-api.us-east-1.amazonaws.com/dev/send_group' # url

def send_to_group(message):

    postHeaders = {
        'Content-type': 'application/json', 
        'x-api-key': x_api_key
    }

    json_data = {
        'group_id': group_id,
        'message': message
    }
    response = requests.post(url, json=json_data, headers = postHeaders)

    return response

# print("Status code: ", response.status_code)
# print("Printing Entire Post Request")
# print(response.json())

def get_rate_usd(bank):

    url = 'https://kurs.web.id/api/v1/bca'

    return requests.get(url).json()

kurs = get_rate_usd('bca')

message = """
Kurs USD (BCA)

Jual: Rp. [usd_jual],-
Beli: Rp. [usd_beli],-

[date_time]
"""
message = message.replace('[usd_jual]', f"{int(kurs['jual']):,}")
message = message.replace('[usd_beli]', f"{int(kurs['beli']):,}")
message = message.replace('[date_time]', datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))

print(message)
