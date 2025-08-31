class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False 

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.title}: {self.description} [{status}]"


class ToDoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Задача \"{task.title}\" добавлена.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Задача \"{title}\" удалена.")
                return
        print(f"Задача \"{title}\" не найдена.")

    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            print("Список задач:")
            for task in self.tasks:
                print("-", task)


manager = ToDoManager()

task1 = Task("Сделать домашку", "Математика, задачи 1-5")
task2 = Task("Прочитать книгу", "Глава 3")

manager.add_task(task1)
manager.add_task(task2)

manager.show_tasks()

task1.mark_complete()

print("\nПосле выполнения одной задачи:")
manager.show_tasks()

manager.remove_task("Прочитать книгу")
print("\nПосле удаления:")
manager.show_tasks()
