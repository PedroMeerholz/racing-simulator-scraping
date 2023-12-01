from selenium.webdriver import Edge
from selenium.webdriver.common.by import By


class Scraper:
    driver = Edge()

    def open_url(self, url: str):
        self.driver.get(url)

    def get_car_element_list(self, class_name: str):
        return self.driver.find_elements(by=By.CLASS_NAME, value=class_name)

    def get_iracing_car_names(self, class_name: str):
        car_list = self.get_car_element_list(class_name)
        car_names = []
        for car_name_element in car_list:
            car_name = car_name_element.accessible_name
            car_names.append(car_name)
        return car_names

    def get_asseto_corsa_car_names(self, class_name: str):
        car_list = self.get_car_element_list(class_name)
        car_names = []
        for car_name_element in car_list:
            car_name = car_name_element.get_attribute('data-caption')
            car_names.append(car_name)
        return car_names

    def get_gran_turismo_sport_car_names(self, class_name: str):
        table = self.get_car_element_list(class_name)[0]
        table_rows = table.find_elements(by=By.TAG_NAME, value='dl')
        car_names = []
        for table_row in table_rows[1:]:
            row_data = table_row.find_elements(by=By.TAG_NAME, value='dd')
            car_name = row_data[1].text
            car_names.append(car_name)
        return car_names

    def close_url(self):
        self.driver.quit()
