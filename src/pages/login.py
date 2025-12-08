from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, username: str, password: str, captcha: str):
        self.fill_text("#Username", username)
        self.fill_text("#Password", password)
        self.fill_text("#CaptchaCase", captcha)
        self.click_element("#AuthenticationLogin input[type='submit']")
        self.page.wait_for_url("**/technician/dashboardv2", timeout=30000)
