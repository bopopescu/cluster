import mysql.connector

def fromFiletoDB(file):
    conn = mysql.connector.connect(user='log', password='1', database='log_query')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS data(IP VARCHAR(15), date_time VARCHAR(30), functions VARCHAR(500));')

    file = open("access.log", 'r')
    for line in file.readlines():
        tmp = line.split(" ")
        # print "INSERT INTO data VALUES(\"%s\", \"%s\", \"%s\");" % (tmp[0], tmp[3].replace('[',''), tmp[6])
        cursor.execute("INSERT INTO data VALUES(\"%s\", \"%s\", \"%s\");" % (tmp[0], tmp[3].replace('[',''), tmp[6]))
    conn.commit()
    conn.close()
    file.close()

fromFiletoDB("access.log")
conn = mysql.connector.connect(user='log', password='1', database='log_query')
cursor = conn.cursor()
cursor.execute('')

# select * from data where functions REGEXP '(common|data|dm|permission|wifi|configdevice|deviceconfig|sp)';
# select * from data where functions not in (select functions from data where functions regexp '^/(common|data|dm|permission|wifi|configdevice|deviceconfig|sp|index.html)');
