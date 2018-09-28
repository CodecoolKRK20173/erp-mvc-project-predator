# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
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
    "* name",
    "* email",
    "* subscribed",]

    options = ["Add new record to table",
               "Remove a record with a given id from the table",
               "Update specified record in the table",
               "ID of the customer with the longest name",
               "Customers that have subscribed to the newsletter",
               "Print table"]
    os.system('clear')
    file = "model/crm/customers.csv"
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
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            id_with_longest_name = crm.get_longest_name_id(table)
            os.system("clear")
            print("ID of the customer with the longest name: " , id_with_longest_name)
            common.waiting()
            os.system("clear")
        elif choice == "5":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            subscribed_mails = crm.get_subscribed_emails(table)
            os.system("clear")
            print("Customers that have subscribed to the newsletter: " ,subscribed_mails)
            common.waiting()
            os.system("clear")
        elif choice == "6":
            common.all_print_table(title_list,file)
        else:
            terminal_view.print_error_message("There is no such choice.")

