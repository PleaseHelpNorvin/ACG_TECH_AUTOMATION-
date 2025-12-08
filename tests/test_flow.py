import uuid
from src.pages.login import LoginPage 

def test_flow(page): 
    page.goto("http://localhost:8890/")

    login = LoginPage(page)

    login.login("acgtech", "locks", "bypassed")


