from utils import lib


while True:
    lib.display_menu()
    choice = input("Enter a choice:")
    if choice == "1":
        lib.add_contact()
    elif choice == "2":
        lib.view_contact()
    elif choice == "3":
        lib.edit_contact()
    elif choice == "4":
        lib.delete_contact()
    elif choice == "5":
        lib.list_all_contacts()
    elif choice == "6":
        lib.close_db()
        print("Program kapatılıyor...")
        break
    else:
        print("Invalid choice. Please try again.")

    
