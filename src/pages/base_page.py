from playwright.sync_api import Page
import time

class BasePage:
    BASE_URL = "http://localhost:8889"
    
    SECTIONS = {
        "" : "",
    }

    def __init__(self, page: Page):
        self.page = page

    def sleep(self, seconds: int):
        time.sleep(seconds)

    def navigate(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")