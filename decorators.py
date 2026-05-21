from ems.session import session
def require_admin(func):
    def wrapper(*args,**kwargs):
        # check role
        if session["role"]!="Admin":
            print("permission not allowed")
            return
        print(f"role is :sessiion{session["role"]}")

    return wrapper