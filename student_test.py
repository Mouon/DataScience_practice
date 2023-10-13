from db_conn import *

conn, cur = open_db('db2023')
sql = """select * from student;"""

cur.execute(sql)

r = cur.fetchone()
while r:
    print(r['sno'],r['sname'])
    r = cur.fetchone()
close_db(conn, cur)