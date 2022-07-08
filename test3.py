import os
import pandas as pd
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import creds
import re

def get_service_simple():
    return build('sheets', 'v4', developerKey=creds.api_key)


def get_service_sacc():
    creds_json = os.path.dirname(__file__) + "/creds/client_secret_573289065240-9revnk43eetpqgfvsarrd42fs1if4m68.apps.googleusercontent.com.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)

service = get_service_sacc()
sheet = service.spreadsheets()
sheet_id = "17y4xeTKvDV-diDpfK4Jx2cphQpUcQZFaCFcF-OoETjg"
resp = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=["скрипт!1:31000"]).execute()

test = resp.get('valueRanges')[0].get('values')
test_length = len(test)
test_length = test_length - 1

logic_name_num = 0
go_to_num = 0
prompt_name_num = 0
remark_num = 0
num = 0
for num in range(0, 10):
    for i in range(0, 9):
        if len(test[num]) > 8:
            if test[num][i] == 'Logic_name':
                logic_name_num = i
            if test[num][i] == 'Prompt_name':
                prompt_name_num = i
            if test[num][i] == 'GoTo':
                go_to_num = i
            if test[num][i] == 'Remark':
                remark_num = i

num = hello_logic_num = question1_logic_num = 0
while num != test_length:
    if len(test[num]) > 7:
        if test[num][logic_name_num] == 'hello_logic':
            hello_logic_num = num
        if test[num][logic_name_num] == 'question1_logic':
            question1_logic_num = num
    num = num + 1

# проходимся по всей логике hello_logic
traversing_array = hello_logic_num
print('Hello_logic:')
while traversing_array != question1_logic_num:
    if len(test[traversing_array]) > 8:
        if test[traversing_array][go_to_num] != '':
            if re.search(r'hangup_null', test[traversing_array][go_to_num]):
                print('\t','-(КОНЕЦ ЗВОНКА)', test[traversing_array][remark_num])
            elif re.search(r'callback_manager', test[traversing_array][go_to_num]):
                print('\t\t\t\t','-(БОТ ЗАКОНЧИЛ РАБОТУ)', test[traversing_array][remark_num], ':\t\t', test[traversing_array][go_to_num])
            elif re.search(r'question1_main', test[traversing_array][go_to_num]):
                print('\t\t','-(ПЕРЕХОД ДАЛЕЕ)', test[traversing_array][remark_num], ':\t\t', test[traversing_array][go_to_num])
            elif re.search(r'question2_main', test[traversing_array][go_to_num]):
                print('\t\t','-(ПЕРЕХОД ДАЛЕЕ)', test[traversing_array][remark_num], ':\t\t', test[traversing_array][go_to_num])
            elif re.search(r'question3_main', test[traversing_array][go_to_num]):
                print('\t\t','-(ПЕРЕХОД ДАЛЕЕ)', test[traversing_array][remark_num], ':\t\t', test[traversing_array][go_to_num])
            elif re.search(r'question4_main', test[traversing_array][go_to_num]):
                print('\t\t','-(ПЕРЕХОД ДАЛЕЕ)', test[traversing_array][remark_num], ':\t\t', test[traversing_array][go_to_num])
            elif re.search(r'question5_main', test[traversing_array][go_to_num]):
                print('\t\t','-(ПЕРЕХОД ДАЛЕЕ)', test[traversing_array][remark_num], ':\t\t', test[traversing_array][go_to_num])

    traversing_array = traversing_array + 1



