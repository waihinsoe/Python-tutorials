import mysql.connector

dbConnection = mysql.connector.connect(
    
    host = 'localhost',
    user = 'root',
    password = 'waihin'
)
print(dbConnection)