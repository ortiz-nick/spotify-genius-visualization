import config
import mysql.connector

def connect():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
)

#myCursor = mydb.cursor()

#myCursor.execute("select * from lyrics")

#result = myCursor.fetchall()

# for i in result:
#     print(i)

#print(mydb)