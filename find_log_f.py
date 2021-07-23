
def sibal():

    f = open('access.log_2021-07-22-23.txt', 'r')
    f = f.readlines()

    # SEARCH_TYPE 문자열이 없는 경우
    no_search_type_list = []
    # SEARCH_TYPE 을 담은 배열
    list_search_type = []

    dict_search_type = {}

    for log_row in f:
        if log_row.find('search_type') == -1:
            no_search_type_list.append(log_row)
        else:
            search_type = log_row[log_row.find('search_type='):log_row.find('search_type') + 14]
            search_type = search_type.replace('search_type=', '').replace('&', '').replace('l', '').replace(' ', '').replace('"', '')
            list_search_type.append(search_type)

    print(f"NO_SEARCH_TYPE_COUNT : {len(no_search_type_list)}건")

    # SEARCH_TYPE 이 없는 경우
    empty_search_type_count = 0

    for s_type in list_search_type:
        if s_type in '':
            empty_search_type_count += 1
        else:
            if s_type in dict_search_type:
                dict_search_type[s_type] = dict_search_type[s_type] + 1
            else:
                dict_search_type[s_type] = 1

    list_search_type_keys = list(dict_search_type.keys())

    dict_time = {}
    time_list = []

    for log_row2 in f:

        search_type = log_row2[log_row2.find('search_type='):log_row2.find('search_type') + 14]
        search_type = search_type.replace('search_type=', '').replace('&', '').replace('l', '').replace(' ', '').replace('"', '')

        for key in list_search_type_keys:
            if key == search_type:
                log_row1 = log_row2[log_row2.find('sec') - 6:log_row2.find('sec') - 5]
                time_list.append(log_row1)

    for s_time in time_list:
        if s_time in dict_time:
            dict_time[s_time] = dict_time[s_time] + 1
        else:
            dict_time[s_time] = 1

    print(dict_time)
    print(dict_search_type)


def one_one():
    f = open('access.log_2021-07-22-23.txt', 'r')
    f = f.readlines()
    print(f"LENGTH_LOG : {len(f)}")

    list_search_type = []
    list_log_time = []

    for log_row in f:
        if log_row.find('search_type') != -1:
            if log_row.find('sec') != -1:

                search_type = log_row[log_row.find('search_type'):log_row.find('search_type')+14]
                search_type = search_type.replace('l', '').replace('&', '').replace('search_type=', '').replace('"', '')
                list_search_type.append(search_type)

                log_time = log_row[log_row.find('sec')-6:log_row.find('sec')-5]
                log_time = log_time.replace(' ', '')
                list_log_time.append(log_time)




one_one()
