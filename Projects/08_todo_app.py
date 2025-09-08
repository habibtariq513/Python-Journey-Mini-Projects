tasks = [] 

# ============================================= Menu =============================================
def menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Tasks")
    print("4. Remove Task")
    print("5. Exit")

# ============================================= View Tasks =============================================
def view_task():    
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")

# ============================================= Add Tasks =============================================
def add_task():
    try:
        task_name = input("\nAdd Task: ")
        tasks.append(task_name)
        print(f"        Task added        ")
        
    except Exception as err:
        print(f"Error Occurred due to {err}")

    print("\n========= Current Tasks =========")
    view_task()

# ============================================= Remove Tasks =============================================
def rem_task():
    if not tasks:
        print("******* There is NO Task *******")
        return
    else:
        print("\n========= All Tasks =========")
        view_task()

        try:
            task_number = int(input("\nAdd Task Number that you want to Remove: "))
            
            if 0 < task_number <= len(tasks):
                tasks.pop(task_number - 1)
                print(f"\n        Task '{task_number}' removed        ")
                
                print("\n========= Current Tasks =========")
                view_task()
            else: 
                print("*** Sorry!! Enter Valid Task Number ***")
                rem_task()

        except Exception as err:
            print(f"Error Occurred due to {err}")

# ============================================= Update Tasks =============================================
def update_task():
    if not tasks:
        print("******* There is NO Task *******")
        return
    else:
        print("\n========= All Tasks =========")
        view_task()

        try:
            task_number = int(input("\nEnter Task Number that you want to Update: "))

            if 0 < task_number <= len(tasks):
                updated_task = input("Update Your Task: ")
                tasks[task_number - 1] = updated_task
                print(f"\n        Task '{task_number}' Updated        ")
                
                print("\n========= Tasks After Updation =========")
                view_task()
            else: 
                print("*** Sorry!! Enter Valid Task Number ***")
                update_task()
        
        except Exception as err:
            print(f"Error Occurred due to {err}")
        

# ============================================= Main =============================================        
while True:
    menu()
    try:
        choice = int(input("Choose an option (1-5): "))
        if choice == 1:
            add_task()
        elif choice == 2:
            if not tasks:
                print("******* There is NO Task *******")
                continue
            else:
                print("\n========= All Tasks =========")
            view_task()
        elif choice == 3:
            update_task()
        elif choice == 4:
            rem_task()
        elif choice == 5:
            print("\nExiting the To-Do List App.")
            exit()
        else:
            print("Invalid choice. Please select a valid option b/w (1 - 5).")
    
    except Exception as err:
        print(f"Error Occurred due to {err}")