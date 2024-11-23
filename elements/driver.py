from enum import Enum
from typing import Union

from selenium.webdriver import Chrome, Firefox, Safari


class DriverType(Enum):
    CHROME = Chrome
    FIREFOX = Firefox
    SAFARI = Safari

class Driver:
    _instances = {}

    def __new__(cls, driver_type: DriverType):
        if driver_type not in cls._instances:
            instance = super(Driver, cls).__new__(cls)
            cls._instances[driver_type] = instance
            instance._initialized = False
        return cls._instances[driver_type]

    def __init__(self, driver_type: DriverType):
        if not self._initialized:
            self.driver_type = driver_type
            self.__driver = None
            self._initialized = True

    @staticmethod
    def create_driver(driver_type: DriverType) -> Union[Chrome, Firefox, Safari]:
        if driver_type is DriverType.CHROME:
            return Chrome()
        if driver_type is DriverType.FIREFOX:
            return Firefox()
        if driver_type is DriverType.SAFARI:
            return Safari()
        else:
            raise ValueError("Error DriverType")

    @property
    def driver(self):
        if not self.__driver:
            self.__driver = self.create_driver(self.driver_type)
        return self.__driver
