# try:
#     print(x)
# except:
#     print("An wxception occured")

# print(X)

# try:
#     print(x)
# except:
#     print("Something else went wrong")
# except NameError:
#     print("Variable x is not defined")

# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")

# try:
#     print("Hi")
# except:
#     print("Something went wrong")
# finally:
#     print("The 'try except' is finished")

# try:
#     f = open("demofile.txt")
#     try:
#         f.write("Lorum Ipsum")
#     except:
#         print("Something went wrong when writing to the file")
#     finally:
#         f.close()
# except:
#     print("Something went wrong when opening the file")

# x = -1

# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

x = "Hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")