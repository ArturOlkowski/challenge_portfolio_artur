import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    Main_page_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    Player_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    Language_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    Sign_out_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    Players_count_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[1]/div/div[1]"
    Reports_count_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[3]/div/div[1]"
    Matches_count_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/div[1]"
    Events_count_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[4]/div/div[1]"
    Scouts_panel_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[2]/h2"
    Shortcuts_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/h2"
    Activity_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h2"
    expected_tile = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_tile
