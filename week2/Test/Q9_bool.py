# False list: 0, 0.0, "", [], {}, None, False

# bool_list = {1: 0, 2: 0.0, 3: "", 4: [], 5: {}, 6: None, 7:False}

# for key in bool_list:
#     print(key, bool(bool_list.keys))


# "if not 0" = "if not False" = "if True" then start program inside this "if"
# "if not 0" is like if/not 0, check not 0 is True or False

# print(bool(0)) # False
# print(bool([])) # False
# False list: 0, 0.0, 0j, False, None, "", [], {}, set()

# but [] is list object, not boolian


# print(False-True) # the answer is -1 (True and False are subclass of int)
# print(bool([1])) # True
# print(bool([0])) # True

# if 0==False:
#     print("F")
# if 1:
#     print("1")
# if 0:
#     print("0")
# if []:
#     print("0")
# if [0]:
#     print("[0]")

# print(bool(0)) # False
# print(bool(1)) # True
# print(bool("")) # False
# print(bool("0")) # True

# if 0==False:
#     print("0=F") # printed
# if 1==False:
#     print("1=F") # not printed
# if ""==False:
#     print("''=F") # NOT printed 
# if "0"==False:
#     print("'0'=F") # not printed

if bool(0)==False:
    print("0=F") # printed
if bool(1)==False:
    print("1=F") # not printed
if bool("")==False:
    print("''=F") # printed 
if bool("0")==False:
    print("'0'=F") # not printed