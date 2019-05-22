import pymysql

db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     passwd = '123456',
                     database = 'students',
                     charset ='utf8')

cur = db.cursor()

# while 1:
#     name = input('Name:')
#     age = input("Age:")
#     gender = input("m or w:")
#     score = input("Score:")
#
#     sql = "insert from myclass (name,age,gender,score) values \
#           (%s,%s,%s,%s)"
#
#     try:
#         cur.execute(sql,[name,age,gender,score])
#         db.commit()
#     except Exception as e:
#         db.rollback()
#
# db.close()
# cur.close()

# try:
#     #插入
#     # sql = "insert into interest values (7,'mary','draw','A','8888','随便';)"
#
#     #修改
#     # sql = "update interest set price = 8888 where name = 'Bob'"
#
#     #删除
#     sql = "delete from interest where price > 8000"
#
#     cur.execute(sql)
#     db.commit()
# except Exception as e:
#     db.rollback()

sql = ""






cur.close()
db.close()
