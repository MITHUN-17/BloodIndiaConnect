from twilio.rest import Client
from  account_details import  account_detailss

class Info:
    def __init__(self, name,date,number):
        self.accdet = account_detailss()
        self.client = Client(self.accdet.account_sid, self.accdet.account_token)
        self.name = name
        self.date =date
        self.number= number
        self.heart="\U00002764"
    def whatsapp(self):
        self.message = self.client.messages \
            .create(to=f'whatsapp:+91{self.number}', from_='whatsapp:+14155238886',
                    body=f"Thank You {str(self.name).upper()}\n\n{str(self.name).upper()} is the reason for SomeOnce's HeartBeat\n\n You Become The Saviour Just By Donating Your Blood \n\n"
                         f" date of donation:{self.date}\n\n\t\t\t\t\t\t\t\t\t\t {self.heart}THANK YOU{self.heart}")




    def text_message(self):
        self.message = self.client.messages \
            .create(

            body=f"\nThank You {str(self.name).upper()} \n\n{str(self.name).upper()} is the reason for Someonce's HeartBeat\n\nYou Become The Saviour Just By Donating Your Blood \n\n"
                         f" date of donation:{self.date}\n\n\t\t\t\t\t\t\t\t\t\t {self.heart}THANK YOU{self.heart}",
            from_="+17087669827",
            to=f"+91 {self.number}"
        )
