from __future__ import annotations

from typing import NamedTuple

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from

from tests.conftest import DriverType

BASE_TABLE_LOCATORS = {
    'TABLE': (By.XPATH, '//table[@class="dataTable"]'),
    'TABLE_HEADER': (By.XPATH, '//tr[@class="header"]'),
    'TABLE_ROW': (By.XPATH, './/tr'),
    'TABLE_EDIT_ROW': (By.XPATH, './/a[@title="Edit"]'),
    'TABLE_COLUMN_HEADER': (By.XPATH, './/th'),
    'TABLE_COLUMN_ROW': (By.XPATH, './/td')
}
Locator = NamedTuple("Locator", [("method", By), ("query", str)])


class Driver:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:                       # при первом вызове создаем объект
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.__driver = self.create_driver()

    @staticmethod
    def create_driver() -> WebDriver:
        return webdriver.Chrome()

    @property
    def driver(self):
        return self.__driver

class Element:
    def __init__(self, locator: Locator):
        self.driver = Driver().driver
        self.locator = locator

    def find(self) -> WebElement:
        return self.driver.find_element(self.locator)

    def click(self) -> None:
        return self.find().click()
    
    def text(self) -> str:
        return self.find().text


class Table(Element):
    def __init__(
            self,
            locator: Locator | None
    ):
        super().__init__(
            locator=locator or Locator(method=By.XPATH, query='//table[@class="dataTable"]')
        )

        self.table_header = Element(Locator(method=By.XPATH, query='.//tr[@class="header"]'))
        self.table_row = Element(Locator(method=By.XPATH, query='.//tr'))
        self.table_column_header = Element(Locator(method=By.XPATH, query='.//th'))
        self.table_column_row = Element(Locator(method=By.XPATH, query='.//td'))
        self.table_edir_row = Element(Locator(method=By.XPATH, query='.//a[@title="Edit"]'))

        self.driver = drive
        self.table_locators = table_locators
        self._column_name = None
        self._table_data = None

    @property
    def table(self) -> WebElement:

        return self.driver.find_element(*self.table_locators['TABLE'])

    @property
    def table_header(self) -> WebElement:

        return self.table.find_element(*self.table_locators['TABLE_HEADER'])

    @property
    def table_rows(self) -> list[WebElement]:

        return self.table.find_elements(*self.table_locators['TABLE_ROW'])[1:-1]

    def edit_row(self, row: WebElement) -> None:
        row.find_element(*self.table_locators['TABLE_EDIT_ROW']).click()

    def get_column_name(self) -> list[str]:
        if self._column_name:
            return self._column_name

        self._column_name = []
        no_name_count = 1
        table_header = self.table.find_element(*self.table_locators['TABLE_HEADER'])
        for column in table_header.find_elements(*self.table_locators['TABLE_COLUMN_HEADER']):
            if not column.text.strip():
                self._column_name.append(f'no_name_column_{no_name_count}')
                no_name_count += 1
            else:
                self._column_name.append(column.text)

        return self._column_name

    def get_row_data(self, row: WebElement) -> dict[str, tuple[str, WebElement]]:
        row_value = [(column.text, column) for column in row.find_elements(*self.table_locators['TABLE_COLUMN_ROW'])]

        return {column_name: column_value for column_name, column_value in zip(self.get_column_name(), row_value)}

    def get_table_data(self) -> list[dict[str, tuple[str, WebElement]]]:
        if self._table_data:
            return self._table_data

        self._table_data = []
        for row in self.table_rows:
            row_value = [(column.text, column) for column in row.find_elements(*self.table_locators['TABLE_COLUMN_ROW'])]
            self._table_data.append({column_name: column_value for column_name, column_value in zip(self.get_column_name(), row_value)})

        return self._table_data