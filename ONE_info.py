from twilio.rest import Client
from account_details import account_detailss


class Info:
    def __init__(self,  location_to_be_reached, google_map_location,username,userbloodgroup,attender_number,sample_address):
        # self.account_sid = "ACe599f3f9b69da75c72ad10b21b941c44"
        # self.account_token = "f0983135f10f69843d039e4db46e2d76"
        # self.account_sid = "AC43f8d6ef76a6916423323475b95de4d7"
        # self.account_token = "b7cc5260d753bcda270525376679063e"
        self.accdet = account_detailss()
        self.client = Client(self.accdet.account_sid, self.accdet.account_token)
        self.linkk = google_map_location
        self.locaa = location_to_be_reached
        self.username = username
        self.userbloodgroup=userbloodgroup
        self.attendernumber=str(attender_number)
        self.sampleaddress=sample_address
        self.attendernumberinlist=[]
        for i in self.attendernumber:
            self.attendernumberinlist.append(i)

    def whatsapp(self,number,doners_serial_number,doners_name):
        self.number=number
        self.name =doners_name
        self.serial_number = doners_serial_number
        self.message = self.client.messages \
            .create(to=f'whatsapp:+91{self.number}', from_='whatsapp:+14155238886',
                    body=f"Hello {str(self.name).capitalize()} your donner's Id  {self.serial_number} \n\n{str(self.userbloodgroup).capitalize()} blood is needed for {str(self.username).capitalize()} \n\nAddress :{self.sampleaddress}\n\nContact Number {self.attendernumber} \n\nGoogle Map's Location: {self.locaa}"
                         f"\n\nGoogle Map: {self.linkk}")



    def caller(self,number):
        self.number = number
        a=str(self.locaa)
        v=a.split()
        print(v)
        self.empty=[]
        self.splittt=str(self.userbloodgroup).split()
        if (len(self.splittt[0])) == 2:
            self.empty.append(self.splittt[0][0])
            self.empty.append(self.splittt[0][1])
            self.empty.append(self.splittt[1])
            print(self.empty)
        else:
            self.splittt=str(self.userbloodgroup).split()
            fine=(self.splittt)
            self.empty.append(fine)

        self.call = self.client.calls.create(
            twiml=f"<Response><Say>{self.empty} [blood,is,needed,at] {v} [contact,number,is] {self.attendernumberinlist} [for,more,information,please,see,your,text message,and whatsapp],"
                  f"{self.empty} [blood,is,needed,at] {v} [contact,number,is] {self.attendernumberinlist} [for,more,information,please,see,your,text message,and whatsapp], "
                  f"{self.empty} [blood,is,needed,at] {v} [contact,number,is] {self.attendernumberinlist} [for,more,information,please,see,your,text message,and whatsapp] [  Thank,You],</Say></Response>",
            to=f"+91{self.number}",
            from_=self.accdet.local_number
        )

    def text_message(self,number,doners_serial_number,doners_name):
        self.number = number
        self.name = doners_name
        self.serial_number = doners_serial_number
        self.message = self.client.messages \
            .create(

            body=f"Hello {str(self.name).capitalize()} your donner's ID {self.serial_number} \n\n{str(self.userbloodgroup).capitalize()} blood is needed for {str(self.username).capitalize()} \n\nAddress: {self.sampleaddress}\n\nContact Number: {self.attendernumber} \n\nGoogle Map's Location :{self.locaa}:  \n\nGoogle Map: {self.linkk} ",
            from_=self.accdet.local_number,
            to=f"+91{self.number}"
        )
