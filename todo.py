from tasks import TaskManager
from utils import display_menu, get_input


def main():
    manager = TaskManager()

    while True:
        display_menu()
        choice = get_input("Choose an option (1-4): ")

        if choice == "1":
            title = get_input("Task title: ")
            desc = get_input("Task description (optional): ")
            manager.add_task(title, desc)
            print("Task added!")

        elif choice == "2":
            print("\nTasks:")
            for i, task in enumerate(manager.list_tasks()):
                print(f"{i}. {task}")
            task_idx = int(get_input("Enter task number to complete: "))
            manager.complete_task(task_idx)
            print("Task marked as completed!")

        elif choice == "3":
            print("\nAll Tasks:")
            for task in manager.list_tasks():
                print(task)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()