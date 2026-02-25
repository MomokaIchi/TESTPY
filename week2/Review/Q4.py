# Countinue Precision
# What is printed? 

for i in range(4):
    if i % 2 == 0:
        continue
    print(i)
    
# i will be 0, 1, 2, 3
# When i is even, it goes to continue and prints nothig.
# When i is odd, it doesn't go to inside the if loop, so it prints i
# The answer is 1 3
# perfect