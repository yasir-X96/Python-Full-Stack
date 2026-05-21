def login_required(func):

    def wrapper(*args, **kwargs):

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "admin" and password == "admin123":
            print("Login Successful\n")
            return func(*args, **kwargs)

        else:
            print("Invalid Login Credentials")

    return wrapper