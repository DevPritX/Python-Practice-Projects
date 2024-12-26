# Todo App
import json

# Features

def load_data():
    try:
        with open("Task_list.txt", "r") as file:
            data = file.read()
            if len(data) < 1:
                return []
            return json.loads(data)
    except FileNotFoundError:
        return []

# List Tasks Method
def list_all_tasks(data_list):
    if len(data_list) == 1:
        print("\n"+"*"*20)
        print("1 Task:")
    elif len(data_list) > 1:
        print("\n"+"*"*20)
        print(f"{len(data_list)} Tasks:")
    else:
        print("\nNo Tasks Found ! Add new Task...")
    for index, item in enumerate(data_list, start=1):
        print(f"{index}. {item["task"].capitalize()} {item["status"].capitalize()}")
    print("*"*20)
# Add Task Method
def add_task(data_list):
    with open("Task_list.txt", "w") as file:
        json.dump(data_list, file)
        print("\nTask Added Successfully")

# Update Task Method
def mark_complete_task(data_list, id):
    data_list[id-1]["status"] = "done"
    with open("Task_list.txt", "w") as file:
        json.dump(data_list, file)
        print("\nTask marked as Completed")

# Remove Task Method
def remove_task(data_list, id):
    data_list.pop(id-1)
    with open("Task_list.txt", "w") as file:
        json.dump(data_list, file)
        print("\nTask removed Successfully")

# Display Operations
def display_operations():
    print("\n"+"-"*10)
    print("1. To Get List of All Tasks: list")
    print("2. To Add New Task: add (Todo Name / Description)")
    print("3. To Delete a Task: remove (Todo ID)")
    print("4. To Mark as Completed: done (Todo ID)")
    print("-"*10)

def main():
    print(f"\nWelcome To Todo App \n{"-"*20}")
    print("Using This App You can Manage and Keep Track of your Daily Tasks...")
    task_list = load_data()
    tasks_len = len(task_list)

    while True:
        display_operations()
        user_input = input("\n$: ").lower().strip().split()
        if len(user_input) > 0:
            operation = user_input.pop(0)
            task = " ".join(user_input)

            match operation:
                case "add":
                    task_list.append({"task": task, "status": "pending"})
                    add_task(task_list)
                case "remove":
                    id = int(task.strip().split()[0])
                    if tasks_len > 0 and id > 0:
                        remove_task(task_list, id)
                    else:
                        print("\nTask Not Found !")
                case "list":
                    list_all_tasks(task_list)
                case "done":
                    id = int(task.strip().split()[0])
                    if tasks_len > 0 and id > 0:
                        mark_complete_task(task_list, id)
                    else:
                        print("\nTask Not Found !")
                case "exit":
                    print("\nGood Bye !!\n"+"-"*20+"\n")
                    exit()
                case _:
                    print("Sorry, This is a Invalid Operation !")
        else:
            continue

if __name__ == "__main__":
    main()