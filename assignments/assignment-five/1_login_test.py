import login
import database

def test_login():
    username = "Bob"
    password = "Wrong password"
    loggedIn = login.login_pass(username, password)
    assert loggedIn == False
