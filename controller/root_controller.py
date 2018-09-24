# everything you'll need is imported:
from view import ui
from controller import store_controller
from controller import hr_controller
from controller import inventory_controller
from controller import accounting_controller
from controller import sales_controller
from controller import crm_controller
from controller import common

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
