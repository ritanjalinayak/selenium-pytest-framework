from selenium.webdriver.common.by import By
from base.base_page import BasePage


class loginpage(BasePage):
    username_input=(By.NAME ,"username")
    password_input=(By.ID , "password")
    sumit_button=(By.ID , "submit")
    error_msg=(By.ID , "error")
    success_msg=(By.CLASS_NAME , "post-title")



    def login(self, username, password):
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click(self.sumit_button)
     

    def get_success_msg(self):
        return self.read_msg(self.success_msg)

    def get_error_msg(self):
        return self.read_msg(self.error_msg)        



        




