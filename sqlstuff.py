import pandas as pd
import pymysql

connection = pymysql.connect(host="localhost", user="root", password="000000", db="chatbot_test")
cursor = connection.cursor()
data = {'Text':[], 'UserID':[]}
df = pd.DataFrame(data)
sql1 = "insert into messages(Text, UserID) values (%s, %s)"

def sql_inject(msg, addr):
    injection = (msg, addr)
    cursor.execute(sql1, injection)
    connection.commit()
    print("[SERVER SQL] Message Injected!")