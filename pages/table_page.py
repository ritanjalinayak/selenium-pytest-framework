import configparser

from selenium.webdriver.common.by import By
from base.base_page import BasePage

class TablePage(BasePage):

    java_language=(By.XPATH, "//input[@value='Java']")
    courese_table=(By.XPATH, "//tbody/tr")
    intermeditade_checkbox=(By.XPATH, "//input[@name='level' and @value='Intermediate']")
    advance_checkbox=(By.XPATH, "//input[@name='level' and @value='Advanced']")
    option_10000 = (By.XPATH, "//li[text()='10,000+']")
    option_any=(By.CLASS_NAME, "dropdown-label")



    def verifyCourseTable(self):       
        self.set_table_url()
        self.click(self.java_language)
        datas = self.get_informations(self.courese_table)
        for data in datas:
            if data.is_displayed():
                value=data.find_element(By.XPATH,"./td[3]").text
                self.logger.info(f"pulled data {value}")
                if value.lower() != "java":
                    return False
        return True
    

    def set_table_url(self):
        config = configparser.ConfigParser()
        config.read("config/config.ini")
        url = config["DEFAULT"]["TABLE_URL"]
        self.updateUrl(url)

 
    def verify_course_begineer(self):       
        self.set_table_url()
        self.uncheckbox(self.intermeditade_checkbox)   
        self.uncheckbox(self.advance_checkbox)
        
        datas = self.get_informations(self.courese_table)
        for data in datas:
            if data.is_displayed():
                value=data.find_element(By.XPATH,"./td[4]").text
                self.logger.info(f"pulled data {value}")
                if value.lower() != "beginner":
                    return False
        return True    
    


    def Check_Minenrollments(self):     
        self.set_table_url()
        self.click(self.option_any)
        self.click(self.option_10000)
        datas = self.get_informations(self.courese_table)

        for data in datas:
            if data.is_displayed():
                value=data.find_element(By.XPATH,"./td[5]").text
                self.logger.info(f"pulled data for enrollment {value}")
                value_parse= int(value)
                if value_parse <10000:
                    return False
        return True   




        








    

