import random

rand_min = 1
rand_max = 10
num_answer = random.randint(rand_min,rand_max)

# input number from user
def guess_num():
    num = input(f"Guess the number ({rand_min}-{rand_max}):")
    return num

# input check
def is_number(num):
    if num.isdecimal():
        return int(num)
    else:
        print("Put number (int)")
        return False

# answer check
def answer_check(num_user, num_answer):
    if num_user == num_answer:
        print("Correct")
        return True
    else:
        print("Wrong")
        if num_user < num_answer:
            print(f"The answer is more than {num_user}")
        if num_answer < num_user:
            print(f"The answer is less than {num_user}")
        if num_user < rand_min or rand_max < num_user:
            print(f"Put {rand_min}-{rand_max}")
        return False


# main
for i in range(5):
    num_user = is_number(guess_num())
    if num_user == False:
        continue
    else:
        x = answer_check(num_user, num_answer)
        if x:
            print(f"You tried {i+1} times")
            break
        else:
            continue

print(f"The answer was {num_answer}")
