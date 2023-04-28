import mysql.connector
from mysql.connector import Error
from datetime import date
today=date.today()
def insert_varibles_into_table(patient_id,patient_name, patient_blood_group,date, location,attender_number,city):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='patient_List',
                                             user='root',
                                             password='VENKAT21o22oo2@')
        cursor = connection.cursor()
        mySql_insert_query = """Insert into patient_details (patient_id,patient_name,patient_blood_group,date_of_admitted,location,attender_number,city)
                                values (%s,%s,%s,%s,%s,%s,%s)
                                 """

        record = (patient_id,patient_name, patient_blood_group, date, location,attender_number,city)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into patient_details table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")

class patient_details_database:
    def __init__(self,patient_id,patient_name,patient_blood_group,date_of_admitted,location,attender_number,city):
        self.patient_id = patient_id
        self.patient_name=patient_name
        self.patient_blood_group = patient_blood_group
        self.date = date_of_admitted
        self.location =location
        self.attender_number = attender_number
        self.city = city
        insert_varibles_into_table(self.patient_id,self.patient_name,self.patient_blood_group,self.date,self.location,self.attender_number,self.city)




class Patient_datas:
    def __init__(self, patient_id : int):
        self.id =  patient_id
        self.connection = mysql.connector.connect(host='localhost',
                                                  database='patient_list',
                                                  user='root',
                                                  password='VENKAT21o22oo2@')

        self.cursor = self.connection.cursor()
        sql_select_query = """select * from patient_details where patient_id = %s """
        self.cursor.execute(sql_select_query, (self.id,))
        self.record = self.cursor.fetchall()
        print(self.record)
        for row in self.record:
           self.patientid    =  row[0]
           self.patientname  =  row[1]
           self.patientbloodgroup = row[2]
           self.dateofdonation    = row[3]
           self.location = row[4]
           self.attendernumber = row[5]
           self.city = row[6]
           print(self.patientid,self.patientname,self.patientbloodgroup,self.dateofdonation,self.location,self.attendernumber,self.city)
        self.cursor.close()
        self.connection.close()

