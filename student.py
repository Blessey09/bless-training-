import pymysql

#connect to the database
db = pymysql.connect(host ='localhost',
                             user = 'root',
                             password='admin',
                             database='demo2',
                             cursorclass=pymysql.cursors.DictCursor)
                             
#caching sha2: succeded by fast path.
cursor=db.cursor()
query='INSERT INTO student VALUES("John","Delhi",24,"OB129")'

#query='INSERT INTO student VALUES("Richard",24,"OB129")'
try:
        cursor.execute(query)
        db.commit()
except:
       db.rollback()
db.close()                     