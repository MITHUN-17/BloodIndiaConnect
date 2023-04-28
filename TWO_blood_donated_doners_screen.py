import time
from tkinter import *
from PIL import ImageTk, Image
from TWO_blood_donated_donners_database import heartful
import threading
from tkinter import messagebox

from TWO_thanking_doners_info import Info


class updating_the_date_of_blood_given_donners_tkscreen():
    def __init__(self):

        def clear():
            self.button['state'] = NORMAL
            self.donners_serial_number.delete(0,END)
            self.donner_blood_given_date.delete(0,END)

        def commandd():
            self.serial_number = self.donners_serial_number.get()
            self.date_of_donation = self.donner_blood_given_date.get()
            if self.serial_number != "" and self.date_of_donation != "":
                self.button['state'] = DISABLED
                v = heartful(self.date_of_donation, self.serial_number)
                print(v.serial_number, v.name, v.mobile_number)
                g = Info(v.name, self.date_of_donation, v.mobile_number, )
                g.whatsapp()
                try:
                    answer = messagebox.showinfo("INFO", f"Thank You {v.name}")

                    Label(text=answer, font=('Arial 20 bold')).pack()
                except:
                    pass
            else:
                try:
                    answer = messagebox.showinfo("INFO" , "Please Enter All Fields")

                    Label(text=answer, font=('Arial 20 bold')).pack()
                except:
                    pass
            # time.sleep(3)
            # exit()
            # self.screen.destroy()

        self.screen = Tk()
        self.screen.maxsize(950,950)
        self.screen.minsize(950, 950)
        self.screen.title(string="Auto Contact Blood Donor's Update Window")


        self.info = Label(text="Welcome Donors ")
        self.info.grid(column=0, row=0)
        self.info.config(font=("Arial", 22, "bold"))
        self.info.config(pady=80,padx=340)

        self.doners_info = Label(text="Enter the Donors Serial Number :")
        self.doners_info.grid(column=0, row=1)
        self.doners_info.config(font=("Arial", 15, "bold"))
        self.doners_info.config(pady=10)

        self.donners_serial_number = Entry(width=50)
        self.donners_serial_number.grid(column=0, row=2)
        self.donners_serial_number.focus()



        self.dateinfo = Label(text="Enter the date of blood Donation \n year-month-date\n(2015-7-27)")
        self.dateinfo.grid(column=0, row=5)
        self.dateinfo.config(pady=20)
        self.dateinfo.config(font=("Arial", 15, "bold"))

        self.donner_blood_given_date = Entry(width=50)
        self.donner_blood_given_date.grid(column=0, row=6)

        # self.button = Button(self.screen, command=threading.Thread(target=commandd).start)
        self.button = Button(command=commandd)
        self.button.grid(column=0, row=11)
        self.button.config(text="Thank you")
        self.button.place(x=400, y=530)
        self.button.config(font=("Arial", 20, "bold"), highlightthickness=0)

        # self.button1 = Button(self.screen, command=threading.Thread(target=clear).start)
        self.button1 = Button(command=clear,width=8)
        self.button1.grid(column=0, row=11)
        self.button1.config(text="Clear")
        self.button1.place(x=410, y=630)
        self.button1.config(font=("Arial", 20, "bold"), highlightthickness=0)


        self.serial_number = self.donners_serial_number.get()
        self.date_of_donation = self.donner_blood_given_date.get()

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

        self.screen.mainloop()
