print("Choose the mode:")
try:
    mode = int(input("See the list (1)\n" \
    "Add a task to the list (2)\n" \
    "End (0)\n"))
except:
    print("Only 1-4 are allowed")

if mode == 1:
    with open("week2/lesson/CLITodoList.txt", "r") as f:
        print(f.read())
elif mode == 2:
    todo_cont = input("write a content: ")
    with open("week2/lesson/CLITodoList.txt", "a") as f:
        f.write(todo_cont + "\n")
    print("TodoList was updated to this: ")
    with open("week2/lesson/CLITodoList.txt", "r") as f:
        print(f.read())
else:
    print("App closed")

# other numbers -> print invalid number, except: only integer number allowed will be better.
