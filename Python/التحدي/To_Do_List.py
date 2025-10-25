
def main() :
    message = """
       1-add task
       2-mark task he is complete
       3-view tasks
       4-quit """

    global tasks
    
    tasks = []

    while True :
        print (message)
        choice = input("Enter your choice :")

        if choice =="1" :
            add_task()
        elif choice =="2" :
            mark_task()
        elif choice =="3" :
            view_task()
        elif choice =="4" : 
            quit()
        else :
            print("your choice is false enter number enter 1 and 4")


def add_task() :
    enter = input("enter your task : ")
    status = {"task":enter , "completed":False}
    tasks.append(status)
    print("add task he is succes")
    print("-"*30)

def mark_task() :
    #get list to task incompeted 
    incompleted_task = []
    for task in tasks :
        if task["completed"] == False :
            incompleted_task.append(task)
    if len(incompleted_task) == 0 :
        print("i am sorry but add task !!")
        return
    # view task
    for i , task in enumerate(incompleted_task) :
        n = i + 1
        print(f"{n} - {task['task']}")
    print("-"*30)
    # choice 
    
    choice_nomber = int(input("choice in task for completed"))
    
    incompleted_task[choice_nomber - 1]["completed"] = True
   
def view_task() :

    if len(tasks) == 0 :
        print ("i don't have a task add")
        return
    
    print("-"*30)
    for i , task in enumerate(tasks) :
        if task["completed"] == True :
            j = "✔"
        else :
            j = "❌"
        n = i + 1
        print(f"{n} - {task['task']} : {j}")
    print("-"*30)

main()

