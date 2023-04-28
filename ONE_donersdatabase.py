# import mysql.connector
# from mysql.connector import Error
# from datetime import datetime
#
# #creation of server connection
# def create_server_connection(host_name, user_name, user_password):
#     connection = None
#     try:
#         connection = mysql.connector.connect(host=host_name, user=user_name, passwd=user_password)
#         print(f"MySql Database Connection Successfully")
#     except Error as err:
#         print(f"Error: {err}")
#     return connection
#
# # crentential
# password = "VENKAT21o22oo2@"
# databasename = "Donners_List"
# connection = create_server_connection("localhost", "root", password)
#
# # creation of database
#
#
# # def create_database(query, conn):
# #     cursor = connection.cursor()
# #     try:
# #          cursor.execute(query)
# #          print(f"Database create successfully")
# #     except Error as err:
# #          print(f"Error ; {err}")
# #
# # create_database_query = f"Create database {databasename}"
# # create_database(create_database_query,connection)
#
# # connection to database
# def create_db_connection(host_name, user_name, user_password, db_name):
#     connection=None
#     try:
#         connection = mysql.connector.connect(host=host_name, user=user_name, passwd=user_password,database=db_name)
#         print(f"My sql database connection successfull")
#     except Error as err:
#         print(f"Error : {err}")
#     return connection
#
#
# def excute_query(conn,query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print(f"Query was successfull")
#     except Error as err:
#         print(f"Error : {err}")
#
# # create_order_table ="""
# # create table doners_details(
# # donners_serial_number int primary key,
# # donners_name varchar(50) not null,
# # donners_blood_group varchar(50) not null,
# # donners_mobile_number varchar(50));
# # """
#
# # insert_value="""
# # insert into doners_details values(02,"pandi_meena","o positive","7598571509");
# # """
# #
# #
# # connection = create_db_connection("localhost", "root", password, databasename)
# # excute_query(connection,insert_value)
#
#
# def read_query(conn ,query):
#     cursor = connection.cursor()
#     result =None
#     try:
#         cursor.execute(query)
#         result = cursor.fetchall()
#         return result
#     except Error as err:
#         print(f"Error ;{err}")
#
# select_statement = """
# select * from doners_details;
# """
# connection = create_db_connection("localhost", "root", password, databasename)
# results = read_query(connection,select_statement)
#
#
# class finallistofsuitabledoners:
#     def __init__(self,blood_group,city):
#         self.donersfinallist = []
#         self.bloodgroup=blood_group
#         self.city = city
#         for i in results:
#             if i[2] == self.bloodgroup:
#                 if i[5] == self.city:
#                     if i[4] == None:
#                         self.donersfinallist.append(i)
#                         print(i)
#                     else:
#                         n=str(i[4])
#                         m=n.split("-")
#                         da = datetime(int(m[0]),int(m[1]),int(m[2]))
#                         dff=datetime.now()-da
#                         if int(dff.days) > 120:
#                             self.donersfinallist.append(i)
#
#         # print(self.donersfinallist)
#

import mysql.connector
from datetime import datetime


class finallistofsuitabledoners:
    def __init__(self, blood_group, city):
        self.serial_number = blood_group
        self.city = city
        self.connection = mysql.connector.connect(host='localhost',
                                                  database='donners_list',
                                                  user='root',
                                                  password='VENKAT21o22oo2@')

        self.cursor = self.connection.cursor()
        sql_select_query = """select * from doners_details where donners_blood_group = %s and city = %s """
        self.cursor.execute(sql_select_query, (self.serial_number, self.city))
        self.record = self.cursor.fetchall()
        # print(self.record)
        self.donersfinallist = []
        for row in self.record:
            if row[4] == None:
                self.donersfinallist.append(row)
            else:
                n = str(row[4])
                m = n.split("-")
                da = datetime(int(m[0]), int(m[1]), int(m[2]))
                dff = datetime.now() - da
                if int(dff.days) > 120:
                    self.donersfinallist.append(row)
        # print(self.donersfinallist)
        self.cursor.close()
        self.connection.close()

