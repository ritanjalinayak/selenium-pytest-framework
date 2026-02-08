
from pages.register_page import RegisterPage
from selenium.webdriver.common.by import By

def test_user_registration(initial_setup):
    driver=initial_setup

    user_data = {
        "first_name": "Ritu",
        "last_name": "Tester",
        "email": "ritu.test006@gmail.com",
        "company": "QA Company",
        "password": "Test@12345"
    }
    

    register = RegisterPage(driver)

    register.userRegister(user_data)

    # Validation
    
    # assert "Your registration completed" in driver.page_source.lower()
    


    success_msg = driver.find_element(By.CLASS_NAME, "result")
    assert "registration completed" in success_msg.text.lower()