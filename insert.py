def read_mac_id(cnt):
    f = open("mac_id.txt", 'rt')
    lines = f.readlines()
    r = open('insert_mac.txt', 'w')

    result_list = []

    for line in lines:
        test = line[0:2] + ":" + line[2:4] + ':' + line[4:6] + ':' + line[6:8] + ':' + line[8:10] + ':' + line[10:12]
        result_list.append(test)
        r.write(test + '\n')

    # for c in range(1, cnt):
    #     r = open(f'{c}_insert_mac.txt', 'w')
    #
    #     for i in result_list[0:int(f'{c}')+000]:
    #         r.write(i + '\n')
    for c in range(1, int(cnt)):
        r = open(f'{c}_test', 'w')
        #for i in result_list[]

    r1 = open('4_insert_mac.txt', 'w')
    # r2 = open('2_insert_mac.txt', 'w')
    # r3 = open('3_insert_mac.txt', 'w')
    # r4 = open('4_insert_mac.txt', 'w')

    for i in result_list[3000:4000]:
        r1.write(i+'\n')

read_mac_id(4)