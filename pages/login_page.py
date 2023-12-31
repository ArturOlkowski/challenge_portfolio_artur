from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = "Scouts Panel"
    # add_player = "//*[text()= 'Add player']"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def type_in_password(self, passord):
        self.field_send_keys(self.password_field_xpath, passord)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_title_of_header(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)

    # def click_add_player(self):
    #     self.click_on_the_element(self.click_add_player)
