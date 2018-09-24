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

def get_choice(options):
    ui.print_menu("Main menu",options, "Exit program")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    return inputs[0]


def run():
    options = ["Store manager",
               "Human resources manager",
               "Inventory manager",
               "Accounting manager",
               "Sales manager",
               "Customer Relationship Management (CRM)"]

    choice = None
    while choice != "0":
        choice = get_choice(options)
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
        else:
            ui.print_error_message("There is no such choice.")
