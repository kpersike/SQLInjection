import model

def form():
    username = input("Username: ")
    password = input("Password: ")
    model.login(username, password)