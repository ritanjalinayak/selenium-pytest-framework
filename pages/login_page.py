from selenium.webdriver.common.by import By
import time
class loginpage:
    def __init__(self,driver):
        self.driver=driver


    username_input=(By.NAME ,"username")
    password_input=(By.ID , "password")
    sumit_button=(By.ID , "submit")
    error_msg=(By.ID , "error")
    success_msg=(By.CLASS_NAME , "post-title")


    def enter_username(self, username):
        self.driver.find_element(*self.username_input).clear()   
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_sumit(self):
        self.driver.find_element(*self.sumit_button).click()


    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_sumit()  

    def get_success_msg(self):
        return self.driver.find_element(*self.success_msg).text

    def get_error_msg(self):
        return self.driver.find_element(*self.error_msg).text          



        




