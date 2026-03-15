class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_task(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}, {task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid Index")

tm = TaskManager()

tm.add_task("Study Python")
tm.add_task("Go to Spanish community party")
tm.add_task("Sleep enough")

tm.show_task()