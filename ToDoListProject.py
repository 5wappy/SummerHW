import json

def reopen_menu():
    prompt = input("If you are finished, type Q to quit, if not, type R to return to main menu: ").lower()
    if prompt == "q":
        save_tasks()
        return
    elif prompt == "r":
        to_do_list()
    else:
        print("This answer is not recognized, please retry.")
        reopen_menu()
    
def task_addition():
    add_task = input("Name of the task you'd like to add: ").capitalize()
    if add_task in tasks:
        prompt = input("The new task was found already in tasks, type Q to quit or type R to return to main menu: ").lower()
        if prompt == "q":
            save_tasks()
            return
        elif prompt == "r":
            to_do_list()
        else:
            print("This answer is not recognized, please retry.")
            reopen_menu()
    elif add_task not in tasks:
        tasks.append(add_task)
        print(tasks)
        reopen_menu()

def task_removal():
    print(tasks)
    delete_task = input("These are your tasks, type the one you would like to remove: ").capitalize()
    if delete_task in tasks:
        tasks.remove(delete_task)
        print(tasks)
        print("Your task has been removed!")
        reopen_menu()
    else:
        print("This option is not recognized, please check your spelling and check again.")
        to_do_list()

def task_edit():
    print(tasks)
    edit_task = input("Your tasks have been printed, which one would you like to change the name of? ").capitalize()

    if edit_task in tasks:
            new_task = input("New name of task: ").capitalize()
            if new_task in tasks:
                prompt = input("The new task was found already in tasks, type Q to quit or type R to return to main menu: ").lower()
                if prompt == "q":
                    save_tasks()
                    return
                elif prompt == "r":
                    to_do_list()
                else:
                    print("This answer is not recognized, please retry.")
                    reopen_menu()
            elif new_task not in tasks:    
                tasks.remove(edit_task)
                tasks.append(new_task)
                print(tasks)
                reopen_menu()
    elif edit_task not in tasks:
        prompt = input("Task not recognized, type Q to quit or type R to return to main menu: ").lower()
        if prompt == "q":
            save_tasks()
            return
        elif prompt == "r":
            to_do_list()
        else:
            print("This answer is not recognized, please retry.")
            reopen_menu()

def task_view():
    print(tasks)
    finished = input("These are the tasks in your list. If you are done viewing, type R to return to main menu, or Q to quit.").lower()
    if finished == "r":
        to_do_list()

    elif finished == "q":
        save_tasks()
        return
        
    else:
        prompt = input("Task not recognized, type Q to quit or type R to return to main menu: ").lower()
        if prompt == "q":
            save_tasks()
            return
        elif prompt == "r":
            to_do_list()
        else:
            print("This answer is not recognized, please retry.")
            reopen_menu()    

def quit_list():
    DoubleCheck = input("Are you sure? (Y/N) ").lower()
    if DoubleCheck == "y":
        save_tasks()
        return
    elif DoubleCheck == "n":
        to_do_list()
    
def to_do_list():
    print("Add Task = 1")
    print("Remove Task = 2")
    print("Edit Task = 3")
    print("View Tasks = 4")
    print("Quit = 5")
    choice = input("Choose what you'd like to do (1-5): ")
    
    if choice == "1":
        task_addition()
    elif choice == "2":
        task_removal()
    elif choice == "3":
        task_edit()
    elif choice == "4":
        task_view()
    elif choice == "5":
        quit_list()
    else:
        print("This answer is not recognized, try again!")
        to_do_list()

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

tasks = load_tasks()
to_do_list()    