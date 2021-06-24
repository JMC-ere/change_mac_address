def f_read():
    f = open('f_stb_id.txt', 'rt')
    lines = f.readlines()
    r = open("f_stb_id_1.txt", "w")

    for line in lines:
        r_line = line.replace(',', '')
        s_line = r_line.split('"')
        result_line = "{"+s_line[1]+"}"
        print(result_line)
        r.write(result_line+'\n')



f_read()