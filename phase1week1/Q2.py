# Q2 Write a function
# def can_access(is_admin: bool, is_active: bool) -> bool:
# Roules:
# Admins can always access
# non-admins can access only if active

# def can_access(is_admin: bool, is_active: bool) -> bool:
#     if is_admin:
#         return True
#     else:
#         return is_active

def can_access(is_admin: bool, is_active: bool) -> bool:
    if is_admin:
        return True
    else:
        return is_active