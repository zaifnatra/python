def get_option():
    try:
        option = int(input("Choose an option: "))
        return option
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_option()

def get_filename():
    filename = input("Enter the filename: ").strip()
    if not filename:
        print("Filename cannot be empty. Please try again.")
        return get_filename()
    return filename

