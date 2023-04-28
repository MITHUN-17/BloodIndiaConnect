from twilio.rest import Client
from account_details import  account_detailss

class Info:
    def __init__(self,patient_name,donners_mobile_number,patient_admitted_hospital):
        self.accdet = account_detailss()
        # self.account_sid = "ACe599f3f9b69da75c72ad10b21b941c44"
        # self.account_token = "f0983135f10f69843d039e4db46e2d76"
        # self.account_sid = "AC43f8d6ef76a6916423323475b95de4d7"
        # self.account_token = "b7cc5260d753bcda270525376679063e"
        self.client = Client(self.accdet.account_sid, self.accdet.account_token)
        self.number = donners_mobile_number
        self.patient_name = patient_name
        self.patient_admitted_hospital = patient_admitted_hospital
    def whatsapp(self):
        self.message = self.client.messages \
            .create(to=f'whatsapp:+91{self.number}', from_='whatsapp:+14155238886',
                    body=f"Thanks For Your Support\n\nRequired Blood Received For {str(self.patient_name).upper()} \n\nAt \t{self.patient_admitted_hospital}")




    def text_message(self):
        self.message = self.client.messages \
            .create(

            body=f"Thanks For Your Support\n\nRequired Blood Received For {str(self.patient_name).upper()} \n\nAt\t {self.patient_admitted_hospital}",
            from_="+17087669827",
            to=f"+91 {self.number}"
        )