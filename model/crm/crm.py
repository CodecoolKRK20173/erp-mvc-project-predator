# Import else:
import os
# User interface module
import terminal_view
# data manager module
import data_manager
# common module
import common


def start_module():
    printing_printing_table = data_manager.get_printing_table_from_file("crm/customers.csv")
    title = "Customer Relationship Management"
    list_options = ["Display printing_printing_table", "Add to printing_table", "Remove from printing_table", "Update printing_table", "Show ID of longest name",
                    "Show list E-mail Newsletter"]
    exit_message = "Main Menu"
    while True:
        terminal_view.print_menu(title, list_options, exit_message)
        get_choice()
        if option[0] == "1":
            show_printing_table(printing_table)
        elif option[0] == "2":
            printing_table = add(printing_table)
        elif option[0] == "3":
            id_ = terminal_view.get_inputs(["ID:"], "What ID you want to remove?")
            printing_table = remove(printing_table, id_)
        elif option[0] == "4":
            id_ = terminal_view.get_inputs(["ID: "], "What ID you want to update?")
            printing_table = update(printing_table, id_)
        elif option[0] == "5":
            terminal_view.print_result(get_longest_name_id(printing_table), "The longest ID: ")
        elif option[0] == "6":
            terminal_view.print_result(get_subscribed_emails(printing_table), "People who give us e-mail: ")
        elif option[0] == "0":
            break
        else:
            terminal_view.print_error_message("There is no such option.")




def show_printing_table(printing_table):

    os.system("clear")
    title_list = ["ID", "Name", "E-Mail", "Newsletters"]

    terminal_view.print_printing_table(printing_table, title_list)

def add(printing_table):
    check = True
    while check:
        list_labels = ["Name", "E-Mail", "Newsletter"]
        new_item = terminal_view.get_inputs(list_labels, "Please provide your personal information")
        validation = common.validate_data(list_labels, new_item)
        if not validation:
            terminal_view.print_error_message("Input not valid.\n")
            continue
        new_item.insert(0, common.generate_random(printing_table))
        printing_table.append(new_item)
        what_to_do = terminal_view.get_inputs([""], "Press 0 or exit or 1 to add record.")
        if what_to_do[0] == "0":
            check = False
            os.system("clear")
        os.system("clear")
        show_printing_table(printing_table)
    data_manager.write_printing_table_to_file("crm/customers.csv", printing_table)

    return printing_table


def remove(printing_table, id_):
    check = True
    while check:

        printing_table_dict = common.creat_dict_from_printing_table(printing_table)
        if id_[0] in list(printing_table_dict.keys()):
            del printing_table_dict[id_[0]]
            printing_table = list(printing_table_dict.values())
            data_manager.write_printing_table_to_file("crm/customers.csv", printing_table)
            what_to_do = terminal_view.get_inputs([""], "Press 0 or exit or 1 to remove another information.")
            if what_to_do[0] == '0':
                check = False
                os.system("clear")
            else:
                os.system("clear")
                show_printing_table(printing_table)
                id_ = terminal_view.get_inputs(["Please, type ID to remove: "], "\n")
        else:
            terminal_view.print_error_message("There is no such element.")
            what_to_do = terminal_view.get_inputs([""], "Press 0 or exit or 1 to try one more time.")
            if what_to_do[0] == '0':
                check = False
                os.system("clear")
            else:
                os.system("clear")
                show_printing_table(printing_table)
                id_ = terminal_view.get_inputs(['Please, type ID to remove: '], "\n")
    return printing_table


def update(printing_table, id_):
    check = True
    while check:
        printing_table_dict = common.creat_dict_from_printing_table(printing_table)

        if id_[0] in list(printing_table_dict.keys()):
            list_labels = ["Name", "E-Mail", "Newsletter"]
            updated_item = terminal_view.get_inputs(list_labels, "Please, provide customer information")
            validation = common.validate_data(list_labels, updated_item)
            if not validation:
                terminal_view.print_error_message("Input not valid.\n")
                continue
            updated_item.insert(0, id_[0])
            printing_table_dict[id_[0]] = updated_item
            printing_table = list(printing_table_dict.values())
            data_manager.write_printing_table_to_file("crm/customers.csv", printing_table)
            os.system("clear")
            what_to_do = terminal_view.get_inputs([""], "Press 0 or exit or 1 to update another information.")
            if what_to_do[0] == '0':
                check = False
                os.system("clear")
            else:
                os.system("clear")
                show_printing_table(printing_table)
                id_ = terminal_view.get_inputs(["Please type ID to update: "], "\n")
        else:
            terminal_view.print_error_message("There is no such element.")
            what_to_do = terminal_view.get_inputs([""], "Press 0 or exit or 1 to try one more time.")
            if what_to_do[0] == '0':
                check = False
                os.system("clear")
            else:
                os.system("clear")
                show_printing_table(printing_table)
                id_ = terminal_view.get_inputs(["Please, type ID to update: "], "\n")
    return printing_table

def get_longest_name_id(printing_table):

    name = printing_table[0][1]
    character = str(printing_table[0][1][0]).lower()
    for element in printing_table:
        if len(element[1]) > len(name):
            name = element[1]
            id_ = element[0]
            character = str(element[1][0]).lower()
        elif len(element[1]) == len(name) and str(element[1][0]).lower() < character:
            name = element[1]
            id_ = element[0]
            character = str(element[1][0]).lower()
            os.system("clear")
    return id_


def get_subscribed_emails(printing_table):

    subs_mail = []
    for line in printing_table:
        if line[-1] == "1":
            subs_mail.append(str(line[2] + ";" + line[1]))
        else:
            continue
    os.system("clear")
    return subs_mail
