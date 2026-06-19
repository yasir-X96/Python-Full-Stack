from ems.customExceptions import UnauthorizedAccessException
from ems.session import session
def require_admin(func):
    def wrapper(*args,**kwargs):
        # check role
        if session["role"]!="Admin":
            #  print("permission not allowed")
             raise UnauthorizedAccessException("Only Admin has Rights for this action")
            
        print(f"role is :sessiion{session["role"]}")

        return func(*args,**kwargs)
    return wrapper 