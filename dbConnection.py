import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password='2112*2112Mysql',
        database="lyrics"
)

#myCursor = mydb.cursor()

#myCursor.execute("select * from lyrics")

#result = myCursor.fetchall()

# for i in result:
#     print(i)

#print(mydb)