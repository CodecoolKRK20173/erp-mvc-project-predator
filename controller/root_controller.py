# everything you'll need is imported:
from view import terminal_view
from controller import store_controller
from controller import hr_controller
from controller import inventory_controller
from controller import accounting_controller
from controller import sales_controller
from controller import crm_controller
from controller import common
#from data_analyser import data_analyser # from controller!!!!!!!!
import os


def run():
    options = ["Store manager",
               "Human resources manager",
               "Inventory manager",
               "Accounting manager",
               "Sales manager",
               "Customer Relationship Management (CRM)",
               "Data Analyzer"]

    os.system("clear")
    terminal_view.print_predator()
    choice = None
    while choice != "0":
        terminal_view.print_menu("What controller would you like to open:", options, "Exit")
        choice = terminal_view.get_choice(options)
        os.system("clear")
        if choice == "1":
            store_controller.run()
        elif choice == "2":
            hr_controller.run()
        elif choice == "3":
            inventory_controller.run()
        elif choice == "4":
            accounting_controller.run()
        elif choice == "5":
            sales_controller.run()
        elif choice == "6":
            crm_controller.run()
        elif option == "7":
            data_analyser.start_module()
        else:
            if choice != "0":
                terminal_view.print_error_message("There is no such choice.")
