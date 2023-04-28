from datetime import date
class patient:
    def __init__(self,user_name,user_blood_group,location):
        self.today=date.today()
        self.location=location
        self.name=user_name
        self.user_blood_group=user_blood_group
