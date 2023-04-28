# import time
# from tkinter import *
# from PIL import ImageTk, Image
#
#
# class tkscreen():
#     def __init__(self):
#         def commandd():
#             self.pn=self.patient_name.get()
#             self.pnbg=self.patient_blood_group.get()
#             self.pnamn=self.patient_attender_mobile_number.get()
#             self.location_of_hospital=self.loaction_text.get("1.0",END)
#             # print(f"{self.pn},{self.pnbg},{self.pnamn},{self.location_of_hospital}")
#             time.sleep(3)
#             self.screen.destroy()
#         self.screen = Tk()
#         self.screen.maxsize(950,950)
#         self.screen.minsize(950, 950)
#         self.screen.title(string="Auto Contact Blood Doners")
#
#
#         self.info = Label(text="Welcome to the Auto Contact Blood Donners Application")
#         self.info.grid(column=0, row=0)
#         self.info.config(font=("Arial", 22, "bold"))
#         self.info.config(pady=50,padx=80)
#
#         self.patient_info_name = Label(text="Enter the patient Name Below :")
#         self.patient_info_name.grid(column=0, row=1)
#         self.patient_info_name.config(font=("Arial", 15, "bold"))
#         self.patient_info_name.config(pady=10)
#
#         self.patient_name = Entry(width=50)
#         self.patient_name.grid(column=0, row=2)
#         self.patient_name.focus()
#
#         self.patient_info_blood_group = Label(text="Enter the Patient Blood Group:")
#         self.patient_info_blood_group.grid(column=0, row=3)
#         self.patient_info_blood_group.config(pady=20)
#         self.patient_info_blood_group.config(font=("Arial", 15, "bold"))
#
#         self.patient_blood_group = Entry(width=50)
#         self.patient_blood_group.grid(column=0, row=4)
#
#         self.patient_attender_mobile_number_info = Label(text="Enter the attender Number:")
#         self.patient_attender_mobile_number_info.grid(column=0, row=5)
#         self.patient_attender_mobile_number_info.config(pady=20)
#         self.patient_attender_mobile_number_info.config(font=("Arial", 15, "bold"))
#
#         self.patient_attender_mobile_number = Entry(width=50)
#         self.patient_attender_mobile_number.grid(column=0, row=6)
#
#         self.location = Label(text="Enter the location:")
#         self.location.grid(column=0, row=7)
#         self.location.config(pady=20)
#         self.location.config(font=("Arial", 15, "bold"))
#
#
#         self.loaction_text = Text(height=10, width=40)
#         self.loaction_text.grid(column=0, row=8)
#
#         self.button = Button(command=commandd)
#         self.button.grid(column=0, row=9)
#         self.button.config(text="CONTACT")
#         self.button.place(x=380, y=650)
#         self.button.config(font=("Arial", 20, "bold"), highlightthickness=0)
#
#         self.pn = self.patient_name.get()
#         self.pnbg = self.patient_blood_group.get()
#         self.pnamn = self.patient_attender_mobile_number.get()
#         self.location_of_hospital = self.loaction_text.get("1.0", END)
#
#         self.image=Image.open("2.jpg")
#         self.resise_image = self.image.resize((270, 400))
#         self.img = ImageTk.PhotoImage(self.resise_image)
#
#         self.image_label = Label(image=self.img)
#         self.image_label.place(x=15,y=150)
#
#         self.image1 = Image.open("2.jpg")
#         self.resise_image1 = self.image.resize((270, 400))
#         self.img1 = ImageTk.PhotoImage(self.resise_image)
#
#         self.image_label1 = Label(image=self.img1)
#         self.image_label1.place(x=660, y=150)
#
#         # self.image1=Image.open("6.png")
#         # self.resise_image1 = self.image1.resize((280,480))
#         # self.img1 = ImageTk.PhotoImage(self.resise_image1)
#         #
#         # self.image_label1 = Label(image=self.img1)
#         # self.image_label1.place(x=660,y=180)
#
#         self.screen.mainloop()
##########################################################################################################################

