# Break Precision
# What is printed?

for i in range(5):
    if i == 3:
        break
    print(i)

# 0, 1, 2
# i will be 0,1,2,3,4
# When i is 3, it goes to if loop then break for