import mysql.connector
class heartful:
    def __init__(self,date_of_donation,serial_number):
        self.serial_number=serial_number
        self.dateofdonation = date_of_donation
        self.connection = mysql.connector.connect(host='localhost',
                                             database='donners_list',
                                             user='root',
                                             password='VENKAT21o22oo2@')

        self.cursor = self.connection.cursor()
        sql_query_one="""Update doners_details set date_of_blood_donated = %s where donners_serial_number = %s"""
        self.input_data=(str(self.dateofdonation),self.serial_number)
        self.cursor.execute(sql_query_one, self.input_data)
        self.connection.commit()
        print("Record Updated successfully ")


        sql_select_query = """select * from doners_details where donners_serial_number = %s"""
        # set variable in query
        self.cursor.execute(sql_select_query, (self.serial_number,))
        # fetch result
        self.record = self.cursor.fetchall()
        print(self.record)
        for row in self.record:
            self.serial_number=row[0]
            self.name=row[1]
            self.mobile_number = row[3]
        self.cursor.close()
        self.connection.close()

