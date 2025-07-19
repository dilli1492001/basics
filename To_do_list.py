tasks=[]
def add_task(task,priority,due_date):
    new_task={
        "task":task,
        "priority":priority,
        "due_date":due_date,
        "complete":False
    }
    tasks.append(new_task)
    print(f"Tasks {tasks} added successfully !\n")
def mark_complete(task_name):
    for task in tasks:
        if task["task"].lower() == task_name.lower():
            task["complete"]=True
            print(f"Task {task_name} marked as complete\n ")
            return
        print(f"Task {task_name} is not found \n")
def remove_task(task_name):
    for task in tasks:
        if task["task"].lower()==task_name.lower():
            tasks.remove(task)
            print(f"task {task_name} removed successfully\n")
        print(f"task {task_name} not found\n")
def view_task():
    if not tasks:
        print("no tasks available")
        return
    print(f"Your Todo list:")
    for index,task in enumerate(tasks,start=1):
        status="complete" if task["complete"] else "pending"
        print(
            f"{index}.Task:{task["task"]}\n Priority:{task["priority"]}\n Due Date: {task["due_date"]} \n Status: {status}\n"
        )
def main():
    while True:
        print("======TODO LIST======")
        print("1.Add_task")
        print("2.Mark a task as complete")
        print("3.Remove task")
        print("4.View all task")
        print("5.Exit")
        chooice =input("enter (1-5): ")
        if chooice == "1":
            task=input("enter the task : ")
            priority=input("enter priority (High/Low/Medium) : ")
            due_date=input("enter due date (dd-mm-yyyy) : ")
            add_task(task,priority,due_date)
        elif chooice=="2":
            task_name=input("enter the task name to mark complete : ")
            mark_complete(task_name)
        elif chooice=="3":
            task_name=input("enter the task name to remove :")
            remove_task(task_name)
        elif chooice=="4":
            view_task()
        elif chooice=="5":
            print("Exit the application ! bye")
            break
        else:
            print("invalid chooice please choose a valid option (1-5) : ")
if __name__=="__main__":
    main()