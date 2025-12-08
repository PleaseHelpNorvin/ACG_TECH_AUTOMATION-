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

    login = LoginPage(page)
    navigation = Navigate(page)
    openlocknow = OpenLockNowPage(page)
    resetuserkeynow = ResetUserKeyNowPage(page)
    resettampernow = ResetTamperNowPage(page)
    closecodevialockid = CloseCodeViaLockIdPage(page)
    closecodeviaaseal = CloseCodeViaASealPage(page)
    openlocknokeycode = OpenLockNoKeyCodePage(page)
    returnactiveoperationcode = ReturnActiveOperationCodePage(page)

    login.login("acgtech", "locks", "bypassed")
    openlocknow_flow(navigation, openlocknow)
    resetuserkeynow_flow(navigation, resetuserkeynow)
    resettampernow_flow(navigation, resettampernow)
    closecodevialockid_flow(navigation, closecodevialockid)
    closecodeviaaseal_flow(navigation, closecodeviaaseal)
    openlocknokeycode_flow(navigation, openlocknokeycode)
    returnactiveoperationcode_flow(navigation, returnactiveoperationcode)
    logout(page)
    
def openlocknow_flow(navigation, openlocknow):
    navigation.go_to_open_lock_now()
    openlocknow.hello()
    
def resetuserkeynow_flow(navigation, resetuserkeynow):
    navigation.go_to_reset_user_key_now()
    resetuserkeynow.hello()

def resettampernow_flow(navigation, resettampernow):
    navigation.go_to_reset_tamper_now()
    resettampernow.hello()

def closecodevialockid_flow(navigation, closecodevialockid):
    navigation.go_to_close_code_via_lock_id()
    closecodevialockid.hello()

def closecodeviaaseal_flow(navigation, closecodeviaaseal):
    navigation.go_to_close_code_via_a_seal()
    closecodeviaaseal.hello()

def openlocknokeycode_flow(navigation, openlocknokeycode):
    navigation.go_to_open_lock_no_key_code()
    openlocknokeycode.hello()

def returnactiveoperationcode_flow(navigation, returnactiveoperationcode):
    navigation.go_to_return_active_operation_codes()
    returnactiveoperationcode.hello()

def logout(page):
    print("logout")
    page.goto("http://localhost:8890/technician/logout")
    