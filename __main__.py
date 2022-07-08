import os
import pandas as pd
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from random import randrange

import creds


def get_values(items):
    # values = [[randrange(10, 99)]]
    # values = [[randrange(10, 99) for _ in range(0, 6)]]
    # values = [[randrange(10, 99)] for _ in range(0, 3)]
    values = [[items[y][x] for x in range(0, 4)] for y in range(0, len(items))]
    return values


def get_service_simple():
    return build('sheets', 'v4', developerKey=creds.api_key)


def get_service_sacc():
    creds_json = os.path.dirname(__file__) + "/creds/client_secret_573289065240-9revnk43eetpqgfvsarrd42fs1if4m68.apps.googleusercontent.com.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


# service = get_service_simple()
service = get_service_sacc()
sheet = service.spreadsheets()

sheet_id = "1jecsOAeIkGgxa05SEPcNsmRb60NTDZ7M9aOGtacPw6w"

# resp = sheet.values().get(spreadsheetId=sheet_id, range="Sheet1!A1:A999").execute()

resp = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=["CKC_Bank_HR!2:31000"]).execute()

# print(resp['valueRanges'])
#for key in resp:
#    print(key)
#print(resp['spreadsheetId'])
#print(resp['valueRanges'])
#for key in resp:
#    print(key, '->', resp[key])
#for item in resp.items():
#    print(item)

print('\nvalueRanges:')
print('range -> ', resp.get('valueRanges')[0].get('range'))
print('majorDimension -> ', resp.get('valueRanges')[0].get('majorDimension'))
print('values(example) -> ', resp.get('valueRanges')[0].get('values')[4])
print('valueRanges -> values:')
test = resp.get('valueRanges')[0].get('values')
pd = test
test_length = len(test)
test_length = test_length - 1
print(test_length)


a = []
num = 0
b = []
b.append('msisdn')
b.append('result')
b.append('duration')
b.append('call_uuid')
a.append(b)
while num != test_length:
    num = num + 1
    if len(test[num]) > 8:
        if test[num][2] == "автоответчик":
            if int(test[num][5]) < 5 or int(test[num][5]) > 10:
                print(test[num][0] + " " + test[num][2])
                b = []
                b.append(test[num][0])
                b.append(test[num][2])
                b.append(test[num][4])
                b.append(test[num][6])
                a.append(b)


#print(a)
#print(test[3][0] + " " + test[3][2])
#print(test[124][0] + " " + test[124][1])
#print(test[1000][0] + " " + test[1000][2])
#print(pd[3][0] + " " + pd[3][2])

sheet = get_service_sacc().spreadsheets()
#
resp = sheet.values().update(
    spreadsheetId=sheet_id,
    range="CKC_Bank_HR_result!A1",
    valueInputOption="RAW",
    body={'values' : get_values(a) }).execute()

# resp = sheet.values().append(
#     spreadsheetId=sheet_id,
#     range="My_law_2.0_result!A1",
#     valueInputOption="RAW",
#     body={'values' : get_values(a) }).execute()


print(len(a))
