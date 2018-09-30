# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
from controller import common


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
               "Get closest person to average year in file"]

    title_list = ["*id", "person", "year"]
    choice = None
    while choice != "0":
        terminal_view.print_menu("What do you want to do:", options, "Back to main menu")
        choice = terminal_view.get_choice(options)
        if choice == "1":
            file_name = input("Choose a file")
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            record = terminal_view.get_inputs(title_list, "Enter data")
            table = hr.add(table, record)
            common.write_table_to_file(file_name, table)
        elif choice == "2":
            file_name = input("Choose a file")
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            id_ = input("get id to removed")
            table = hr.remove(table, id_)
            common.write_table_to_file(file_name, table)
            terminal_view.print_table(table, title_list)
        elif choice == "3":
            file_name = input("Choose a file")
            table = common.get_table_from_file(file_name)
            hr.update(table, id_, record)
        elif choice == "4":
            file_name = input("Choose a file")
            table = common.get_table_from_file(file_name)
            hr.get_oldest_person(table)
        elif choice == "5":
            file_name = input("Choose a file")
            table = common.get_table_from_file(file_name)
            hr.get_persons_closest_to_average(table)

        else:
            if choice != "0":
                terminal_view.print_error_message("There is no such choice.")
