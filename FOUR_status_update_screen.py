# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import messagebox
# from ONE_donersdatabase import finallistofsuitabledoners
# from FOUR_status_update_info import Info
#
# class status_update_tkscreen():
#     def __init__(self):
#         def commandd():
#                self.pat_name = self.patient_name.get()
#                self.pat_blood_group = self.blood_group.get()
#                self.city = self.cities.get()
#                self.address = self.address_text.get('1.0',END)
#                a=str(self.address).split()
#                if self.pat_name != "" and self.pat_blood_group != "Select The Blood Group" and self.city != "Select The City" and a != []:
#                     self.button["state"] = DISABLED
#                     gg=finallistofsuitabledoners(self.pat_blood_group,self.city)
#                     print(gg.donersfinallist)
#
#                     for i in gg.donersfinallist:
#                            dddd=Info(self.pat_name,i[3],self.address)
#                            dddd.whatsapp()
#                            # dddd.text_message()
#                     print(self.city,self.pat_name,self.pat_blood_group,self.address)
#                     try:
#                         answer = messagebox.showinfo("INFO", "Successfully Informed Donors")
#                         Label(text=answer, font=('Arial 20 bold')).pack()
#                     except:
#                         pass
#                else:
#                    try:
#                        answer = messagebox.showinfo("INFO", "Please Enter All Fields")
#                        Label(text=answer, font=('Arial 20 bold')).pack()
#                    except:
#                        pass
#
#
#         self.screen_Four = Tk()
#         self.screen_Four.maxsize(950, 950)
#         self.screen_Four.minsize(950, 950)
#         self.screen_Four.title(string="Auto Contact Blood Don0rs")
#
#         self.info = Label(text="STATUS UPDATE")
#         self.info.grid(column=0, row=0)
#         self.info.config(font=("Arial", 22, "bold"))
#         self.info.config(pady=20, padx=350)
#
#         self.donners_name_label = Label(text="Enter the Patient's Name Below :")
#         self.donners_name_label.grid(column=0, row=1)
#         self.donners_name_label.config(font=("Arial", 15, "bold"))
#         self.donners_name_label.config(pady=20)
#
#         self.patient_name = Entry(width=50)
#         self.patient_name.grid(column=0, row=2)
#         self.patient_name.focus()
#
#         self.donners_blood_group_label = Label(text="Select the Patient's Blood Group:")
#         self.donners_blood_group_label.grid(column=0, row=3)
#         self.donners_blood_group_label.config(pady=20)
#         self.donners_blood_group_label.config(font=("Arial", 15, "bold"))
#
#         self.blood_group = StringVar(self.screen_Four)
#         self.blood_group.set("Select The Blood Group")
#         self.list_of_blood_group = OptionMenu(self.screen_Four, self.blood_group, "a positive", "a negative", "b positive",
#                                               "b negative"
#                                               , "ab positive", "ab negative", "o positive", "o negative")
#         self.list_of_blood_group.grid(column=0, row=4)
#         self.list_of_blood_group.config(height=2, highlightbackground="red", highlightthickness=10)
#
#
#         self.donners_locatiom = Label(text="Select the Location\City:")
#         self.donners_locatiom.grid(column=0, row=5)
#         self.donners_locatiom.config(pady=20)
#         self.donners_locatiom.config(font=("Arial", 15, "bold"))
#
#         self.cities = StringVar(self.screen_Four)
#         self.cities.set("Select The City")
#         self.list_of_location = OptionMenu(self.screen_Four, self.cities, "coimbatore", "chennai", "hosur", "madurai",
#                                            "karaikudi", "karur",
#                                            "trichy", "namkal")
#         self.list_of_location.grid(column=0, row=6)
#         self.list_of_location.config(height=2, highlightbackground="red", highlightcolor="blue", highlightthickness=10)
#
#         self.addressd = Label(text=f"Enter the Address")
#         self.addressd.grid(column=0, row=9)
#         self.addressd.config(pady=20)
#         self.addressd.config(font=("Arial", 15, "bold"))
#         #
#         self.address_text = Text(width=40, height=5)
#         self.address_text.grid(column=0, row=10)
#
#         # self.button = Button(self.screen,command=threading.Thread(target=commandd).start)
#
#         self.button = Button(command=commandd)
#         self.button.config(text="Inform To Donors")
#         self.button.place(x=330, y=689)
#         self.button.config(font=("Arial", 20, "bold"), highlightthickness=0)
#
#
#
#         self.image = Image.open("2.jpg")
#         self.resise_image = self.image.resize((270, 400))
#         self.img = ImageTk.PhotoImage(self.resise_image)
#
#         self.image_label = Label(image=self.img)
#         self.image_label.place(x=15, y=150)
#
#         self.image1 = Image.open("2.jpg")
#         self.resise_image1 = self.image.resize((270, 400))
#         self.img1 = ImageTk.PhotoImage(self.resise_image)
#
#         self.image_label1 = Label(image=self.img1)
#         self.image_label1.place(x=660, y=150)
#
#         self.screen_Four.mainloop()


