from twilio.rest import Client
from account_details import account_detailss

class Info:
    def __init__(self, name,serial_number,number):
        self.acdet = account_detailss()
        # self.account_sid = "ACe599f3f9b69da75c72ad10b21b941c44"
        # self.account_token = "f0983135f10f69843d039e4db46e2d76"
        # self.account_sid = "AC43f8d6ef76a6916423323475b95de4d7"
        # self.account_token = "b7cc5260d753bcda270525376679063e"
        # self.client = Client(self.account_sid, self.account_token)
        self.client = Client(self.acdet.account_sid, self.acdet.account_token)
        self.name = name
        self.serial_numbers = serial_number
        self.number= number
        self.heart="\U00002764"
    def whatsapp(self):
        self.message = self.client.messages \
            .create(to=f'whatsapp:+91{self.number}', from_='whatsapp:+14155238886',
                    body=f"Welcome {self.name}\n\nYour unique Donners Id : {self.serial_numbers}\n\nYour little effort can give others a second chance to live life\n\n\t\t\t\t\t\tThank You{self.heart}")




    def text_message(self):
        self.message = self.client.messages \
            .create(

            body=f"Welcome {self.name}\n\nyour unique serial Number {self.serial_numbers}\n\nYour little effort can give others a second chance to live life\n\n\t\t\t\t\t\tThank You{self.heart}",
            from_="+17087669827",
            to=f"+91 {self.number}"
        )