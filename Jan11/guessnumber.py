import random

num_answer = random.randint(1,10)

# input number from user
def guess_num():
    num = input("Guess the number (1-10):")
    return num

# input check
def is_number(num):
    if num.isdecimal():
        return int(num)
    else:
        print("put number")
        return False

# answer check
def answer_check(num_user, num_answer):
    if num_user == num_answer:
        print("Correct")
        return True
    else:
        print("Wrong")
        return False


# main
for i in range(5):
    num_user = is_number(guess_num())
    if num_user == False:
        exit
    else:
        x = answer_check(num_user, num_answer)
        if x:
            break
        else:
            exit

print(f"The answer was {num_answer}")
