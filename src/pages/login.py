from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, username: str, password: str, captcha: str):
        self.fill_text("#Username", username)
        self.fill_text("#Password", password)
        self.fill_text("#CaptchaCase", captcha)
        self.click_element("#AuthenticationLogin button[type='submit']")
        self.page.wait_for_url("**/systemstat")
