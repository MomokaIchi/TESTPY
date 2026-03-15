class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append({"name": name, "done": False})

    def show_task(self):
        for i, task in enumerate(self.tasks, start=1):
            print(i, task["name"], task["done"])

    def done_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
        else:
            print("Invalid Index")


tm = Task()

tm.add_task("Study Python")
tm.add_task("Go to Spanish party")

tm.show_task()

tm.done_task(0)

tm.show_task()