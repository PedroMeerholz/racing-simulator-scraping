from selenium.webdriver import Edge
from selenium.webdriver.common.by import By


class TrackScraper:
    driver = Edge()

    def open_url(self, url: str):
        self.driver.get(url)

    def get_iracing_tracks(self, class_name: str):
        track_list = self.driver.find_elements(by=By.CLASS_NAME, value=class_name)
        track_names = []
        for track_element in track_list:
            track_name = track_element.accessible_name
            track_names.append(track_name)
        return track_names

    def get_asseto_corsa_tracks(self, class_name: str):
        track_div_list = self.driver.find_elements(by=By.CLASS_NAME, value=class_name)
        tracks = []
        for track_div in track_div_list[8:25]:
            track_name_element = track_div.find_element(by=By.TAG_NAME, value='p')
            track_name = track_name_element.get_attribute('innerHTML')
            tracks.append(track_name)
        return tracks

    def get_asseto_corsa_competizione_tracks(self, class_name: str):
        track_div_list = self.driver.find_elements(by=By.CLASS_NAME, value=class_name)
        tracks = []
        for track_div in track_div_list:
            track_name_element = track_div.find_element(by=By.TAG_NAME, value='p')
            track_name = track_name_element.get_attribute('innerHTML')
            tracks.append(track_name)
        return tracks

    def get_gran_turismo_sport_tracks(self, class_name):
        track_div_list = self.driver.find_elements(by=By.CLASS_NAME, value=class_name)
        tracks = []
        for track_div in track_div_list:
            track_name_element = track_div.find_element(by=By.TAG_NAME, value='h2')
            track_name = track_name_element.get_attribute('innerHTML')
            tracks.append(track_name)
        return tracks

    def get_rfactor2_car_names(self, class_name: str):
        table = self.driver.find_element(by=By.CLASS_NAME, value=class_name)
        table_rows = table.find_elements(by=By.TAG_NAME, value='li')
        track_names = []
        for row in table_rows:
            row_sublist = row.find_elements(by=By.TAG_NAME, value='ol')
            for sublist in row_sublist:
                track_sublist = sublist.find_elements(by=By.TAG_NAME, value='a')
                for track in track_sublist:
                    track_name = track.accessible_name
                    track_names.append(track_name)
        return track_names

    def close_url(self):
        self.driver.quit()