# import time
# from tkinter import *
# from PIL import ImageTk, Image
#
#
# class tkscreen():
#     def __init__(self):
#         self.known=None
#         def commandd():
#             self.pn=self.patient_name.get()
#             self.pnbg = self.list.get(self.list.curselection())
#             self.known=self.pnbg
#             self.pnamn=self.patient_attender_mobile_number.get()
#             self.location_of_hospital=self.loaction_text.get("1.0",END)
#             # print(f"{self.pn},{self.pnbg},{self.pnamn},{self.location_of_hospital}{self.known}")
#             time.sleep(3)
#             self.screen.destroy()
#         self.screen = Tk()
#         self.screen.maxsize(950,950)
#         self.screen.minsize(950, 950)
#         self.screen.title(string="Auto Contact Blood Doners")
#
#
#         self.info = Label(text="Welcome to the Auto Contact Blood Donners Application")
#         self.info.grid(column=0, row=0)
#         self.info.config(font=("Arial", 22, "bold"))
#         self.info.config(pady=20,padx=80)
#
#         self.patient_info_name = Label(text="Enter the patient Name Below :")
#         self.patient_info_name.grid(column=0, row=1)
#         self.patient_info_name.config(font=("Arial", 15, "bold"))
#         self.patient_info_name.config(pady=10)
#
#         self.patient_name = Entry(width=50)
#         self.patient_name.grid(column=0, row=2)
#         self.patient_name.focus()
#
#         self.patient_info_blood_group = Label(text="Select the Patient Blood Group:")
#         self.patient_info_blood_group.grid(column=0, row=3)
#         self.patient_info_blood_group.config(pady=20)
#         self.patient_info_blood_group.config(font=("Arial", 15, "bold"))
#
#         self.list = Listbox(height=8, width=50)
#         self.course = ["o positive", "o negative", "b positive", "b negative", "a positive", "a negative",
#                        "ab positive", "ab negative"]
#         self.D = [self.list.insert(self.course.index(i), i) for i in self.course]
#         self.list.grid(column=0, row=4)
#
#         self.patient_attender_mobile_number_info = Label(text="Enter the attender Number:")
#         self.patient_attender_mobile_number_info.grid(column=0, row=5)
#         self.patient_attender_mobile_number_info.config(pady=20)
#         self.patient_attender_mobile_number_info.config(font=("Arial", 15, "bold"))
#
#         self.patient_attender_mobile_number = Entry(width=50)
#         self.patient_attender_mobile_number.grid(column=0, row=6)
#
#         self.location = Label(text="Enter the location:")
#         self.location.grid(column=0, row=7)
#         self.location.config(pady=20)
#         self.location.config(font=("Arial", 15, "bold"))
#
#
#         self.loaction_text = Text(height=10, width=40)
#         self.loaction_text.grid(column=0, row=8)
#
#
#
#
#         self.button = Button(command=commandd)
#         self.button.grid(column=0, row=11)
#         self.button.config(text="CONTACT")
#         self.button.place(x=380, y=690)
#         self.button.config(font=("Arial", 20, "bold"), highlightthickness=0)
#
#
#
#         self.pn = self.patient_name.get()
#
#         self.pnamn = self.patient_attender_mobile_number.get()
#         self.location_of_hospital = self.loaction_text.get("1.0", END)
#
#         self.image=Image.open("2.jpg")
#         self.resise_image = self.image.resize((270, 400))
#         self.img = ImageTk.PhotoImage(self.resise_image)
#
#         self.image_label = Label(image=self.img)
#         self.image_label.place(x=15,y=150)
#
#         self.image1 = Image.open("2.jpg")
#         self.resise_image1 = self.image.resize((270, 400))
#         self.img1 = ImageTk.PhotoImage(self.resise_image)
#
#         self.image_label1 = Label(image=self.img1)
#         self.image_label1.place(x=660, y=150)
#
#         self.screen.mainloop()
#
######################################################################################################################
#
#
# from tkinter import *
# from PIL import ImageTk, Image
# from ONE_location import Location_finder
# from tkinter import messagebox
# import threading
# from ONE_patient_info import patient
# from ONE_donersdatabase import finallistofsuitabledoners
# from ONE_info import Info
# import time
# from ONE_patientdatabade import patient_details_database
# from itertools import count, cycle
#
#
# class ImageLabel(Label):
#     def load(self, im):
#         if isinstance(im, str):
#             im = Image.open(im)
#         frames = []
#
#         try:
#             for i in count(1):
#                 frames.append(ImageTk.PhotoImage(im.copy()))
#                 im.seek(i)
#         except EOFError:
#             pass
#         self.frames = cycle(frames)
#
#         try:
#             self.delay = im.info['duration']
#         except:
#             self.delay = 100
#
#         if len(frames) == 1:
#             self.config(image=next(self.frames))
#         else:
#             self.next_frame()
#
#     def unload(self):
#         self.config(image=None)
#         self.frames = None
#
#     def next_frame(self):
#         if self.frames:
#             self.config(image=next(self.frames))
#             self.after(self.delay, self.next_frame)
#
# class Finding_blood_tkscreen():
#     def __init__(self):
#         # self.ki = None
#         self.known = None
#         self.loco = None
#         self.pnn = None
#         self.pnamnn = None
#         self.location1 = None
#         self.city1 = None
#
#         def commandd():
#
#             self.button["state"] = DISABLED
#             self.pn = self.patient_name.get()
#             self.pnn = self.pn
#             self.pnbg = self.blood_group.get()
#             self.known = self.pnbg
#             self.pnamn = self.patient_attender_mobile_number.get()
#             self.pnamnn = self.pnamn
#             self.location_of_hospital = self.loaction_text.get("1.0", 'end-1c')
#             self.location1 = self.location_of_hospital
#             self.city_finder = self.cities.get()
#             self.loco = self.city_finder
#
#             self.info.destroy()
#             self.patient_info_name.destroy()
#             self.patient_name.destroy()
#             self.patient_info_blood_group.destroy()
#             self.list_of_blood_group.destroy()
#             self.patient_attender_mobile_number_info.destroy()
#             self.patient_attender_mobile_number.destroy()
#             self.blood_needed_location.destroy()
#             self.list_of_location.destroy()
#             self.location.destroy()
#             self.loaction_text.destroy()
#             self.button.destroy()
#             self.image_label.destroy()
#             self.image_label1.destroy()
#             self.image_label2.destroy()
#
#             # self.info.grid_remove()
#             # self.patient_info_name.grid_remove()
#             # self.patient_name.grid_remove()
#             # self.patient_info_blood_group.grid_remove()
#             # self.list_of_blood_group.grid_remove()
#             # self.patient_attender_mobile_number_info.grid_remove()
#             # self.patient_attender_mobile_number.grid_remove()
#             # self.blood_needed_location.grid_remove()
#             # self.list_of_location.grid_remove()
#             # self.location.grid_remove()
#             # self.loaction_text.grid_remove()
#             # self.button.destroy()
#             # self.image_label.destroy()
#             # self.image_label1.destroy()
#             # self.image_label2.destroy()
#
#
#
#             self.d = finallistofsuitabledoners(self.known, self.loco)
#
#             if self.d.donersfinallist == []:
#
#                 self.image = Image.open("0.png")
#                 self.resise_image = self.image.resize((750, 550))
#                 self.img = ImageTk.PhotoImage(self.resise_image)
#
#                 self.image_label = Label(image=self.img)
#                 self.image_label.place(x=120, y=200)
#                 self.one = Label(text="Sorry No respective Donners Found")
#                 self.one.config(font=("Arial", 22, "bold"))
#                 self.one.place(x=200, y=111)
#                 exit()
#                 self.screen.destroy()
#
#             else:
#                 lbl = ImageLabel(self.screen)
#                 lbl.place(x=310, y=270)
#                 lbl.load("q.gif")
#                 lbl.next_frame()
#
#                 self.ki = Location_finder(self.location1)
#                 self.venkat = patient(self.pnn, self.known, self.location1)
#                 try:
#                     self.venkatesan = Info(self.ki.exact_location_text, self.ki.link, self.pnn, self.known, self.pnamnn
#                                            , self.ki.address)
#
#                 except:
#                     Label(text="Sorry For The Inconvenience", font=('Arial 28 italic')).place(x=260, y=100)
#                     answer = messagebox.showinfo("INFO",
#                                                  f"\tError Occured \n\nCheck Your Internet Connectivity\n\nClose and Try Again")
#                     exit()
#                     self.screen.destroy()
#
#                 print(self.d.donersfinallist)
#
#                 for i in self.d.donersfinallist:
#                     self.venkatesan.whatsapp(i[3],i[0],i[1])
#                     self.venkatesan.caller(i[3])
#                     self.venkatesan.text_message(i[3],i[0],i[1])
#                     # time.sleep(1)
#                 if self.d.donersfinallist != []:
#                     patient_details_database(self.pnn, self.known, self.venkat.today, self.location1, self.pnamnn)
#
#                 # searching.destroy()
#                 # if self.d.donersfinallist != []:
#                 lbl.unload()
#                 self.image = Image.open("0.png")
#                 self.resise_image = self.image.resize((750, 550))
#                 self.img = ImageTk.PhotoImage(self.resise_image)
#
#                 self.image_label = Label(image=self.img)
#                 self.image_label.place(x=120, y=200)
#                 self.one = Label(text="Successfully Messages are send to the respected donners")
#                 self.one.config(font=("Arial", 22, "bold"))
#                 self.one.place(x=60, y=111)
#                 answer = messagebox.showinfo("INFO",
#                                              f"Call, WhatsApp, TextMessage\n\t Sended to {len(self.d.donersfinallist)} Donners")
#                 # else:
#                 #
#                 #     self.image = Image.open("0.png")
#                 #     self.resise_image = self.image.resize((750, 550))
#                 #     self.img = ImageTk.PhotoImage(self.resise_image)
#                 #
#                 #     self.image_label = Label(image=self.img)
#                 #     self.image_label.place(x=120, y=200)
#                 #     self.one = Label(text="Sorry No respective Donners Found")
#                 #     self.one.config(font=("Arial", 22, "bold"))
#                 #     self.one.place(x=200, y=111)
#                 exit()
#                 self.screen.destroy()
#
#         self.screen = Tk()
#         self.screen.maxsize(950, 950)
#         self.screen.minsize(950, 950)
#         self.screen.title(string="Auto Contact Blood Doners")
#
#         self.info = Label(text="Welcome to the Auto Contact Blood Donners Application")
#         self.info.grid(column=0, row=0)
#         self.info.config(font=("Arial", 22, "bold"))
#         self.info.config(pady=20, padx=80)
#
#         self.patient_info_name = Label(text="Enter the patient Name Below *")
#         self.patient_info_name.grid(column=0, row=1)
#         self.patient_info_name.config(font=("Arial", 15, "bold"))
#         self.patient_info_name.config(pady=10)
#
#         self.patient_name = Entry(width=50)
#         self.patient_name.grid(column=0, row=2)
#         self.patient_name.focus()
#
#         self.patient_info_blood_group = Label(text="Select the Patient Blood Group *")
#         self.patient_info_blood_group.grid(column=0, row=3)
#         self.patient_info_blood_group.config(pady=20)
#         self.patient_info_blood_group.config(font=("Arial", 15, "bold"))
#
#         self.blood_group = StringVar(self.screen)
#         self.blood_group.set("Select The Blood Group")
#         self.list_of_blood_group = OptionMenu(self.screen, self.blood_group, "a positive", "a negative", "b positive",
#                                               "b negative"
#                                               , "ab positive", "ab negative", "o positive", "o negative")
#         self.list_of_blood_group.grid(column=0, row=4)
#         self.list_of_blood_group.config(height=2, highlightbackground="red", highlightthickness=10)
#
#         self.patient_attender_mobile_number_info = Label(text="Enter the attender Number *")
#         self.patient_attender_mobile_number_info.grid(column=0, row=5)
#         self.patient_attender_mobile_number_info.config(pady=20)
#         self.patient_attender_mobile_number_info.config(font=("Arial", 15, "bold"))
#
#         self.patient_attender_mobile_number = Entry(width=50)
#         self.patient_attender_mobile_number.grid(column=0, row=6)
#
#         self.blood_needed_location = Label(text="Select the Location\City *")
#         self.blood_needed_location.grid(column=0, row=7)
#         self.blood_needed_location.config(pady=20)
#         self.blood_needed_location.config(font=("Arial", 15, "bold"))
#
#         self.cities = StringVar(self.screen)
#         self.cities.set("Select The City")
#         self.list_of_location = OptionMenu(self.screen, self.cities, "coimbatore", "chennai", "hosur", "madurai",
#                                            "karaikudi", "karur",
#                                            "trichy", "namakal")
#         self.list_of_location.grid(column=0, row=8)
#         self.list_of_location.config(height=2, highlightbackground="red", highlightthickness=10)
#
#         self.location = Label(text="Enter the Address *")
#         self.location.grid(column=0, row=9)
#         self.location.config(pady=20)
#         self.location.config(font=("Arial", 15, "bold"))
#
#         self.loaction_text = Text(height=5, width=40)
#         self.loaction_text.grid(column=0, row=10)
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
#         self.image2 = Image.open("1.png")
#         self.resise_image2 = self.image2.resize((70, 80))
#         self.img2 = ImageTk.PhotoImage(self.resise_image2)
#
#         self.image_label2 = Label(image=self.img2)
#         self.image_label2.place(x=300, y=415)
#         self.button = Button(self.screen, command=threading.Thread(target=commandd).start)
#         # self.button = Button(command=commandd)
#
#         # self.button.grid(column=0, row=11)
#         self.button.config(text="CONTACT")
#         self.button.place(x=400, y=689)
#         self.button.config(font=("Arial", 20, "bold"), highlightthickness=0)
#
#         self.screen.mainloop()
#################################################################################################################################


