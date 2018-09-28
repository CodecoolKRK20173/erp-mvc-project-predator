# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
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

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    title_list = ["* id",
    "* Month of the transaction",
    "* Day of the transaction",
    "* Year of the transaction",
    "* type",
    "* amount"]

    options = ["Add new record to table",
               "Remove a record with a given id from the table",
               "Updates specified record in the table",
               "Question: Which year has the highest profit?",
               "Question: What is the average (per item) profit in a given year?",
               "Print table"]
    os.system('clear')
    file = "model/accounting/items.csv"
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
