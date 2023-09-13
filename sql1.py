from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
                  )

cursor = conn.cursor()
print("连接成功")

conn.select_db("students")
cursor.execute("SELECT * FROM student")
reslut = cursor.fetchall()
for r in reslut:
    print(r)

conn.close()