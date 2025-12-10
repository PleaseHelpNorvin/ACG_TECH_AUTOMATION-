from src.pages.base_page import BasePage

class OpenLockNoKeyCodePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def test_form(self, tech):
        print(f"[OpenLockNoKeyCode] Technician: {tech}")
        self.fill_text("input[name='LockId']", "12345678")
        self.fill_text("input[name='Pin']", "0000") 
        self.click_element("#btnExecute")
        self.sleep(2)