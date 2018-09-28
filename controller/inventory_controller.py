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

    title_list = ["* id",
    "* Name of item",
    "* manufacturer",
    "* purchase_year",
    "* durability"]

    options = ["Add new record to table",
               "Remove a record with a given id from the table",
               "Updates specified record in the table",
               "Question: Which items have not exceeded their durability yet?",
               "Question: What are the average durability times for each manufacturer?",
               "Print table"]
    os.system('clear')
    file = "model/inventory/inventory.csv"
    choice = None
    while choice != "0":
        terminal_view.print_menu("What do you want to do:",options,"Back to main menu")
        choice = terminal_view.get_choice(options)
        if choice == "1":
            common.all_add(title_list,file)
        elif choice == "2":
            common.all_remove(title_list,file)
        elif choice == "3":
            common.all_updates(title_list,file)
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            common.all_print_table(title_list,file)
        else:
            terminal_view.print_error_message("There is no such choice.")
