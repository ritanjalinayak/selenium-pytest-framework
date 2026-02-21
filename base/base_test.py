import pytest
import configparser

from utilities.driver_factory import get_driver

class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = get_driver()

        config = configparser.ConfigParser()
        config.read("config/config.ini")
        self.driver.get(config.get("DEFAULT", "BASE_URL"))

        yield
        self.driver.quit()
