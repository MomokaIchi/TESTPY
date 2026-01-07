# number guess game
import random
(i,num_guess) = (0,0)
num_answer = random.randint(1,10)

while i <= 4:
    if num_guess == num_answer:
        print("Correct!")
        break
    else:
        num_guess = int(input("Guess the number (1-10):"))
    i=i+1

print(f"The answer was {num_answer}")