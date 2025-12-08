from src.pages.base_page import BasePage

class Navigate(BasePage):
    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)

    def go_to_open_lock_now(self):
        self.go_to("openlocknow")

    def go_to_reset_user_key_now(self):
        self.go_to("resetuserkeynow")

    def go_to_reset_tamper_now(self):
        self.go_to("resettampernow")
    
    def go_to_close_code_via_lock_id(self):
        self.go_to("closecodevialockid")
    
    def go_to_close_code_via_a_seal(self):
        self.go_to("closecodeviaaseal")
    
    def go_to_open_lock_no_key_code(self):
        self.go_to("openlocknokeycode")

    def go_to_return_active_operation_codes(self):
        self.go_to("returnactiveoperationcodes")
        