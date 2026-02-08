import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("\nСписок задач пуст.\n")
        return

    print("\nТвои задачи:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']}")
    print()


def add_task(tasks):
    title = input("Введите название задачи: ").strip()
    if not title:
        print("Название не может быть пустым.\n")
        return

    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Задача добавлена.\n")


def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        number = int(input("Введите номер выполненной задачи: "))
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Задача отмечена как выполненная.\n")
    except (ValueError, IndexError):
        print("Неверный номер задачи.\n")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        number = int(input("Введите номер задачи для удаления: "))
        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Удалена задача: {removed['title']}\n")
    except (ValueError, IndexError):
        print("Неверный номер задачи.\n")


def main():
    tasks = load_tasks()

    while True:
        print("Меню:")
        print("1 — Показать задачи")
        print("2 — Добавить задачу")
        print("3 — Отметить как выполненную")
        print("4 — Удалить задачу")
        print("0 — Выход")

        choice = input("Выбери действие: ").strip()
        print()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неизвестная команда. Попробуй снова.\n")


if __name__ == "__main__":
    main()
