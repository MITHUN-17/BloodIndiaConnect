import time
from tkinter import *
from PIL import ImageTk, Image
from ONE_Finding_donners_screen import Finding_blood_tkscreen
from TWO_blood_donated_doners_screen import updating_the_date_of_blood_given_donners_tkscreen
from THREE_donners_registration_portal_screen import donners_registration_tkscreen
from FOUR_status_update_screen import status_update_tkscreen


class tkscreen():
    def __init__(self):
        def find_doner():
            self.screen.destroy()
            Finding_blood_tkscreen()
            tkscreen()

        def Update_date():
            self.screen.destroy()
            updating_the_date_of_blood_given_donners_tkscreen()
            tkscreen()
        def Status_update():
            self.screen.destroy()
            status_update_tkscreen()
            tkscreen()
        def registration():
            self.screen.destroy()
            donners_registration_tkscreen()
            tkscreen()
        self.screen = Tk()

        # self.screen.config(background="#FFFFFF")
        self.screen.maxsize(950, 950)
        self.screen.minsize(950, 950)
        self.screen.title(string="Auto Contact Blood Donors")

        self.info = Label(text="Welcome to Auto Contact Blood Donors")
        # self.info.config(background="#FFFFFF")
        self.info.grid(column=0, row=0)
        self.info.config(font=("Arial", 22, "bold"))
        self.info.config(pady=50, padx=180)

        self.find_doners = Button(command=find_doner)
        self.find_doners.config(text="Contact Donors")
        self.find_doners.place(x=330, y=200)
        self.find_doners.config(font=("Arial", 20, "bold"), highlightthickness=1)

        self.status_update = Button(command=Status_update)
        self.status_update.config(text="Status Update")
        self.status_update.place(x=350, y=300)
        self.status_update.config(font=("Arial", 20, "bold"), highlightthickness=1)

        self.update_date_of_blood_donation = Button(command=Update_date)
        self.update_date_of_blood_donation.config(text="Update Date of Blood Donated")
        self.update_date_of_blood_donation.place(x=260, y=400)
        self.update_date_of_blood_donation.config(font=("Arial", 20, "bold"), highlightthickness=1)

        self.donners_registration = Button(command=registration)
        self.donners_registration.config(text="Register New Donor ")
        self.donners_registration.place(x=300, y=500)
        self.donners_registration.config(font=("Arial", 20, "bold"), highlightthickness=1)

#
#
#
#

        self.image = Image.open("2.jpg")
        self.resise_image = self.image.resize((270, 400))
        self.img = ImageTk.PhotoImage(self.resise_image)

        self.image_label = Label(image=self.img)
        self.image_label.place(x=-20, y=80)

        self.image1 = Image.open("2.jpg")
        self.resise_image1 = self.image.resize((270, 400))
        self.img1 = ImageTk.PhotoImage(self.resise_image)

        self.image_label1 = Label(image=self.img1)
        self.image_label1.place(x=690, y=80)

        self.image2 = Image.open("heart.webp")
        self.resise_image2 = self.image2.resize((940, 220))
        self.img2 = ImageTk.PhotoImage(self.resise_image2)

        self.image_label2 = Label(image=self.img2)
        self.image_label2.place(x=0, y=570)

        self.screen.mainloop()



