# f = open("week2/lesson/CLITodoList.txt", "x") # completely meaningless

# with open("week2/lesson/CLITodoList.txt", "a") as f:
#     f.write("Todo List!")

# with open("week2/lesson/CLITodoList.txt") as f:
#     print(f.read())

# with open("week2/lesson/CLITodoList.txt", "a") as f:
#     f.write("Added\n")

# with open("week2/lesson/CLITodoList.txt") as f:
#     print(f.read())

# user input:


todo_cont = input("write a content: ")
with open("week2/lesson/CLITodoList.txt", "a") as f:
    f.write(todo_cont + "\n")
