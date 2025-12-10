import uuid
from src.pages.login import LoginPage 
from src.pages.openlocknow import OpenLockNowPage
from src.pages.navigation import Navigate
from src.pages.resetuserkeynow import ResetUserKeyNowPage
from src.pages.resettampernow import ResetTamperNowPage
from src.pages.closecodevialockid import CloseCodeViaLockIdPage
from src.pages.closecodeviaaseal import CloseCodeViaASealPage
from src.pages.openlocknokeycode import OpenLockNoKeyCodePage
from src.pages.returnactiveoperationcode import ReturnActiveOperationCodePage

def test_flow(page): 
    page.goto("http://localhost:8890/")

    technicians = ["start", "acgtech"]

    for tech in technicians:
        print(f"\n=== RUNNING FLOW FOR {tech} ===\n")

        LoginPage(page).login(tech, "locks", "bypassed")

        if tech != "start": 
            openlocknow_flow(Navigate(page), OpenLockNowPage(page), tech)
            resetuserkeynow_flow(Navigate(page), ResetUserKeyNowPage(page), tech)
            resettampernow_flow(Navigate(page), ResetTamperNowPage(page), tech)
            closecodevialockid_flow(Navigate(page), CloseCodeViaLockIdPage(page), tech)
            closecodeviaaseal_flow(Navigate(page), CloseCodeViaASealPage(page), tech)
            openlocknokeycode_flow(Navigate(page), OpenLockNoKeyCodePage(page), tech)
            returnactiveoperationcode_flow(Navigate(page), ReturnActiveOperationCodePage(page), tech)
        else : 
            resetuserkeynow_flow(Navigate(page), ResetUserKeyNowPage(page), tech)
            resettampernow_flow(Navigate(page), ResetTamperNowPage(page), tech)
            returnactiveoperationcode_flow(Navigate(page), ReturnActiveOperationCodePage(page), tech)

        logout(page)
    
def openlocknow_flow(navigation, openlocknow, tech):
    navigation.go_to_open_lock_now()
    openlocknow.test_form(tech)

def resetuserkeynow_flow(navigation, resetuserkeynow, tech):
    navigation.go_to_reset_user_key_now()
    resetuserkeynow.test_form(tech)

def resettampernow_flow(navigation, resettampernow, tech):
    navigation.go_to_reset_tamper_now()
    resettampernow.test_form(tech)

def closecodevialockid_flow(navigation, closecodevialockid, tech):
    navigation.go_to_close_code_via_lock_id()
    closecodevialockid.test_form(tech)

def closecodeviaaseal_flow(navigation, closecodeviaaseal, tech):
    navigation.go_to_close_code_via_a_seal()
    closecodeviaaseal.test_form(tech)

def openlocknokeycode_flow(navigation, openlocknokeycode, tech):
    navigation.go_to_open_lock_no_key_code()
    openlocknokeycode.test_form(tech)

def returnactiveoperationcode_flow(navigation, returnactiveoperationcode,tech):
    navigation.go_to_return_active_operation_codes()
    returnactiveoperationcode.hello()

def logout(page):
    print("logout")
    page.goto("http://localhost:8890/technician/logout")
    