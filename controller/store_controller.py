# everything you'll need is imported:
from model.store import store
from view import terminal_view
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    options = ["Add new record to table",
               "Remove a record with a given id from the table",
               "Updates specified record in the table",
               "Question: How many different kinds of game are available of each manufacturer?",
               "Question: What is the average amount of games in stock of a given manufacturer",
               "back to main menu"]


    choice = None
    while choice != "0":
        terminal_view.print_menu("What do you want do:",options,"to back to main menu enter 0")
        choice = terminal_view.get_choice(options)
        if choice == "1":
            file_name = get_input("Choose a file")
            table = common.get_table_from_file(file_name)
            store.add(table, record)
        elif choice == "2":
            file_name = get_input("Choose a file")
            table = common.get_table_from_file(file_name)
            store.remove(table, id_)
        elif choice == "3":
            file_name = get_input("Choose a file")
            table = common.get_table_from_file(file_name)
            store.update(table, id_, record)
        elif choice == "4":
            file_name = get_input("Choose a file")
            table = common.get_table_from_file(file_name)
            store.get_counts_by_manufacturers(table)
        elif choice == "5":
            file_name = get_input("Choose a file")
            table = common.get_table_from_file(file_name)
            store.get_average_by_manufacturer(table, manufacturer)

        else:
            terminal_view.print_error_message("There is no such choice.")
