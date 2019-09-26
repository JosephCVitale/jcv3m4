from database import USER1

#Always returns true 
def login_fail(username, password):
    return True

#Returns true only when username and password are correct
def login_pass(username, password):
    correct = False
    if username == USER1["username"] and password == USER1["password"]:
        correct = True
    return correct
    


