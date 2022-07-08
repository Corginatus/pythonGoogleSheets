# skript_reader
import random
import re
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import json
import creds


def get_values():
    values = [['Done']]
    # values = [[randrange(10, 99) for _ in range(0, 6)]]
    # values = [['Done'] for _ in range(0, 3)]
    # values = [[items[y][x] for x in range(0, 4)] for y in range(0, len(items))]
    return values


def get_service_simple():
    return build('sheets', 'v4', developerKey=creds.api_key)


def get_service_sacc():
    cr = """{"type": "service_account",
  "project_id": "python-pr-342609",
  "private_key_id": "0fa86526d1e0c80babc26437ae9cf0219eb107df",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC+WwghkOOUHzgN\nSNi64EVVdP1c4uww92+4Zi7DjKWDXyd6jPFaz0tuhEWIDJheyfIUhBUiEcg8DNFH\ncPQ6w2pPjcf97b6GJR3cCxtOYI7Po2YwV99g22doKpqCowjAflWchv6X1R/ibcen\nLNFtdhw1u8jmCfjtk3ewYrW5umZSJhjY/G3u78glqFt4D8GQA2yid6kFWHbUBmHS\n5Gf4qzAZ1GBdu/q9PeDyiidG4zwVb+ARSR0xHQ3p4y66Yj8YeDbrYL3FQxA9WC4L\nDuwgt12C/bGtxpGfrqohgNoIcCERKElSUyDPupBb6eQxJXFIx66JnNn0eumxPnCL\nY/hWNvuDAgMBAAECggEAV4XZjj1lNjTIe+szo3D80BcTa4L24GjUmG97LvRbIbU9\nnK5zRrKrVyxAIBbSdDrcMKyuXtTYQSwPiY6Y7O/u0Jc7Djki8eDdAtCkhHwHDddu\nY+nzTkBzIkT8d/ZoTsGHsYmsQ7l9iIm7U9Vakb7Np7Mo4wRQzUORs6sfLT9UTo5j\ndiCA/km0tjp48c8JlU76alcko6oBwZPTFHu90dMgcvzsGQVkhGjmAb7XQW7PoGQ1\n5dYs5ac+Bcwai0//8gSqeKPAiepjVv5YhovRNkoorY15rgl3rXm+BDMCs32Xjc/Z\nslLjeoT+/1akRz5pd8Lk94NQyi+t09E9TOfYORTUSQKBgQD26hH7nw9+WqGbkir7\nNA5GoXG76AlRmbS/wOR0EMXOXIKGrAXIEBM7PK4USL5v8qqdJbuKKMEJo0mPnDVO\nAE0FWQuhsGzkO1jruegRIegjxmou38im68RhK4Cs3mn16p8OJidEx/cery8YNdyH\nXhG8Ar3WwWyY+Nl4Trk8F9U0TQKBgQDFXC3MlrlccQ4/82s9r7qH2rp58ubbhd2t\nuUfzc2U2u8U2W1/iyOsc95VdXrjRI1dVX1B79+by+m9yNvhENRdefFF7A8t/yfIC\niE2BGg1LkCAlcywCG91XiBEGMLUro80fzErwNmrqLtXeBNP9g87gP8tB6y/j3G62\nlMqRSB4XDwKBgQDA24EiTVH3umiiL+Ach8NizbUdNRcaQnlYkRyfv34ROlbFQ9Xc\nNxoeWb4Kn+sHW76BsjgyqLRmh8DsR/GmtDt0ouGf8EKNXgGNVY762sYMM206oZaD\nMoIX97ewzqRq7VBA5/IiGiJeOC0Ltv5CSWqGtIl9FWVycmTCQJMUafUgvQKBgCcc\nyYbOKBYF4ckSuKIU/WaHFoWsecvvj6sqGPRKXjimpcLMAQi0wMOQ3W0PpJjt5BTr\nOswWqRJmR0ffVPxPeT4kbRFwAxhkMS4HTTTUsOXUvkottP8F/qumL5mGdaEcaT5w\nAjnwzudyOLgzRL/tK0aN3f5GWctSmC5e9nYsUKpJAoGASwJmdJ9NGf2po1nfOFrJ\nwUXD/rbBXIqDaOHNRHs/pSzAojf5jOj8Eg9+cPNxPsmV5SMjbBU1lAmWyJCYJzvO\nHkyFMA9GSFGAlDNTuYdt77InRglY2pncHy770Ey3WuoHS2pPYE8WL85bgIHvUr3T\n9rVs5XFbLTNEI4XvLCXrtac=\n-----END PRIVATE KEY-----\n",
  "client_email": "service-account@python-pr-342609.iam.gserviceaccount.com",
  "client_id": "110632577635186306018",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/service-account%40python-pr-342609.iam.gserviceaccount.com"}"""

    creds_json = json.loads(cr, strict=False)
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


service = get_service_sacc()
sheet = service.spreadsheets()
sheet_id = "1kHJ26GAK1PYqlzkNEejdd1QcTiMrI0a2yCMGju9Q_D8"

respF = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=["Sheet2!F1:F1000"]).execute()
respE = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=["Sheet2!E1:E1000"]).execute()


