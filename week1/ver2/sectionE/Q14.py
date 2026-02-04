# Write a simple number guessing program:
# Store secret number = 7
# Ask user to input a number
# If equal -> print "Correct"
# Else -> print "Wrong"

num_ans = 7
num_user = int(input("Guess number: "))
if num_user == num_ans:
    print("Correct")
else:
    print("Wrong")