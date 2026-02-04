# Fix this function (minimum change):
def is_admin(user):
    if user.is_admin == True:
        return True
    else:
        return False
    
def is_admin(user) -> bool:
    return user.is_admin