from tkinter import *
from PIL import ImageTk, Image
from ONE_location import Location_finder
from tkinter import messagebox
import threading
from ONE_patient_info import patient
from ONE_donersdatabase import finallistofsuitabledoners
from ONE_info import Info
import time
from ONE_patientdatabade import patient_details_database ,Patient_datas
from itertools import count, cycle
from  ONE_patient_attender_info import patient_attender_info
import mysql.connector



class ImageLabel(Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


class Finding_blood_tkscreen():
    def __init__(self):
        # self.ki = None
        self.known = None
        self.loco = None
        self.pnn = None
        self.pnamnn = None
        self.location1 = None
        self.city1 = None
        self.patient_idd = None

        def commandd():

            self.button["state"] = DISABLED
            self.patient_idd = self.patient_id_entry.get()
            # print(self.patient_idd)
            # print(type(self.patient_idd))
            if self.patient_idd != "Use only if Error occurred " and self.patient_idd != "":
                pdata = Patient_datas(int(self.patient_idd))
                self.pnn = pdata.patientname
                self.known = pdata.patientbloodgroup
                self.pnamnn = pdata.attendernumber
                self.location1 = pdata.location
                self.loco = pdata.city


            else:
                self.pn = self.patient_name.get()
                self.pnn = self.pn
                self.pnbg = self.blood_group.get()
                self.known = self.pnbg
                self.pnamn = self.patient_attender_mobile_number.get()
                self.pnamnn = self.pnamn
                self.location_of_hospital = self.loaction_text.get("1.0", 'end-1c')
                self.location1 = self.location_of_hospital
                self.city_finder = self.cities.get()
                self.loco = self.city_finder




            self.info.destroy()
            self.patient_id.destroy()
            self.patient_id_entry.destroy()
            self.patient_info_name.destroy()
            self.patient_name.destroy()
            self.patient_info_blood_group.destroy()
            self.list_of_blood_group.destroy()
            self.patient_attender_mobile_number_info.destroy()
            self.patient_attender_mobile_number.destroy()
            self.blood_needed_location.destroy()
            self.list_of_location.destroy()
            self.location.destroy()
            self.loaction_text.destroy()
            self.button.destroy()
            self.image_label.destroy()
            self.image_label1.destroy()
            self.image_label2.destroy()



            # self.info.grid_remove()
            # self.patient_info_name.grid_remove()
            # self.patient_name.grid_remove()
            # self.patient_info_blood_group.grid_remove()
            # self.list_of_blood_group.grid_remove()
            # self.patient_attender_mobile_number_info.grid_remove()
            # self.patient_attender_mobile_number.grid_remove()
            # self.blood_needed_location.grid_remove()
            # self.list_of_location.grid_remove()
            # self.location.grid_remove()
            # self.loaction_text.grid_remove()
            # self.button.destroy()
            # self.image_label.destroy()
            # self.image_label1.destroy()
            # self.image_label2.destroy()

            # print(self.patient_idd)

            self.d = finallistofsuitabledoners(self.known, self.loco)

            if self.d.donersfinallist == []:

                self.image = Image.open("0.png")
                self.resise_image = self.image.resize((750, 550))
                self.img = ImageTk.PhotoImage(self.resise_image)

                self.image_label = Label(image=self.img)
                self.image_label.place(x=120, y=200)
                self.one = Label(text="Sorry No respective Donners Found")
                self.one.config(font=("Arial", 22, "bold"))
                self.one.place(x=200, y=111)
                exit()
                self.screen.destroy()

            else:



                lbl = ImageLabel(self.screen)
                lbl.place(x=310,y=270)
                # lbl.load("q.gif")
                lbl.load("h.gif")
                lbl.next_frame()
                # lbl.next_frame()
                # print(self.patient_idd)

                if self.patient_idd == "Use only if Error occurred " or self.patient_idd == "":

                    conn = mysql.connector.connect(
                        user='root', password='VENKAT21o22oo2@', host='localhost', database='patient_list')
                    cursor = conn.cursor()
                    sql = '''SELECT count(*) from patient_details'''
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    aa = result[0]
                    # print(aa)
                    conn.close()
                    self.venkat = patient(self.pnn, self.known, self.location1)
                    patient_details_database(aa+1,self.pnn,self.known,self.venkat.today,self.location1,self.pnamnn,self.loco)

                    attenderinfo = patient_attender_info(aa+1,self.pnn, self.known, self.location1, self.loco, self.pnamnn)
                    attenderinfo.whatsapp()
                    attenderinfo.text_message()


                self.ki = Location_finder(self.location1)

                try:
                    self.venkatesan = Info(self.ki.exact_location_text, self.ki.link, self.pnn, self.known, self.pnamnn
                                           , self.ki.address)

                except:
                    Label(text="Sorry For The Inconvenience", font=('Arial 28 italic')).place(x=260, y=100)
                    answer = messagebox.showinfo("INFO",
                                                 f"\tError Occured \n\nCheck Your Internet Connectivity\n\nClose and Try Again")
                    exit()
                    self.screen.destroy()

                print(self.d.donersfinallist)
                for i in self.d.donersfinallist:
                    self.venkatesan.whatsapp(i[3], i[0], i[1])
                    self.venkatesan.caller(i[3])
                    self.venkatesan.text_message(i[3],i[0],i[1])
                    # time.sleep(1)




                # searching.destroy()
                # if self.d.donersfinallist != []:
                lbl.unload()
                self.image = Image.open("0.png")
                self.resise_image = self.image.resize((750, 550))
                self.img = ImageTk.PhotoImage(self.resise_image)

                self.image_label = Label(image=self.img)
                self.image_label.place(x=120, y=200)
                self.one = Label(text="Successfully Messages are send to the respected donners")
                self.one.config(font=("Arial", 22, "bold"))
                self.one.place(x=60, y=111)
                answer = messagebox.showinfo("INFO",
                                    f"Call, WhatsApp, TextMessage\n\t Send to {len(self.d.donersfinallist)} Donor")

                # else:
                #
                #     self.image = Image.open("0.png")
                #     self.resise_image = self.image.resize((750, 550))
                #     self.img = ImageTk.PhotoImage(self.resise_image)
                #
                #     self.image_label = Label(image=self.img)
                #     self.image_label.place(x=120, y=200)
                #     self.one = Label(text="Sorry No respective Donners Found")
                #     self.one.config(font=("Arial", 22, "bold"))
                #     self.one.place(x=200, y=111)
                exit()
                self.screen.destroy()

        self.screen = Tk()
        self.screen.maxsize(950, 950)
        self.screen.minsize(950, 950)
        self.screen.title(string="Auto Contact Blood Donors")

        self.info = Label(text="Welcome to the Auto Contact Blood Donors Application")
        self.info.grid(column=0, row=0)
        self.info.config(font=("Arial", 22, "bold"))
        self.info.config(pady=10, padx=80)

        self.patient_id = Label(text="Patient id")
        self.patient_id.grid(column=0, row=1)
        self.patient_id.config(font=("Arial", 15, "bold"))
        self.patient_id.config(pady=10)

        #
        #
        # self.patient_id_entry = Entry(width=50)
        # self.patient_id_entry.insert(0,"Use for Retry")
        # self.patient_id_entry.grid(column=0, row=2)
        # self.patient_id_entry.focus()

        def click(*args):
            self.patient_id_entry.delete(0, 'end')

        # call function when we leave entry box
        # def leave(*args):
        #     patient_id_entry.delete(0, 'end')
        #     # patient_id_entry.insert(0, 'Use only if Error occurred  ')

            # self.screen.focus()

        # Add Entry Box
        self.patient_id_entry = Entry(self.screen, width=50)

        # Add text in Entry box
        self.patient_id_entry.insert(0, 'Use only if Error occurred ')
        self.patient_id_entry.grid(column=0,row=2)

        # Use bind method
        self.patient_id_entry.bind("<Button-1>", click)
        # patient_id_entry.bind("<Leave>", leave)

        self.patient_info_name = Label(text="Enter the patient Name Below *")
        self.patient_info_name.grid(column=0, row=3)
        self.patient_info_name.config(font=("Arial", 15, "bold"))
        self.patient_info_name.config(pady=10)

        self.patient_name = Entry(width=50)
        self.patient_name.grid(column=0, row=4)
        self.patient_name.focus()

        self.patient_info_blood_group = Label(text="Select the Patient Blood Group*")
        self.patient_info_blood_group.grid(column=0, row=5)
        self.patient_info_blood_group.config(pady=20)
        self.patient_info_blood_group.config(font=("Arial", 15, "bold"))

        self.blood_group = StringVar(self.screen)
        self.blood_group.set("Select The Blood Group*")
        self.list_of_blood_group = OptionMenu(self.screen, self.blood_group, "a positive", "a negative", "b positive",
                                              "b negative"
                                              , "ab positive", "ab negative", "o positive", "o negative")
        self.list_of_blood_group.grid(column=0, row=6)
        self.list_of_blood_group.config(height=2, highlightbackground="red", highlightthickness=10)

        self.patient_attender_mobile_number_info = Label(text="Enter the attender Number*")
        self.patient_attender_mobile_number_info.grid(column=0, row=7)
        self.patient_attender_mobile_number_info.config(pady=20)
        self.patient_attender_mobile_number_info.config(font=("Arial", 15, "bold"))

        self.patient_attender_mobile_number = Entry(width=50)
        self.patient_attender_mobile_number.grid(column=0, row=8)

        self.blood_needed_location = Label(text="Select the Location\City*")
        self.blood_needed_location.grid(column=0, row=9)
        self.blood_needed_location.config(pady=20)
        self.blood_needed_location.config(font=("Arial", 15, "bold"))

        self.cities = StringVar(self.screen)
        self.cities.set("Select The City*")
        self.list_of_location = OptionMenu(self.screen, self.cities, "coimbatore", "chennai", "hosur", "madurai",
                                           "karaikudi", "karur",
                                           "trichy", "namakal")
        self.list_of_location.grid(column=0, row=10)
        self.list_of_location.config(height=2, highlightbackground="red", highlightthickness=10)

        self.location = Label(text="Enter the Address*")
        self.location.grid(column=0, row=11)
        self.location.config(pady=20)
        self.location.config(font=("Arial", 15, "bold"))

        self.loaction_text = Text(height=5, width=40)
        self.loaction_text.grid(column=0, row=12)

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

        self.image2 = Image.open("1.png")
        self.resise_image2 = self.image2.resize((70, 80))
        self.img2 = ImageTk.PhotoImage(self.resise_image2)

        self.image_label2 = Label(image=self.img2)
        self.image_label2.place(x=300, y=460)
        self.button = Button(self.screen, command=threading.Thread(target=commandd).start)
        # self.button = Button(command=commandd)

        # self.button.grid(column=0, row=11)
        self.button.config(text="CONTACT")
        self.button.place(x=400, y=710)
        self.button.config(font=("Arial", 20, "bold"), highlightthickness=0)

        self.screen.mainloop()
