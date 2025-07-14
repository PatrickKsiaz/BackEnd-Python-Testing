import mysql.connector

#host, database,username,passsword

conn = mysql.connector.connect(host='localhost',database='PythonAutomation', user='root', password='rahulshettyacademy')

print(conn.is_connected())

cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')


