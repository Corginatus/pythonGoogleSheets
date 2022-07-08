import re
import os
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import creds
import requests

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

def start_analytics(v1,v2,v3):
    print('ANALYTICS:')
    service = get_service_sacc()
    sheet = service.spreadsheets()

    sheet_id = "1kHJ26GAK1PYqlzkNEejdd1QcTiMrI0a2yCMGju9Q_D8"

    refresh_token = ''
    try:
        str_encode = b'\xff\xfe9\x00X\x00u\x00X\x00X\x00H\x00b\x00P\x00'

        r = requests.post('https://api-v3.neuro.net/api/v2/ext/auth',
                          auth=("mylaw.api@gmail.com", str_encode.decode('UTF-16')))
        refresh_token = r.json()['refresh_token']
        print("Аутентификация прошла успешно!")
    except requests.ConnectionError:
        # nn.log('Error!')
        exit()

    company_uuids = ['96857848-a88f-4cb0-bad8-6f70f3ec6211', '1c07c539-916c-4519-b26a-2c7a67a6f24e',
                     'e3cd14a1-a289-4d2f-86ab-182dc5e889ce',
                     'd2069c81-b66a-4e8d-88b9-46e60ee01a34', '70196014-fa26-48fe-b586-84a752eee58f']

    all_agents = {}
    for company_uuid in company_uuids:
        try:
            print('Получение агентов...')
            url = f'https://api-v3.neuro.net/api/v2/ext/company-agents?company_uuid={company_uuid}'
            header = {'Authorization': "Bearer " + refresh_token,
                      'Content-Type': 'application/json'}

            r = requests.get(url, headers=header)

            all_agents[company_uuid] = r.json()
        except requests.ConnectionError:
            # nn.log('Error!')
            print("Ошибка при получении агентов!")
            exit()

    time_start = v2
    time_end = v3

    agent_name = 'qwe'

    agents_statistic = {}
    for company_uuid in company_uuids:
        for agent in all_agents[company_uuid]:
            try:
                '''time_start = (datetime.datetime.now(timezone(time_zone)) - datetime.timedelta(minutes=5, hours=(
                                                        3 + hour_offset))).strftime("%Y-%m-%d %H:%M:%S")
                                            time_end = (datetime.datetime.now(timezone(time_zone)) - datetime.timedelta(
                                                hours=(3 + hour_offset))).strftime("%Y-%m-%d %H:%M:%S")'''

                if agent['name'] != agent_name:

                    r = requests.post('https://api-v3.neuro.net/api/v2/ext/statistic/dialog-report',
                                      json={"agent_uuid": agent['agent_uuid'],
                                            "start": time_start,
                                            "end": time_end},
                                      headers={
                                          'Authorization': "Bearer " + refresh_token})

                    agents_statistic[agent['name']] = r.json()
                    for keyy, valuee in agents_statistic.items():
                        key = keyy
                        value = valuee

                    print('Получение данных...', key)

                    my_list = []
                    d1 = {}
                    # print(agents_statistic.keys())

                    if len(value['result']) > 0:  # если есть логи
                        # d1 = {}
                        check_list = {}
                        a = b = g = []
                        # print(key, '->', value)
                        for log in value.get('result'):
                            if 'call_transcript' in log.keys():
                                if len(log['call_transcript']) > 0:
                                    str_1 = log['call_transcript']
                                    result_list_of_conv = re.split(r';', str_1)
                                    if len(result_list_of_conv) > 1:
                                        for j in range(len(result_list_of_conv)):
                                            str_1 = result_list_of_conv[j]
                                            if re.search(r'bot', str_1) is None:  # если строка не бот
                                                if re.search(r'\):', result_list_of_conv[j - 1]) is None:
                                                    str_b = result_list_of_conv[j - 1]
                                                else:
                                                    res_2 = re.split(r'\):', result_list_of_conv[j - 1])
                                                    str_b = str(res_2[1])
                                                if re.search(r'\):', str_1) is None:
                                                    str_h = str_1
                                                else:
                                                    res_2 = re.split(r'\):', str_1)
                                                    str_h = str(res_2[1])
                                                flag = False
                                                if str_b in d1.keys():
                                                    n = next((i for i, x in enumerate(d1[str_b]) if x[0] == str_h),
                                                             None)
                                                    if n is not None:  # если есть строка(human) в ключе (bot)
                                                        d1[str_b][n][1] = d1[str_b][n][
                                                                              1] + 1  # d1[str_b][number][0] - ответ (human)
                                                    else:  # d1[str_b][number][1] - их кол-во
                                                        d1[str_b].append([str_h, 1])
                                                else:
                                                    d1[str_b] = [[str_h, 1]]

                        for key_t, value_t in d1.items():
                            print('\t', key_t, '->')
                            for k in value_t:
                                print('\t\t', k)
                                b = [key, 'Question: ' + key_t, 'Answer: ' + str(k[0]), 'Amount: ' + str(k[1])]
                                a.append(b)

                        my_range = str(v1 + '!A1')

                        sheet = get_service_sacc().spreadsheets()
                        resp = sheet.values().append(
                            spreadsheetId=sheet_id,
                            range=my_range,
                            valueInputOption="RAW",
                            body={'values': get_values(a)}).execute()

            except requests.ConnectionError:
                print('Вас забанили!(ошибкка при получение данных)')
                exit()


def menu():
    d = 0
    d1 = ''
    d2 = ''
    while True:
        print("##############################################################################")
        print('Данная программа заносит аналитику на лист answers/test'
              ' (Пожалуйста, перед использованием, убедитесь, что этот лист пустой)')
        print('Для того, чтобы начать выгрузку возражений, введите временной промежуток')
        print('Пример ввода(YY-MM-DD): ')
        print('">>> 2022-04-01 00:00:00"')
        print('">>> 2022-04-05 22:00:00"')
        print('Для выхода из программы введите "0" или "выход"')
        print("##############################################################################")
        x = str(input('>>> '))
        if x == '0' or x == 'выход':
            print("Выход из программы")
            break
        if re.findall(r'^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}$', x):
            print(str(d+1) + 'ая дата:',  x)
            d = d + 1
            if d == 1:
                d1 = x
            if d == 2:
                d2 = x
                my_str = 'answers'
                while True:
                    print('Введите название листа (test/answers)')
                    y = str(input('>>> '))
                    if y == 'test' or y == 'answers':
                        my_str = y
                        start_analytics(my_str, d1, d2)
                break
        if x == '1':
            print(d)


if __name__ == '__main__':
    menu()

