def show_list_menu(title, options):
    print(title)
    for index, option in enumerate(options):
        print(f"\t{index + 1}. {option}")
    print()
    selected_option = int(input("Enter the number of the option: ")) - 1
    return selected_option
