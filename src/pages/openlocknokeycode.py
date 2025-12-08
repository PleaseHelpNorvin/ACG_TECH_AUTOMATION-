from src.pages.base_page import BasePage

class OpenLockNoKeyCodePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def hello(self):
        print("hellow OpenLockNoKeyCodePage")