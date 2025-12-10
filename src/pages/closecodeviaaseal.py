from src.pages.base_page import BasePage

class CloseCodeViaASealPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def test_form(self, tech):
        print(f"[CloseCodeViaASeal] Technician: {tech}")
        self.fill_text("input[name='ASeal']", "12345678")
        self.click_element("#btnExecute")
        self.sleep(2)