import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from ONE_donersdatabase import finallistofsuitabledoners
from FOUR_status_update_info import Info
from ONE_patientdatabade import Patient_datas
import  threading

class status_update_tkscreen():
    def __init__(self):
        def commandd():
               self.patientid = self.patient_id_entry.get()
               if self.patientid != "Enter If Known" and self.patientid != "" :
                   self.button["state"] = DISABLED
                   self.p=Patient_datas(int(self.patientid))
                   self.patient_name.insert(0,f"{self.p.patientname}")
                   self.blood_group.set(f"{self.p.patientbloodgroup}")
                   self.cities.set(f"{self.p.city}")
                   self.address_text.insert(END,f"{self.p.location}")

                   self.pat_name = self.p.patientname
                   self.pat_blood_group = self.p.patientbloodgroup
                   self.city = self.p.city
                   self.address = self.p.location
                   gg = finallistofsuitabledoners(self.pat_blood_group, self.city)
                   print(gg.donersfinallist)

                   for i in gg.donersfinallist:
                       dddd = Info(self.pat_name, i[3], self.address)
                       dddd.whatsapp()
                       # dddd.text_message()
                   print(self.city, self.pat_name, self.pat_blood_group, self.address)

                   try:
                       answer = messagebox.showinfo("INFO", "Successfully Informed Donors")
                       Label(text=answer, font=('Arial 20 bold')).pack()
                   except:
                       pass




               else:

                   self.pat_name = self.patient_name.get()
                   self.pat_blood_group = self.blood_group.get()
                   self.city = self.cities.get()
                   self.address = self.address_text.get('1.0',END)
                   a=str(self.address).split()


                   if self.pat_name != "" and self.pat_blood_group != "Select The Blood Group" and self.city != "Select The City" and a != []:
                        self.button["state"] = DISABLED
                        gg=finallistofsuitabledoners(self.pat_blood_group,self.city)
                        print(gg.donersfinallist)

                        for i in gg.donersfinallist:
                               dddd=Info(self.pat_name,i[3],self.address)
                               dddd.whatsapp()
                               # dddd.text_message()
                        print(self.city,self.pat_name,self.pat_blood_group,self.address)
                        try:
                            answer = messagebox.showinfo("INFO", "Successfully Informed Donors")
                            Label(text=answer, font=('Arial 20 bold')).pack()
                        except:
                            pass
                   else:
                       try:
                           answer = messagebox.showinfo("INFO", "Please Enter All Fields")
                           Label(text=answer, font=('Arial 20 bold')).pack()
                       except:
                           pass


        self.screen_Four = Tk()
        self.screen_Four.maxsize(950, 950)
        self.screen_Four.minsize(950, 950)
        self.screen_Four.title(string="Auto Contact Blood Don0rs")

        self.info = Label(text="STATUS UPDATE")
        self.info.grid(column=0, row=0)
        self.info.config(font=("Arial", 22, "bold"))
        self.info.config(pady=20, padx=350)

        self.patient_id = Label(text="Patient id")
        self.patient_id.grid(column=0, row=1)
        self.patient_id.config(font=("Arial", 15, "bold"))
        self.patient_id.config(pady=10)


        def click(*args):
            self.patient_id_entry.delete(0, 'end')


        self.patient_id_entry = Entry(self.screen_Four, width=50)

        # Add text in Entry box
        self.patient_id_entry.insert(0, 'Enter If Known')
        self.patient_id_entry.grid(column=0, row=2)

        # Use bind method
        self.patient_id_entry.bind("<Button-1>", click)

        self.donners_name_label = Label(text="Or")
        self.donners_name_label.grid(column=0, row=3)
        self.donners_name_label.config(font=("Arial", 15, "bold"))
        self.donners_name_label.config(pady=10)

        self.donners_name_label = Label(text="Enter the Patient's Name Below :")
        self.donners_name_label.grid(column=0, row=4)
        self.donners_name_label.config(font=("Arial", 15, "bold"))
        self.donners_name_label.config(pady=10)

        self.patient_name = Entry(width=50)
        self.patient_name.grid(column=0, row=5)
        self.patient_name.focus()

        self.donners_blood_group_label = Label(text="Select the Patient's Blood Group:")
        self.donners_blood_group_label.grid(column=0, row=6)
        self.donners_blood_group_label.config(pady=20)
        self.donners_blood_group_label.config(font=("Arial", 15, "bold"))

        self.blood_group = StringVar(self.screen_Four)
        self.blood_group.set("Select The Blood Group")
        self.list_of_blood_group = OptionMenu(self.screen_Four, self.blood_group, "a positive", "a negative", "b positive",
                                              "b negative"
                                              , "ab positive", "ab negative", "o positive", "o negative")
        self.list_of_blood_group.grid(column=0, row=7)
        self.list_of_blood_group.config(height=2, highlightbackground="red", highlightthickness=10)


        self.donners_locatiom = Label(text="Select the Location\City:")
        self.donners_locatiom.grid(column=0, row=8)
        self.donners_locatiom.config(pady=20)
        self.donners_locatiom.config(font=("Arial", 15, "bold"))

        self.cities = StringVar(self.screen_Four)
        self.cities.set("Select The City")
        self.list_of_location = OptionMenu(self.screen_Four, self.cities, "coimbatore", "chennai", "hosur", "madurai",
                                           "karaikudi", "karur",
                                           "trichy", "namkal")
        self.list_of_location.grid(column=0, row=9)
        self.list_of_location.config(height=2, highlightbackground="red", highlightcolor="blue", highlightthickness=10)

        self.addressd = Label(text=f"Enter the Address")
        self.addressd.grid(column=0, row=10)
        self.addressd.config(pady=20)
        self.addressd.config(font=("Arial", 15, "bold"))
        #
        self.address_text = Text(width=40, height=5)
        self.address_text.grid(column=0, row=11)


        # self.button = Button(self.screen_Four,command=threading.Thread(target=commandd).start)
        self.button = Button(command=commandd)
        self.button.config(text="Inform To Donors")
        self.button.place(x=330, y=689)
        self.button.config(font=("Arial", 20, "bold"), highlightthickness=0)



        self.image = Image.open("2.jpg")
        self.resise_image = self.image.resize((270, 400))
        self.img = ImageTk.PhotoImage(self.resise_image)

        self.image_label = Label(image=self.img)
        self.image_label.place(x=15, y=150)

        self.image1 = Image.open("2.jpg")
        self.resise_image1 = self.image.resize((270, 400))
        self.img1 = ImageTk.PhotoImage(self.resise_image)

        self.image_label1 = Label(image=self.img1)
        self.image_label1.place(x=660, y=150)

        self.screen_Four.mainloop()







