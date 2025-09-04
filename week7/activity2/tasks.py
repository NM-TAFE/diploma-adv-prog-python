'''
A buggy Task Manager that provides an opportunity to debug code by both reasoning about it and stepping through
The program has a number of bugs that are introduced one at a time. 
The goal is to find and fix the bugs.
Ensure you step through this program in pdb only to understand how the program works and to find the bugs.
'''

# Once debugged add some documentation examples to help the next programmer!
import sys
import pdb
# import os

def add_task(tasks, task):
    pdb.set_trace()
    tasks.append((task, False))

def mark_task_completed(tasks, index):
    breakpoint()
    if 0 <= index < len(tasks):
        tasks[index] = True 
    else:
        print("Invalid task index.")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.remove(tasks[index]) 
    else:
        print("Invalid task index.")

def list_tasks(tasks):
    # pdb.set_trace()
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks):
        print(f"{index}. {'[X]' if task else '[ ]'} {task[0]}") 

def sort_tasks(tasks):
    # pdb.set_trace()
    tasks.sort(key=lambda task: x[1])

def binary_search(tasks, target):
    # pdb.set_trace()
    sort_tasks(tasks)
    low, high = 0, len(tasks) - 1
    while low <= high:
        mid = (low + high)
        if tasks[mid][0] == target:
            return mid
        elif tasks[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    pdb.set_trace()
    tasks = []

    while True:
        print("\n1. Add Task")
        print("2. Mark Task Completed")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Sort Tasks")
        print("6. Search Task")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            add_task(tasks, task)
        elif choice == "2":
            pdb.set_trace()
            index = int(input("Enter task index to mark as completed: "))
            mark_task_completed(tasks, index)
        elif choice == "3":
            index = int(input("Enter task index to delete: "))
            delete_task(tasks)
        elif choice == "4":
            list_tasks(tasks)
        elif choice == "5":
            sort_tasks(tasks)
            print("Tasks sorted.")
        elif choice == "6":
            target = input("Enter task description to search: ")
            index = binary_search(tasks, target)
            if index != -1:
                print(f"Task '{target}' found at index {index}.")
            else:
                print(f"Task '{target}' not found.")
        elif choice == "7":
            sys.exit("Exiting program.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
