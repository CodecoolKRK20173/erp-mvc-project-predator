# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
from controller import common
import os


def run():
    """
Uruchamia ten moduł i wyświetla jego menu.
     * Użytkownik ma tutaj dostęp do domyślnych funkcji specjalnych.
     * Użytkownik może wrócić do głównego menu.

    Zwroty:
        Żaden
    """

    options = ["Add new record to table",
               "Remove a record",
               "Update a record",
               "Get oldest person in file",
               "Get closest person to average year in file",
               "Print table"]

    title_list = ["*id", "person", "year"]
    os.system('clear')
    file = "model/hr/persons.csv"
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
            oldest_person = hr.get_oldest_person(table)
            os.system("clear")
            print("The oldest persons in the file: ", oldest_person)
            common.waiting()
            os.system("clear")
        elif choice == "5":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            closest_to_average = hr.get_persons_closest_to_average(table)
            os.system("clear")
            print("Closest person to average year is:", closest_to_average)
            common.waiting()
            os.system("clear")
        elif choice == "6":
            common.all_print_table(title_list, file)

        else:
            if choice != "0":
                terminal_view.print_error_message("There is no such choice.")
