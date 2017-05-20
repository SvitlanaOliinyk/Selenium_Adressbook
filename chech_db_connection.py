import pymysql
from db_api.adressbook_orm import AdressbookORM
from model.group import Group

config = {
"host": "localhost",
"port": 8889,
"user": "root",
"password": "root",
"db": "test"
}

db = AdressbookORM(**config)


connection = pymysql.connect(**config)

try:
    for g in db.get_contacts_in_group(Group(id='30')):
        print(g)
finally:
    pass

# try:
#     with connection.cursor() as cursor:
#         sql = "select * from group_list"
#         cursor.execute(sql)
#         for row in cursor:
#             print(row)
# finally:
#     connection.close()