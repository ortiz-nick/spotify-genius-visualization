import config
import mysql.connector

def connect():
    return mysql.connector.connect(
        host = config.DB_HOST,
        user = config.DB_USER,
        password = config.DB_PASSWORD,
        database = config.DB_NAME
)

#myCursor = mydb.cursor()

#myCursor.execute("select * from lyrics")

#result = myCursor.fetchall()

# for i in result:
#     print(i)
