import os
import importlib

def load_tasks():
    task_list = []

    for filename in os.listdir("."):  # list all files in current folder
        if filename.startswith("task") and filename.endswith(".py"):
            module_name = filename[:-3]  # remove the .py
            module = importlib.import_module(module_name)  # load the file as module

            # check if the module has run_task function
            if hasattr(module, "run_task"):
                task_list.append((module_name, module.run_task))

    return task_list


def show_menu(task_list):
    """Prints a menu of available tasks."""
    print("\nAvailable Tasks:")
    for index, (name, _) in enumerate(task_list, start=1):
        print(f"{index}. {name}")
    print("0. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu(tasks)

        # ask the user to pick a number
        choice = input("Select task number: ")

        # make sure input is a number
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        choice = int(choice)

        if choice == 0:
            print("Exiting program...")
            break

        # check if user picked a valid task
        if 1 <= choice <= len(tasks):
            task_function = tasks[choice - 1][1]  # get the run_task function
            task_function()  # run it
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
