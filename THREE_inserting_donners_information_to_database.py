import mysql.connector

def insert_varibles_into_table(donner_serial_number,donner_name,donners_blood_group,donners_mobile_number,date_of_donation,city):
    global a
    try:
        connection = mysql.connector.connect(user='root', password='VENKAT21o22oo2@', host='localhost', database='donners_list')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO doners_details (donners_serial_number, donners_name, donners_blood_group, donners_mobile_number,date_of_blood_donated,city)
                                VALUES (%s, %s, %s, %s, %s, %s) """

        record = (donner_serial_number,donner_name,donners_blood_group,donners_mobile_number,date_of_donation,city)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into doners_details table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


class doner:
    def __init__(self,donner_serial_number,donner_name,donners_blood_group,donners_mobile_number,date_of_donation,city):
        self.serial_number = donner_serial_number
        self.name=donner_name
        self.blodd_group =donners_blood_group
        self.mobile_number = donners_mobile_number
        self.date = date_of_donation
        self.city =city
        insert_varibles_into_table(self.serial_number,self.name,self.blodd_group,self.mobile_number,self.date,self.city)


