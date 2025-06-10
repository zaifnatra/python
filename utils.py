def get_option():
    try:
        option = int(input("Choose an option: "))
        return option
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_option()


