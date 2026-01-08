# Rewrite this is the cleanest way:
def is_zero(n):
    if n == 0:
        return True
    else:
        return False
    
def is_zero_clean(n) -> bool:
    return n == 0