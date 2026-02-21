from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(self.__class__.__name__)

    def enter_text(self, locator, text):
        self.logger.info(f"Entering text into {locator}")
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def click(self, locator):
        self.logger.info(f"Clicking on {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def read_msg(self,locator):
        self.logger.info(f"Reading from  {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def get_title(self):
        return self.driver.title
   

    def get_informations(self, locator):
        self.logger.info("get_informations is called")
        # return self.wait.until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)
    
    def updateUrl(self, url):
        self.logger.info(f"Navigating to URL: {url}")
        self.driver.get(url)
    
    def uncheckbox(self,locater):
        self.logger.info(f"uncheck the uncheckbox{locater}")
        element=self.wait.until(EC.element_to_be_clickable(locater))
        if element.is_selected():
            element.click()

    

        
