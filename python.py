todo_list = []

def add_task():
  
  new_task = input("Enter a new task: ")
  todo_list.append(new_task)
  print("Task added successfully!")

def view_tasks():
  
  if not todo_list:
    print("There are no tasks in the list.")
  else:
    print("Your To-Do List:")
    for index, task in enumerate(todo_list):
      print(f"{index+1}. {task}")

def update_task():
 
  if not todo_list:
    print("There are no tasks to update.")
    return

  view_tasks() 
  task_index = int(input("Enter the index of the task to update (1-indexed): ")) - 1

  if 0 <= task_index < len(todo_list):
    new_task = input("Enter the updated task: ")
    todo_list[task_index] = new_task
    print("Task updated successfully!")
  else:
    print("Invalid task index. Please try again.")

def main():
 
  while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
      add_task()
    elif choice == '2':
      view_tasks()
    elif choice == '3':
      update_task()
    elif choice == '4':
      print("Exiting the application...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
