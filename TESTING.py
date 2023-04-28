# # import time
# # from tkinter import *
# # from PIL import ImageTk, Image
# # from tkinter import messagebox
# # from ONE_donersdatabase import finallistofsuitabledoners
# # from FOUR_status_update_info import Info
# # from ONE_patientdatabade import Patient_datas
# # import  threading
# #
# # class status_update_tkscreen():
# #     def __init__(self):
# #         def commandd():
# #                self.patientid = self.patient_id_entry.get()
# #                if self.patientid != "Enter If Known" and self.patientid != "" :
# #                    self.button["state"] = DISABLED
# #                    self.p=Patient_datas(int(self.patientid))
# #                    self.patient_name.insert(0,f"{self.p.patientname}")
# #                    self.blood_group.set(f"{self.p.patientbloodgroup}")
# #                    self.cities.set(f"{self.p.city}")
# #                    self.address_text.insert(END,f"{self.p.location}")
# #
# #                    self.pat_name = self.p.patientname
# #                    self.pat_blood_group = self.p.patientbloodgroup
# #                    self.city = self.p.city
# #                    self.address = self.p.location
# #                    gg = finallistofsuitabledoners(self.pat_blood_group, self.city)
# #                    print(gg.donersfinallist)
# #
# #                    for i in gg.donersfinallist:
# #                        dddd = Info(self.pat_name, i[3], self.address)
# #                        dddd.whatsapp()
# #                        # dddd.text_message()
# #                    print(self.city, self.pat_name, self.pat_blood_group, self.address)
# #
# #                    try:
# #                        answer = messagebox.showinfo("INFO", "Successfully Informed Donors")
# #                        Label(text=answer, font=('Arial 20 bold')).pack()
# #                    except:
# #                        pass
# #
# #
# #
# #
# #                else:
# #
# #                    self.pat_name = self.patient_name.get()
# #                    self.pat_blood_group = self.blood_group.get()
# #                    self.city = self.cities.get()
# #                    self.address = self.address_text.get('1.0',END)
# #                    a=str(self.address).split()
# #
# #
# #                    if self.pat_name != "" and self.pat_blood_group != "Select The Blood Group" and self.city != "Select The City" and a != []:
# #                         self.button["state"] = DISABLED
# #                         gg=finallistofsuitabledoners(self.pat_blood_group,self.city)
# #                         print(gg.donersfinallist)
# #
# #                         for i in gg.donersfinallist:
# #                                dddd=Info(self.pat_name,i[3],self.address)
# #                                dddd.whatsapp()
# #                                # dddd.text_message()
# #                         print(self.city,self.pat_name,self.pat_blood_group,self.address)
# #                         try:
# #                             answer = messagebox.showinfo("INFO", "Successfully Informed Donors")
# #                             Label(text=answer, font=('Arial 20 bold')).pack()
# #                         except:
# #                             pass
# #                    else:
# #                        try:
# #                            answer = messagebox.showinfo("INFO", "Please Enter All Fields")
# #                            Label(text=answer, font=('Arial 20 bold')).pack()
# #                        except:
# #                            pass
# #
# #
# #         self.screen_Four = Tk()
# #         self.screen_Four.maxsize(950, 950)
# #         self.screen_Four.minsize(950, 950)
# #         self.screen_Four.title(string="Auto Contact Blood Don0rs")
# #
# #         self.info = Label(text="STATUS UPDATE")
# #         self.info.grid(column=0, row=0)
# #         self.info.config(font=("Arial", 22, "bold"))
# #         self.info.config(pady=20, padx=350)
# #
# #         self.patient_id = Label(text="Patient id")
# #         self.patient_id.grid(column=0, row=1)
# #         self.patient_id.config(font=("Arial", 15, "bold"))
# #         self.patient_id.config(pady=10)
# #
# #
# #         def click(*args):
# #             self.patient_id_entry.delete(0, 'end')
# #
# #
# #         self.patient_id_entry = Entry(self.screen_Four, width=50)
# #
# #         # Add text in Entry box
# #         self.patient_id_entry.insert(0, 'Enter If Known')
# #         self.patient_id_entry.grid(column=0, row=2)
# #
# #         # Use bind method
# #         self.patient_id_entry.bind("<Button-1>", click)
# #
# #         self.donners_name_label = Label(text="Or")
# #         self.donners_name_label.grid(column=0, row=3)
# #         self.donners_name_label.config(font=("Arial", 15, "bold"))
# #         self.donners_name_label.config(pady=10)
# #
# #         self.donners_name_label = Label(text="Enter the Patient's Name Below :")
# #         self.donners_name_label.grid(column=0, row=4)
# #         self.donners_name_label.config(font=("Arial", 15, "bold"))
# #         self.donners_name_label.config(pady=10)
# #
# #         self.patient_name = Entry(width=50)
# #         self.patient_name.grid(column=0, row=5)
# #         self.patient_name.focus()
# #
# #         self.donners_blood_group_label = Label(text="Select the Patient's Blood Group:")
# #         self.donners_blood_group_label.grid(column=0, row=6)
# #         self.donners_blood_group_label.config(pady=20)
# #         self.donners_blood_group_label.config(font=("Arial", 15, "bold"))
# #
# #         self.blood_group = StringVar(self.screen_Four)
# #         self.blood_group.set("Select The Blood Group")
# #         self.list_of_blood_group = OptionMenu(self.screen_Four, self.blood_group, "a positive", "a negative", "b positive",
# #                                               "b negative"
# #                                               , "ab positive", "ab negative", "o positive", "o negative")
# #         self.list_of_blood_group.grid(column=0, row=7)
# #         self.list_of_blood_group.config(height=2, highlightbackground="red", highlightthickness=10)
# #
# #
# #         self.donners_locatiom = Label(text="Select the Location\City:")
# #         self.donners_locatiom.grid(column=0, row=8)
# #         self.donners_locatiom.config(pady=20)
# #         self.donners_locatiom.config(font=("Arial", 15, "bold"))
# #
# #         self.cities = StringVar(self.screen_Four)
# #         self.cities.set("Select The City")
# #         self.list_of_location = OptionMenu(self.screen_Four, self.cities, "coimbatore", "chennai", "hosur", "madurai",
# #                                            "karaikudi", "karur",
# #                                            "trichy", "namkal")
# #         self.list_of_location.grid(column=0, row=9)
# #         self.list_of_location.config(height=2, highlightbackground="red", highlightcolor="blue", highlightthickness=10)
# #
# #         self.addressd = Label(text=f"Enter the Address")
# #         self.addressd.grid(column=0, row=10)
# #         self.addressd.config(pady=20)
# #         self.addressd.config(font=("Arial", 15, "bold"))
# #         #
# #         self.address_text = Text(width=40, height=5)
# #         self.address_text.grid(column=0, row=11)
# #
# #
# #         # self.button = Button(self.screen_Four,command=threading.Thread(target=commandd).start)
# #         self.button = Button(command=commandd)
# #         self.button.config(text="Inform To Donors")
# #         self.button.place(x=330, y=689)
# #         self.button.config(font=("Arial", 20, "bold"), highlightthickness=0)
# #
# #
# #
# #         self.image = Image.open("2.jpg")
# #         self.resise_image = self.image.resize((270, 400))
# #         self.img = ImageTk.PhotoImage(self.resise_image)
# #
# #         self.image_label = Label(image=self.img)
# #         self.image_label.place(x=15, y=150)
# #
# #         self.image1 = Image.open("2.jpg")
# #         self.resise_image1 = self.image.resize((270, 400))
# #         self.img1 = ImageTk.PhotoImage(self.resise_image)
# #
# #         self.image_label1 = Label(image=self.img1)
# #         self.image_label1.place(x=660, y=150)
# #
# #         self.screen_Four.mainloop()
# #
# #
# #
# # # status_update_tkscreen()
#
#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from  tkinter import  messagebox
# from tkinter import *
# class Location_finder:
#     def __init__(self,address):
#         self.option = webdriver.ChromeOptions()
#         self.option.headless = True
#         # self.chrome = "C:\\chromedriver_win32\\chromedriver"
#         self.chrome = "C:\\Users\\venkatesan\\Downloads\\chromedriver_win32\\chromedriver"
#         # self.driver= webdriver.Chrome(executable_path=self.chrome,chrome_options=self.option)
#         self.driver= webdriver.Chrome(executable_path=self.chrome)
#
#         self.address = address
#         list_of_address=str(address).split("\n")
#         self.a=(",".join(list_of_address))
#         print(self.a)
#
#         try:
#
#             self.driver.get("https://www.google.com/maps/@10.9358408,76.952783,15z")
#             self.search=self.driver.find_element(By.XPATH,'//*[@id="searchboxinput"]')
#             self.search.send_keys(self.a)
#             time.sleep(2)
#             self.click=self.driver.find_element(By.XPATH,'//*[@id="searchbox-searchbutton"]')
#             self.click.click()
#             time.sleep(20)
#             self.share=self.driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[5]/button/div[1]')
#             self.share.click()
#             time.sleep(20)
#             self.exact_location=self.driver.find_element(By.XPATH,'//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div[1]/div[3]/div[2]')
#             self.exact_location_text=self.exact_location.text
#             self.link=self.driver.find_element(By.CLASS_NAME,'vrsrZe').get_attribute("value")
#             self.driver.quit()
#             # print(f"{self.exact_location_text}\n{self.link}")
#
#
#         except:
#             # try:
#             #     answer = messagebox.showinfo("INFO", "Error Ocured Try Again")
#             #     Label(text=answer, font=('Arial 20 bold'))
#             # except:
#             #     pass
#
#             self.driver.quit()
#
#
#

#
# from  account_details import account_detailss
# d=account_detailss()
# print(d.account_token)
# from account_details import  account_detailss
# a=account_detailss()
# print(a.__dir__())

# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Add image file
bg = PhotoImage(file = "C:\\Users\\venkatesan\\Desktop\\New folder\\India's population is 1,415,162,794 (1).png")

# Create Canvas
canvas1 = Canvas( root, width = 200,
				height = 100)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image(1,0, image = bg,
					anchor = "nw")

# Execute tkinter
root.mainloop()
