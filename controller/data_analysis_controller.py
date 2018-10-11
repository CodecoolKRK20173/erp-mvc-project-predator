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
    # ! sign with a position is unfinished function but added in options
    # ??? possible rework of the function

    options = ["Print table",
               "Get game title by id-130",
               "Show the most recently sold game-148",
               "!4.Get the sum of games' prices by their sale id-203",
               "Get the customer's id by the sales id of a game-218",
               "Show ids of all customers-236",
               "Show sale ids of all customers-254(???)",
               "!8.Show the sale numbers of games for each customer-274",
               "Show the owner of a recently sold game-300",
               "Show the owner's id of a recently sold game-316",
               "Show the customer who spent the most and the amount spent-365",
               "Show the customer's id who spent the most and the amount spent-376",
               "Show the most frequent buyers-387",
               "Show the ids of the most frequent buyers-408",
               "Get the customer by id-81"]

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

        elif choice == "9":
            file_name_sales = common.get_input("Choose a file with sales: ")
            file_name_customer = common.get_input("Choose a file with customers: ")
            if file_name_sales == "":
                file_name_sales = file
            if file_name_customer == "":
                file_name_customer = "model/crm/customers.csv"
            table_from_customers = common.get_table_from_file(file_name_customer)
            table_from_sales = common.get_table_from_file(file_name_sales)
            last_buyer = sales.get_the_last_buyer_name(table_from_customers, table_from_sales)
            os.system("clear")
            print("Owner of a recently sold game: ", last_buyer)
            common.waiting()
            os.system("clear")

        elif choice == "10":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            last_buyer_id = sales.get_the_last_buyer_id(table)
            os.system("clear")
            print("Owner's id of a recently sold game: ", last_buyer_id)
            common.waiting()
            os.system("clear")

        elif choice == "11":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            buyer_name_spent_most_and_money = sales.get_the_buyer_name_spent_most_and_the_money_spent(table)
            os.system("clear")
            print("Customer who spent the most and the amount spent: ", buyer_name_spent_most_and_money)
            common.waiting()
            os.system("clear")

        elif choice == "12":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            buyer_id_spent_most_and_money = sales.get_the_buyer_id_spent_most_and_the_money_spent(table)
            os.system("clear")
            print("Customer's id who spent the most and the amount spent: ", buyer_id_spent_most_and_money)
            common.waiting()
            os.system("clear")

        elif choice == "13":
            file_name_sales = common.get_input("Choose a file with sales: ")
            file_name_customer = common.get_input("Choose a file with customers: ")
            if file_name_sales == "":
                file_name_sales = file
            if file_name_customer == "":
                file_name_customer = "model/crm/customers.csv"
            table_from_customers = common.get_table_from_file(file_name_customer)
            table_from_sales = common.get_table_from_file(file_name_sales)
            the_most_frequent_buyers = sales.get_the_most_frequent_buyers_names(table_from_customers,
                                                                                table_from_sales,
                                                                                num=1)
            os.system("clear")
            print("The most frequent buyers: ", the_most_frequent_buyers)
            common.waiting()
            os.system("clear")

        elif choice == "14":
                file_name = common.get_input("Choose a file: ")
                if file_name == "":
                    file_name = file
                table = common.get_table_from_file(file_name)
                the_most_frequent_buyers_ids = sales.get_the_most_frequent_buyers_ids(table, num=1)
                os.system("clear")
                print("ids of the most frequent buyers: ", the_most_frequent_buyers_ids)
                common.waiting()
                os.system("clear")

        elif choice == "15":
            file_name = common.get_input("Choose a file: ")
            if file_name == "":
                file_name = "model/crm/customers.csv"
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            identification = common.get_input("Enter the id: ")
            print(crm.get_name_by_id_from_table(table, identification))
            common.waiting()
            os.system("clear")

        else:
            if choice != "0":
                terminal_view.print_error_message("There is no such choice.")
