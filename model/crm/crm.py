import os
# User interface module
import terminal_view
# data manager module
import data_manager
# common module
import common


def start_module():
    table = data_manager.get_table_from_file("crm/customers.csv")
    title = "Customer Relationship Management"
    list_options = ["Display Table", "Add to Table", "Remove from Table", "Update Table", "Show ID of longest name",
                    "Show list of E-mail Newsletters"]
    exit_message = "Main Menu"
    while True:
        terminal_view.print_menu(title, list_options, exit_message)
#        option = terminal_view.get_inputs([""], "Please enter a number")
        get_choice()
        if option[0] == "1":
            show_table(table)
        elif option[0] == "2":
            table = add(table)
        elif option[0] == "3":
            id_ = terminal_view.get_inputs(["ID:"], "Please, type ID You want to remove")
            table = remove(table, id_)
        elif option[0] == "4":
            id_ = terminal_view.get_inputs(["ID: "], "Please, type ID You want to update")
            table = update(table, id_)
        elif option[0] == "5":
            terminal_view.print_result(get_longest_name_id(table), "The ID with longest name is: ")
        elif option[0] == "6":
            terminal_view.print_result(get_subscribed_emails(table), "People with e-mail subscriptions are: ")
        elif option[0] == "0":
            break
        else:
            terminal_view.print_error_message("There is no such option.")




def show_table(table):

    os.system("clear")
    title_list = ["ID", "Name", "E-Mail", "Newsletter"]

    terminal_view.print_table(table, title_list)

def add(table):

    check = True
    while check:

        list_labels = ["Name", "E-Mail", "Newsletter"]
#        new_item = terminal_view.get_inputs(list_labels, "Please provide your personal information")
    add()
        validation = common.validate_data(list_labels, new_item)
        if not validation:
            terminal_view.print_error_message("Input not valid.\n")
            continue
        new_item.insert(0, common.generate_random(table))
        table.append(new_item)
        what_to_do = terminal_view.get_inputs([""], "Press 0 or exit or 1 to add record.")
        if what_to_do[0] == "0":
            check = False
            os.system("clear")
        os.system("clear")
        show_table(table)
    data_manager.write_table_to_file("crm/customers.csv", table)

    return table


def remove(table, id_):

    check = True
    while check:

        table_dict = common.creat_dict_from_table(table)
        if id_[0] in list(table_dict.keys()):
            del table_dict[id_[0]]
            table = list(table_dict.values())
            data_manager.write_table_to_file("crm/customers.csv", table)
#            what_to_do = terminal_view.get_inputs([""], "Press 0 or exit or 1 to remove another information.")
            if what_to_do[0] == '0':
                check = False
                os.system("clear")
            else:
                os.system("clear")
                show_table(table)
#                id_ = terminal_view.get_inputs(["Please, type ID to remove: "], "\n")
        else:
            terminal_view.print_error_message("There is no such element.")
            what_to_do = terminal_view.get_inputs([""], "Press 0 or exit or 1 to try one more time.")
            if what_to_do[0] == '0':
                check = False
                os.system("clear")
            else:
                os.system("clear")
                show_table(table)
                id_ = terminal_view.get_inputs(['Please, type ID to remove: '], "\n")
    return table


def update(table, id_):

    check = True
    while check:
        table_dict = common.creat_dict_from_table(table)

        if id_[0] in list(table_dict.keys()):
            list_labels = ["Name", "E-Mail", "Newsletter"]
#            updated_item = terminal_view.get_inputs(list_labels, "Please, provide customer information")
            validation = common.validate_data(list_labels, updated_item)
            if not validation:
#                terminal_view.print_error_message("Input not valid.\n")
                continue
            updated_item.insert(0, id_[0])
            table_dict[id_[0]] = updated_item
            table = list(table_dict.values())
            data_manager.write_table_to_file("crm/customers.csv", table)
            os.system("clear")
            what_to_do = terminal_view.get_inputs([""], "Press 0 or exit or 1 to update another information.")
            if what_to_do[0] == '0':
                check = False
                os.system("clear")
            else:
                os.system("clear")
                show_table(table)
#                id_ = terminal_view.get_inputs(["Please type ID to update: "], "\n")
        else:
            terminal_view.print_error_message("There is no such element.")
#            what_to_do = terminal_view.get_inputs([""], "Press 0 or exit or 1 to try one more time.")
            if what_to_do[0] == '0':
                check = False
                os.system("clear")
            else:
                os.system("clear")
                show_table(table)
#                id_ = terminal_view.get_inputs(["Please, type ID to update: "], "\n")
    return table

def get_longest_name_id(table):

    name = table[0][1]
    character = str(table[0][1][0]).lower()
    for element in table:
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

def get_subscribed_emails(table):

    subs_mail = []
    for line in table:
        if line[-1] == "1":
            subs_mail.append(str(line[2] + ";" + line[1]))
        else:
            continue
    os.system("clear")
    return subs_mail
