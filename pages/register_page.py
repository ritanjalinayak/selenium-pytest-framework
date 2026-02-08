from selenium.webdriver.common.by import By
import time
class RegisterPage:
    def __init__(self,driver):
        self.driver=driver


        self.gender_female = (By.ID, "gender-female")
        self.First_name=(By.ID, "FirstName")
        self.Last_name=(By.NAME,"LastName")
        self.Email=(By.NAME,"Email")
        self.CompanyName=(By.NAME,"Company")
        self.Password=(By.NAME,"Password")
        self.confirm_password=(By.NAME,"ConfirmPassword")
        self.Register_button=(By.NAME,"register-button")
            

    def userRegister(self,user_data):
        self.driver.find_element(*self.gender_female).click()

        self.driver.find_element(*self.First_name).clear()
        self.driver.find_element(*self.First_name).send_keys(user_data["first_name"])

        self.driver.find_element(*self.Last_name).clear()
        self.driver.find_element(*self.Last_name).send_keys(user_data["last_name"])
        
        self.driver.find_element(*self.Email).clear()
        self.driver.find_element(*self.Email).send_keys(user_data["email"])

        self.driver.find_element(*self.CompanyName).clear()
        self.driver.find_element(*self.CompanyName).send_keys(user_data["company"])
        
        self.driver.find_element(*self.Password).clear()
        self.driver.find_element(*self.Password).send_keys(user_data["password"])

        self.driver.find_element(*self.confirm_password).clear()
        self.driver.find_element(*self.confirm_password).send_keys(user_data["password"])

        self.driver.find_element(*self.Register_button).click()
        time.sleep(5)

        




