import json


def read_2021():

    with open("2021_result.json", "r") as f:
        json_data = json.load(f)

    result_dict = {}

    aggs_data = json_data['aggregations']['target']
    for i in aggs_data['buckets']:
        print(i['key'])
        for z in i['NAME']['buckets']:
            print(z['key'])
            print(str(z['key']).upper().replace(':', ''))


read_2021()


def read_mac_id():
    f = open("mac_id.txt", 'rt')
    lines = f.readlines()
    r = open('insert_mac.txt', 'w')

    result_list = []

    for line in lines:
        test = line[0:2] + ":" + line[2:4] + ':' + line[4:6] + ':' + line[6:8] + ':' + line[8:10] + ':' + line[10:12]
        result_list.append(test)
        r.write(test + '\n')


def change_mac():

    f = open('insert_mac.txt', 'rt')
    lines = f.readlines()

    for line in lines:
        line = line.replace('\n', '')
        line = line.split(':')
        # print(line)
        list_line = []
        for i in range(0, len(line)):
            line_s = line[i]
            list_line.append(line_s)

        line_r = ':'.join(list_line)
        print(f'"{line_r.lower()}",')
