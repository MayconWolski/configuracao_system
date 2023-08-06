import pymysql

# Connect Database MySQL
bd_connect = pymysql.connect(host='localhost', port=3306, database='faitec_database', user='root', password='', autocommit=True)

# Create cursor

Cursor = bd_connect.cursor()

