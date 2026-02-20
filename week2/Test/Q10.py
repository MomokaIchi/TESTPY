# Mini Backend Mindset Question
# You are validating user input.

password = ""
if password:
    print("OK")
else:
    print("Invalid")

# 1. What is printed?
# 2. Why is this check useful in backend systems?

# OK
# bool("")=False but ""!=False
# So OK? but I want this func to show Invalid