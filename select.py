import pymysql

#connect to the database
connection = pymysql.connect(host ='localhost',
                             user = 'root',
                             password='admin',
                             database='demo2',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
		sql="SELECT * FROM student"
		cursor.execute(sql)
		result=cursor.fetchone()
		print(result)