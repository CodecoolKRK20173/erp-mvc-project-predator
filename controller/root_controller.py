# Do not modify this file
# run this program (the ERP software) from the terminal from thd root directory of this project


import sys
from view import ui  # User Interface
# Store module
from controller import store_controller
# Human Resources module
from controller import hr_controller
# Tool manager module
from controller import inventory_controller
# Accounting module
from controller import accounting_controller
# Sales module
from controller import sales_controller
# Customer Relationship Management (CRM) module
from controller import crm_controller


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        store_controller.run()
    elif option == "2":
        hr_controller.run()
    elif option == "3":
        inventory_controller.run()
    elif option == "4":
        accounting_controller.run()
    elif option == "5":
        sales_controller.run()
    elif option == "6":
        crm_controller.run()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Store manager",
               "Human resources manager",
               "Inventory manager",
               "Accounting manager",
               "Sales manager",
               "Customer Relationship Management (CRM)"]

    ui.print_menu("Main menu", options, "Exit program")

def run():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))
