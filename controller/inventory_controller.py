# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
from controller import common
import os


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    title_list = ["* ID",
                  "* Name of item",
                  "* Manufacturer",
                  "* Year of purchase",
                  "* Years it can be used"]

    options = ["Add new record to table",
               "Remove a record with a given id from the table",
               "Update specified record in the table",
               "Items that have not exceeded their durability yet",
               "Average durability for each manufacturer",
               "Print table"]
    os.system('clear')
    file = "model/inventory/inventory.csv"
    choice = None
    while choice != "0":
        terminal_view.print_menu("What do you want to do: ", options, "Back to main menu")
        choice = terminal_view.get_choice(options)
        if choice == "1":
            common.all_add(title_list, file)
        elif choice == "2":
            common.all_remove(title_list, file)
        elif choice == "3":
            common.all_updates(title_list, file)
        elif choice == "4":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            items_with_available_durability = inventory.get_available_items(table)
            os.system("clear")
            print("Items that have not exceeded their durability:\n", items_with_available_durability)
            common.waiting()
            os.system("clear")
        elif choice == "5":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = "model/store/games.csv"
            table = common.get_table_from_file(file_name)
            average_durability = inventory.get_average_durability_by_manufacturers(table)
            os.system("clear")
            print("Average durability times for each manufacturer:\n", average_durability)
            common.waiting()
            os.system("clear")
        elif choice == "6":
            common.all_print_table(title_list, file)

        else:
            if choice != "0":
                terminal_view.print_error_message("There is no such choice.")
