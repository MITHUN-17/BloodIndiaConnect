from twilio.rest import Client
from account_details import  account_detailss



class patient_attender_info:
    def __init__(self,patient_id,patient_name,patient_blood_group,patient_admitted_hospital,patient_admitted_hospital_city,patient_attender_mobile_number):
        self.patientid = patient_id
        self.number = patient_attender_mobile_number
        self.patientname = patient_name
        self.patientbloodgroup = patient_blood_group
        self.patientadmittedhospital = patient_admitted_hospital
        self.patientadmittedhospitalcity = patient_admitted_hospital_city
        self.accdet = account_detailss()

        # self.account_sid = "ACe599f3f9b69da75c72ad10b21b941c44"
        # self.account_token = "f0983135f10f69843d039e4db46e2d76"
        # self.account_sid = "AC43f8d6ef76a6916423323475b95de4d7"
        # self.account_token = "b7cc5260d753bcda270525376679063e"
        self.client = Client(self.accdet.account_sid, self.accdet.account_token)


    def whatsapp(self):
        self.message = self.client.messages \
            .create(to=f'whatsapp:+91{self.number}', from_='whatsapp:+14155238886',
                    body=f"\t\tPatient Detail's\n\nPatient Name : {self.patientname}\n\nPatient ID : {self.patientid}\n\nPatient Blood Group : {self.patientbloodgroup}"
                         f"\n\nPatient Admitted Hospital : {self.patientadmittedhospital}\n\nCity Of Hospital Located : {self.patientadmittedhospitalcity}")

    def text_message(self):
        self.message = self.client.messages \
            .create(

            body=f"\n\n\tPatient Detail's\n\nPatient Name : {self.patientname}\n\nPatient ID : {self.patientid}\n\nPatient Blood Group : {self.patientbloodgroup}"
                 f"\n\nPatient Admitted Hospital : {self.patientadmittedhospital}\n\nCity Of Hospital Located : {self.patientadmittedhospitalcity}",
            from_=self.accdet.local_number,
            to=f"+91{self.number}"
        )
