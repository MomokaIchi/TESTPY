# What does this function return?

def check(n):
    if n:
        return True
    return False

# check(0) -> True
# check(3) -> True
# if n is "", nothing, return False

# for test
num = bool(input("put number:"))
print(f"answer is {num}")
