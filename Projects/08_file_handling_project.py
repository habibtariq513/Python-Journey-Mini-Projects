import os
from pathlib import Path # For file path manipulations

# Function to display current directory files and folders
def file_folder_path():
    print("\nFile and Folder Path Manipulations...")
    path = Path('') 
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i + 1}: {items}")


# ===================================== File creation function ========================================
def create_file():
    try:
        file_folder_path()
        print("\nCreating a file...")
        file_name = input("Enter file name: ") 
        p = Path(file_name)

        if not p.exists():
            content = input("Enter file content: ")
            with open(p, "w") as f:
                f.write(content)
                f.seek(0)    
            print("FILE CREATED SUCCESSFULLY.")
        else: 
            print("OOPS! File already exists.")
    except Exception as err:
        print(f"An Error occurres as {err}")


# ===================================== File Reading function ========================================
def read_file():
    try:
        file_folder_path()
        print("\nReading a file...")
        file_name = input("Enter file name: ") 
        p = Path(file_name)

        if p.exists() and p.is_file():
            with open(file_name, "r") as f:
                print(f"\n\"{f.read()}\"")
            print("\nFILE READED SUCCESSFULLY.")
        else: 
            print("OOPS! File does NOT exist.")

    except Exception as err:
        print(f"An Error occurres as {err}")


# ===================================== File Updation function ========================================
def update_file():
    try:
        file_folder_path()
        print("\nUpdating a file...")
        file_name = input("Enter file name: ") 
        p = Path(file_name)

        if p.exists() and p.is_file():
            choice = 0
            while choice != 4:
                print("\n1. Update The File Name")
                print("2. Append Content To The File")
                print("3. Overwriting the previous content")
                print("4. Exit")

                choice = int(input("Enter your Choice: "))
                if choice == 1:                                             # For File Renaming
                    new_name = input("Enter New Name: ") 
                    file_name = new_name
                    p.rename(new_name)
                    print("\nFILE RENAMED SUCCESSFULLY.")
                
                elif choice == 2:                                             # For Data Appending
                    with open(file_name, "a") as f:
                        data = input("Enter data to appened: ")
                        f.write(data)
                        f.seek(0)
                    print("\nDATA APPENDED SUCCESSFULLY.")

                elif choice == 3:                                             # For File Overwriting
                    with open(file_name, "r+") as f:
                        data = input("Enter data to overwrite: ")
                        f.write(data)
                        f.seek(0)
                    print("\nDATA OVERWRITTEN SUCCESSFULLY.")
                
                elif choice == 4:
                    break
                
                else:
                    print("Invalid choice. Please try again.")            
        else: 
            print("OOPS! File does NOT exist.")
    except Exception as err:
        print(f"An Error occurres as {err}")


# ===================================== File Deletion function ========================================
def delete_file():
    # file_folder_path()
    # print("\nDeleting a file...")
    # file_name = input("Enter file name: ")
    # os.remove(file_name)
    try:
        file_folder_path()
        print("\nDeleting a file...")
        file_name = input("Enter file name: ") 
        p = Path(file_name)

        if p.exists() and p.is_file():
            os.remove(file_name)
            print("FILE DELETED SUCCESSFULLY.")
        else: 
            print("OOPS! File does NOT exist.")
    except Exception as err:
        print(f"An Error occurres as {err}")


# Menu function
def menu():
    print("\n================= File Management System =================")
    print("1. Create File")
    print("2. Read File")
    print("3. Update File")
    print("4. Delete File")
    print("5. Exit")
    

# Main loop
c = 0
while c != 5:
    menu()
    c = int(input("Enter your choice: "))
    if c == 1:
        create_file()
    elif c == 2:
        read_file()
    elif c == 3:
        update_file()
    elif c == 4:
        delete_file()
    elif c == 5:
        print("Thanks For Using ME")
        exit()
    else:
        print("Invalid choice. Please try again.")
