# everything you'll need is imported:
from model.store import store
from view import terminal_view
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

    options = ["Add new record to table",
               "Remove a record with a given id from the table",
               "Update specified record in the table",
               "Number of different kinds of game that are available of each manufacturer",
               "Average amount of games in stock of a given manufacturer",
               "Print table"]

    title_list = ["*id",
    "* title",
    "* manufacturer",
    "* price",
    "* in_stock"]
    os.system('clear')
    choice = None
    while choice != "0":
        terminal_view.print_menu("What do you want to do:",options,"Back to main menu")
        choice = terminal_view.get_choice(options)
        os.system('clear')
        if choice == "1":
        #   to jest dzialajacy plik               model/store/games.csv
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = "model/store/games.csv"
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            record = terminal_view.get_inputs(title_list, "Enter data: ")
            table = store.add(table, record)
            common.write_table_to_file(file_name, table)
            os.system("clear")
            terminal_view.gprint('*** Record has been added ***')
            common.waiting()
            os.system("clear")
        elif choice == "2":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = "model/store/games.csv"
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            id_ = common.get_input("Get id to removed: ")
            table = store.remove(table, id_)
            common.write_table_to_file(file_name, table)
            os.system("clear")
            terminal_view.gprint('*** Record has been removed ***')
            common.waiting()
            os.system("clear")
        elif choice == "3":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = "model/store/games.csv"
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            id_ = common.get_input("Enter id to update: ")
            record = terminal_view.get_inputs(title_list, "Enter data: ")
            table = store.update(table, id_, record)
            common.write_table_to_file(file_name, table)
            os.system("clear")
            terminal_view.gprint('*** Record has been updated ***')
            common.waiting()
            os.system("clear")
        elif choice == "4":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = "model/store/games.csv"
            table = common.get_table_from_file(file_name)
            dictionary = store.get_counts_by_manufacturers(table)
            terminal_view.print_dictionary("Number of different kinds of game that are available of each manufacturer:", dictionary)
            common.waiting()
            os.system("clear")
        elif choice == "5":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = "model/store/games.csv"
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            manufacturer = common.get_input("Enter a manufacturer: ")
            print(store.get_average_by_manufacturer(table, manufacturer))
            common.waiting()
            os.system("clear")
        elif choice == "6":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = "model/store/games.csv"
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            common.waiting()
            os.system("clear")

        else:
            if choice != "0":
                terminal_view.print_error_message("There is no such choice.")
