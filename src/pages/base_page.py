from playwright.sync_api import Page
import time

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    BASE_URL = "http://localhost:8890/technician/dashboardv2/form/"
    
    SECTIONS = {
        "openlocknow" : "OpenLockNow",
        "resetuserkeynow" : "ResetUserKeyNow",
        "resettampernow" : "ResetTamperNow", 
        "closecodevialockid" : "CloseCodeViaLockId", 
        "closecodeviaaseal" : "CloseCodeViaASeal", 
        "openlocknokeycode" : "OpenLockNoKeyCode", 
        "returnactiveoperationcodes" : "ReturnActiveOperationCodes", 
    }


    def sleep(self, seconds: int):
        time.sleep(seconds)

    def navigate(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def go_to(self, section: str):
        """Navigate using section keys defined in SECTIONS."""
        if section not in self.SECTIONS:
            raise ValueError(f"Unknown section '{section}'. Valid sections: {list(self.SECTIONS.keys())}")

        full_url = f"{self.BASE_URL}{self.SECTIONS[section]}"
        self.page.goto(full_url)
        self.page.wait_for_load_state("networkidle")

    def fill_text(self, selector: str, text: str):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, text)
        
    def click_element(self, selector: str):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

