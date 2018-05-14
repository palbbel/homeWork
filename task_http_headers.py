import json
import re


def http_headers_to_json(path_src, path_dest):
    data_dict = {}

    with open(path_src) as f:
        list_line = f.readlines()

    for row in list_line[1:]:
        if row != '\n':
            data_dict.update([[x.strip() for x in row.split(': ')], ])

    element1 = list_line[0][:list_line[0].find(' ')]
    element2 = list_line[0][list_line[0].find(' ')+1:list_line[0].find(' ', list_line[0].find(' ')+1)]
    element3 = list_line[0][list_line[0].find(' ', list_line[0].find(' ')+1)+1:].replace('\n', '')

    check_answer = re.match('HTTP', list_line[0])
    # файл с заголовком запроса
    if not check_answer:
        data_dict.update({'method': element1})
        data_dict.update({'uri': element2})
        data_dict.update({'protocol': element3})

    # файл с заголовком ответа
    else:
        data_dict.update({'protocol': element1})
        data_dict.update({'status_code': element2})
        # проверяем версию (не 2 версия)
        if list_line[0][:6] != 'HTTP/2':
            data_dict.update({'status_message': element3})

    with open(path_dest, 'w') as f:
        json.dump(data_dict, f, indent=4)

if __name__ == '__main__':
    path_src = input()
    path_dest = input()
    http_headers_to_json(path_src, path_dest)

