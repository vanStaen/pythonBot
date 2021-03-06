import json
import mysql.connector
from mysql.connector import Error

# Get Data for conection to mySQL
with open('../../config.mysql.db.json', 'r') as config:
    data = config.read()
dbData = json.loads(data)
for db in dbData['awardspace']:
    name = db['name']
    host = db['host']
    user = db['user']
    database = db['database']
    pwd = db['pwd']

print('#############################')
print(f"Connection to {name}")

# Connect to MySQL
try:
    connection = mysql.connector.connect(host=host,
                                         database=database,
                                         user=user,
                                         password=pwd)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
