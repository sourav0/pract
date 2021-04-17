import pymysql

myconn = pymysql.connect(host="localhost", user="root", passwd="1234")
cur = myconn.cursor()

try:
    dbs = cur.execute("show databases")
except:
    myconn.rollback()
for x in cur:
    print(x)

# printing the connection object
print(myconn)