import json
import db_qry
import os
import cx_Oracle
from datetime import datetime

arr_stbId = []

# 터널링 정보
# 1.255.145.181 통해서
# 192.168.145.254:1521 을 2541 포트로 변경후 실행 요망!

if __name__ == '__main__':
    f = open("mac_address.txt", 'rt')
    lines = f.readlines()
    for line in lines:
        line = line.lower().replace('\n', '')
        line = line.replace(':0', ':')
        try:
            if str(line[0]) == '0':
                line = line[1:]

        except Exception as e:
            print(e)

        if line != '':
            arr_stbId.append(line)
    print(arr_stbId)

    with open('info.json', 'r') as f:
        oracle_info = json.load(f)

    # oracle client 관련
    LOCATION = r"C:/instantclient_19_10"
    os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]  # 환경변수 등록

    conn = cx_Oracle.connect(oracle_info['STG']['DB_USER'],
                             oracle_info['STG']['DB_PW'],
                             oracle_info['STG']['DB_HOST'],
                             encoding='UTF-8')

    cursor = conn.cursor()

    qry = db_qry.ORACLE_QRY % str(arr_stbId).replace("[","").replace("]","")

    cursor.execute(qry)

    result_stb_ids = cursor.fetchall()

    today = datetime.today().strftime("%Y.%m.%d-")

    r = open(today + "stb_id.txt", 'w')

    for i in result_stb_ids:
        r.write(str(i)+ '\n')

    r.close()
    f.close()
