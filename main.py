from utils import get_option
from utils import get_filename, load_file

def menu():
    print("1. Load File")
    print("2. Print Stats")
    print("3. Delete Athlete")
    print("4. Save File")
    print("5. Athlete Info")
    print("6. Display Chart")
    print("7. Exit")

menu()
option = get_option()

while option != 7:
    if option == 1:
        filename = get_filename()
        athletes = load_file(filename)
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        pass
    elif option == 6:
        pass
    elif option is None:
        pass  # skip this round due to bad input
    else:
        print("Invalid option. Please try again.")
    
    menu()
    option = get_option()
