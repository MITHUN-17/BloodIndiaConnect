from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from  tkinter import  messagebox
from tkinter import *
class Location_finder:
    def __init__(self,address):
        self.option = webdriver.ChromeOptions()
        self.option.headless = True
        self.chrome = "C:\\chromedriver_win32 (1)\\chromedriver.exe"
        # self.chrome = "C:\\Users\\venkatesan\\Downloads\\chromedriver_win32\\chromedriver"
        self.driver= webdriver.Chrome(executable_path=self.chrome,chrome_options=self.option)
        # self.driver= webdriver.Chrome(executable_path=self.chrome)

        self.address = address
        list_of_address=str(address).split("\n")
        self.a=(",".join(list_of_address))
        print(self.a)

        try:

            self.driver.get("https://www.google.com/maps/@10.9358408,76.952783,15z")
            self.search=self.driver.find_element(By.XPATH,'//*[@id="searchboxinput"]')
            self.search.send_keys(self.a)
            time.sleep(2)
            self.click=self.driver.find_element(By.XPATH,'//*[@id="searchbox-searchbutton"]')
            self.click.click()
            time.sleep(20)
            self.share=self.driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[5]/button/div[1]')
            self.share.click()
            time.sleep(20)
            self.exact_location=self.driver.find_element(By.XPATH,'//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div[1]/div[3]/div[2]')
            self.exact_location_text=self.exact_location.text
            self.link=self.driver.find_element(By.CLASS_NAME,'vrsrZe').get_attribute("value")
            self.driver.quit()
            # print(f"{self.exact_location_text}\n{self.link}")


        except:
            # try:
            #     answer = messagebox.showinfo("INFO", "Error Ocured Try Again")
            #     Label(text=answer, font=('Arial 20 bold'))
            # except:
            #     pass

            self.driver.quit()



