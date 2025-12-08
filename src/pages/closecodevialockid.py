from src.pages.base_page import BasePage

class CloseCodeViaLockIdPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def hello(self):
        print("hellow CloseCodeViaLockIdPage")