def read_skript(sheet_name, my_rage, my_number):
    skript = True

    print('my_number', my_number)

    #...

    my_ranges = sheet_name + "!H1:H1000"
    GoTo = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=[my_ranges]).execute()
    my_ranges = sheet_name + "!A1:A1000"
    Number = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=[my_ranges]).execute()
    my_ranges = sheet_name + "!F1:F1000"
    Pattern = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=[my_ranges]).execute()
    my_ranges = sheet_name + "!D1:D1000"
    Prompt_name = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=[my_ranges]).execute()
    my_ranges = sheet_name + "!E1:E1000"
    Prompt_text = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=[my_ranges]).execute()

    column_GoTo = GoTo.get('valueRanges')[0].get('values')
    column_Number = Number.get('valueRanges')[0].get('values')
    column_Pattern = Pattern.get('valueRanges')[0].get('values')
    column_Prompt_name = Prompt_name.get('valueRanges')[0].get('values')
    column_Prompt_text = Prompt_text.get('valueRanges')[0].get('values')

    # column_Number - column_Prompt_name - column_Prompt_text - column_Pattern - column_GoTo

    number_element = 0
    for item in range(len(column_Number)):
        # print(column_Number[i])
        if str(column_Number[number_element]) == str(my_number):
            break
        number_element = number_element + 1

    print(column_Number[number_element], column_Prompt_name[number_element], column_Prompt_text[number_element], column_Pattern[number_element],
          column_GoTo[number_element])


    mass_Prompt_text = []
    pre_intermediate_array = []
    intermediate_array = []




    print(random.choice(re.split(r'/', str(column_Pattern[number_element]))))

    print('number_element', number_element)


    prompts = re.split(r'\'', str(column_GoTo[number_element]))[1].replace(' ', '')
    if re.search(r'->', prompts) is not None:
        pre_intermediate_array = re.split(r'->', prompts)
        print(pre_intermediate_array)
        for element in pre_intermediate_array:
            if re.search(r'&', prompts) is not None:
                my_string = ''
                intermediate_array = re.split(r'&', element)
                for i in intermediate_array:

                    prompt_name_num = 0
                    prompt_text_num = 0
                    for cpn in column_Prompt_name:
                        if '[\'' + str(i) + '\']' == str(cpn):
                            prompt_text_num = prompt_name_num
                        prompt_name_num = prompt_name_num + 1
                    # print('str(column_Prompt_text[prompt_text_num])', str(column_Prompt_text[prompt_text_num]))
                    if re.search(r'\'', str(column_Prompt_text[prompt_text_num])) is not None:
                        my_pre_string = re.split(r'\'', str(column_Prompt_text[prompt_text_num]))[1]
                        my_string = my_string + my_pre_string
                mass_Prompt_text.append(my_string)

    print('ожидаемые_фразы')
    for i in mass_Prompt_text:
        print(i)

    result_data = []
    for i in mass_Prompt_text:
        result_data.append(random.choice(re.split(r'/', str(column_Pattern[number_element]))))

    print(result_data)

    #...

    if skript == True:
        my_value = [["TRUE"]]
    else:
        my_value = [["FALSE"]]

    resp = sheet.values().update(
        spreadsheetId=sheet_id,
        range=my_rage,
        valueInputOption="RAW",
        body={'values': my_value }).execute()


if __name__ == '__main__':
    column_F = respF.get('valueRanges')[0].get('values')
    column_E = respE.get('valueRanges')[0].get('values')


    if column_F is not None and column_E is not None:
        if len(column_F) < len(column_E):
            sheet_name = re.split(r'\'', str(column_E[0]))[1]

            print("column_F - ", len(column_F))
            print("column_E - ", len(column_E))
            my_rage = "Sheet2!F" + str(len(column_F) + 1)
            my_number = column_E[len(column_F)]
            read_skript(sheet_name, my_rage, my_number)




# if done_A is not None:
#     if len(done_A) > 4:
#         if done_B is not None:
#             if len(done_B) == len(done_A):
#                 print('Равны')
#                 sheet_read = re.split(r'\'', str(done_B[0]))[1]
#                 agent_name = re.split(r'\'', str(done_B[1]))[1]
#                 bot_phrase = re.split(r'\'', str(done_B[2]))[1]
#                 phrases_count = re.split(r'\'', str(done_B[3]))[1]
#
#                 my_rage = str(sheet_read) + '!1:1000000'
#                 resp = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=my_rage).execute()
#                 my_data = resp.get('valueRanges')[0].get('values')
#                 # print(my_data)
#                 num = 0
#                 pre_result_data = []
#                 result_data = []
#                 for i in my_data:
#                     if i[0] == agent_name and i[1] == bot_phrase and int(i[3]>=phrases_count):
#                         # print(i)
#                         pre_result_data.append(i[2])
#
#                 for q in range(0, 10):
#                     phrase_cut = random.choice(pre_result_data)
#                     # print(phrase_cut)
#                     result_data.append(re.split(r':', phrase_cut)[1])
#             else:
#                 print('Не равны')
#                 index = len(done_A)
#                 # print(phrases[index])
#                 my_rage = "Sheet1!B" + str(index)
#                 # print(my_rage)
#                 # print(done_A[index-1])
#                 qwe = re.split(r'\'', str(done_A[index-1]))
#                 my_mass = re.split(r'/', str(qwe[1]))
#                 print(my_mass)
#                 resp2 = sheet.values().update(
#                     spreadsheetId=sheet_id,
#                     range=my_rage,
#                     valueInputOption="RAW",
#                     body={'values': get_values()}).execute()
