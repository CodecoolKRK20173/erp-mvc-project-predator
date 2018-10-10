# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from model.sales import sales
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

    title_list = ["* id of item",
                  "* title",
                  "* price",
                  "* month of the sale",
                  "* day of the sale",
                  "* year of the sale",
                  "* customer's id"]
    # number at the end is a line in the model
    # ! sign is unfinished function but added in options
    # ??? possible rework of the function
    # number from the start is the number of the unfinished yet option
    options = ["Print table",
               "Show game title by id-130",
               "Show the most recently sold game-148",
               "!4.Get the sum of games' prices by their sale id-203",
               "Get the customer's id by the sales id of a game-218",
               "Show ids of all customers-236",
               "Show sale ids of all customers-254(???)",
               "!8.Show the sale numbers of games for each customer-274",
               "9.Show the owner of a recently sold game-290",
               "10.Show the owner's id of a recently sold game-306",
               "11.Show the customer who spent the most and the amount spent-355",
               "12.Show the customer's id who spent the most and the amount spent-366",
               "13.Show the most frequent buyers-377",
               "14.Show the most frequent buyers' ids-398",
               "15. file from crm here"]

    os.system('clear')
    file = "model/sales/sales.csv"
    choice = None
    while choice != "0":
        terminal_view.print_menu("What do you want to do:", options, "Back to main menu")
        choice = terminal_view.get_choice(options)

        if choice == "1":
            common.all_print_table(title_list, file)

        elif choice == "2":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            identification = common.get_input("Enter the id: ")
            print(sales.get_title_by_id_from_table(table, identification))
            common.waiting()
            os.system("clear")

        elif choice == "3":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            most_recently_sold_game = sales.get_item_id_title_sold_last(table)
            os.system("clear")
            print("The most recently sold game is: ", most_recently_sold_game)
            common.waiting()
            os.system("clear")

        elif choice == "4":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            item_ids = common.get_input("Enter the id: ")
            print(sales.get_the_sum_of_prices_from_table(table, item_ids))
            common.waiting()
            os.system("clear")

        elif choice == "5":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            item_ids = common.get_input("Enter the sale id: ")
            print(sales.get_customer_id_by_sale_id_from_table(table, sale_id))
            common.waiting()
            os.system("clear")

        elif choice == "6":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            ids_of_all_customers = sales.get_all_customer_ids_from_table(table)
            os.system("clear")
            print("ids of all customers: ", ids_of_all_customers)
            common.waiting()
            os.system("clear")

        elif choice == "7":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            sale_ids_of_all_customers = sales.get_all_sales_ids_for_customer_ids_form_table(table)
            os.system("clear")
            print("Sale ids of all customers: ", sale_ids_of_all_customers)
            common.waiting()
            os.system("clear")

        elif choice == "8":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            num_of_sales_per_customer = sales.get_num_of_sales_per_customer_ids_from_table(table)
            os.system("clear")
            print("Sale numbers of games for each customer: ", num_of_sales_per_customer)
            common.waiting()
            os.system("clear")

        else:
            if choice != "0":
                terminal_view.print_error_message("There is no such choice.")
