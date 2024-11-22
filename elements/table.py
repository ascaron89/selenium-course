from __future__ import annotations

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


BASE_TABLE_LOCATORS = {
    'TABLE': (By.XPATH, '//table[@class="dataTable"]'),
    'TABLE_HEADER': (By.XPATH, '//tr[@class="header"]'),
    'TABLE_ROW': (By.XPATH, './/tr'),
    'TABLE_EDIT_ROW': (By.XPATH, './/a[@title="Edit"]'),
    'TABLE_COLUMN_HEADER': (By.XPATH, './/th'),
    'TABLE_COLUMN_ROW': (By.XPATH, './/td'),
    'TABLE_SELECTED_VALUE': (By.XPATH, './/select/option[@selected]'),
}


class Table:
    def __init__(self, driver: WebDriver, table_locators=None):
        if table_locators is None:
            table_locators = BASE_TABLE_LOCATORS
        self.driver = driver
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
        """Редактирование переданной строки."""

        row.find_element(*self.table_locators['TABLE_EDIT_ROW']).click()

    def get_column_name(self) -> list[str]:
        """Возвращает имена столбцов."""

        if self._column_name:
            return self._column_name

        self._column_name = []
        no_name_count = 1
        for column in self.table_header.find_elements(*self.table_locators['TABLE_COLUMN_HEADER']):
            if not column.text.strip():
                self._column_name.append(f'no_name_column_{no_name_count}')
                no_name_count += 1
            else:
                self._column_name.append(column.text)

        return self._column_name


    def get_row_data(self, row: WebElement) -> dict[str, tuple[str, WebElement]]:
        """Возвращает данные строки."""

        row_value = []
        for column in row.find_elements(*self.table_locators['TABLE_COLUMN_ROW']):
            if c := column.find_elements(*self.table_locators['TABLE_SELECTED_VALUE']):
                row_value.append((c[0].text, column))
            else:
                row_value.append((column.text, column))

        return {column_name: column_value for column_name, column_value in zip(self.get_column_name(), row_value)}

    def get_table_data(self) -> list[dict[str, tuple[str, WebElement]]]:
        """Возвращает данные таблицы."""

        if self._table_data:
            return self._table_data

        self._table_data = []
        for row in self.table_rows:
            self._table_data.append(self.get_row_data(row))

        return self._table_data