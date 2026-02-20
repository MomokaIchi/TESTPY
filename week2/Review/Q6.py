# Mutation Awareness
# What is printed? Be careful about when len(num) is evaluated.

nums = [1, 2]
nums.append(len(nums))
print(nums)