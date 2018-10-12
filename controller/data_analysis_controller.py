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

    # ! sign with a position is unfinished function but added in options
    # !8. Show the sale numbers of games for each customer-292
    # !11. Show the customer who spent the most and the amount spent-365"
    # !12. Show the customer's id who spent the most and the amount spent-376"
    # !13. Show the most frequent buyers-387
    # !14. Show the if of the most freuent buyers-

    options = ["Print table",
               "Get game title by id",
               "Show the most recently sold game",
               "Get the sum of games' prices by their id",
               "Get the customer's id by the id of a game",
               "Show ids of all customers who purchased games",
               "Show sale ids of all customers",
               "Show the sale numbers of games for each customer",
               "Show the owner of a recently sold game",
               "Show the owner's id of a recently sold game",
               "Show the customer who spent the most and the amount spent",
               "Show the customer's id who spent the most and the amount spent",
               "Show the most frequent buyers",
               "Show the ids of the most frequent buyers",
               "Get the customer by id"]

    os.system('clear')
    file = "model/sales/sales.csv"
    choice = None
    while choice != "0":
        os.system('clear')
        terminal_view.print_predator()
        terminal_view.print_menu("What do you want to do:", options, "Back to main menu")
        choice = terminal_view.get_choice(options)

        if choice == "1":
            os.system("clear")
            common.all_print_table(title_list, file)

        elif choice == "2":
            os.system("clear")
            file_name = common.get_file()
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            identification = common.get_input("Enter the id: ")
            print(sales.get_title_by_id_from_table(table, identification))
            common.waiting()
            os.system("clear")

        elif choice == "3":
            file_name = common.get_file()
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            most_recently_sold_game = sales.get_item_id_title_sold_last(table)
            print("The most recently sold game is: ")
            terminal_view.print_table([most_recently_sold_game], ["* id", "* title"])
            common.waiting()
            os.system("clear")

        elif choice == "4":
            os.system("clear")
            file_name = common.get_file()
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            item_ids = []
            x = True
            while x:
                add_id = common.get_input("Enter the id or 'x' to exit: ")
                if add_id == "x":
                    x = False
                item_ids.append(add_id)
            print(sales.get_the_sum_of_prices_from_table(table, item_ids))
            common.waiting()
            os.system("clear")

        elif choice == "5":
            os.system("clear")
            file_name = common.get_file()
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, title_list)
            sale_id = common.get_input("Enter the id of a game: ")
            print(sales.get_customer_id_by_sale_id_from_table(table, sale_id))
            common.waiting()
            os.system("clear")

        elif choice == "6":
            file_name = common.get_file()
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            ids_of_all_customers = sales.get_all_customer_ids_from_table(table)
            print("ids of all customers who purchased games:\n", ids_of_all_customers)
            common.waiting()
            os.system("clear")

        elif choice == "7":
            file_name = common.get_file()
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            sale_ids_of_all_customers = sales.get_all_sales_ids_for_customer_ids_form_table(table)
            print("Sale ids of all customers:\n\n", sale_ids_of_all_customers)
            common.waiting()
            os.system("clear")

        elif choice == "8":
            file_name = common.get_file()
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            num_of_sales_per_customer = sales.get_num_of_sales_per_customer_ids_from_table(table)
            print("Sale numbers of games for each customer: ", num_of_sales_per_customer)
            common.waiting()
            os.system("clear")

        elif choice == "9":
            file_name_sales = common.get_input("Choose a file with sales: ")
            if file_name_sales == "":
                file_name_sales = file
            file_name_customer = common.get_input("Choose a file with customers: ")
            if file_name_customer == "":
                file_name_customer = "model/crm/customers.csv"
            table_from_customers = common.get_table_from_file(file_name_customer)
            table_from_sales = common.get_table_from_file(file_name_sales)
            last_buyer = sales.get_the_last_buyer_name(table_from_customers, table_from_sales)
            print("Owner of a recently sold game: ", last_buyer)
            common.waiting()
            os.system("clear")

        elif choice == "10":
            file_name = common.get_file()
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            last_buyer_id = sales.get_the_last_buyer_id(table)
            print("Owner's id of a recently sold game: ", last_buyer_id)
            common.waiting()
            os.system("clear")

        elif choice == "11":
            os.system("clear")
            file_name = common.get_file()
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            buyer_name_spent_most_and_money = sales.get_the_buyer_name_spent_most_and_the_money_spent(table)
            print("Customer who spent the most and the amount spent:\n")
            terminal_view.print_table([buyer_name_spent_most_and_money], ["* customer", "* money"])
            common.waiting()
            os.system("clear")

        elif choice == "12":
            file_name = common.get_file()
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            buyer_id_spent_most_and_money = sales.get_the_buyer_id_spent_most_and_the_money_spent(table)
            print("Customer's id who spent the most and the amount spent:\n", buyer_id_spent_most_and_money)
            common.waiting()
            os.system("clear")

        elif choice == "13":
            file_name_sales = common.get_input("Choose a file with sales: ")
            if file_name_sales == "":
                file_name_sales = file
            file_name_customer = common.get_input("Choose a file with customers: ")
            if file_name_customer == "":
                file_name_customer = "model/crm/customers.csv"
            table_from_customers = common.get_table_from_file(file_name_customer)
            table_from_sales = common.get_table_from_file(file_name_sales)
            the_most_frequent_buyers = sales.get_the_most_frequent_buyers_names(table_from_customers,
                                                                                table_from_sales,
                                                                                num=1)
            print("The most frequent buyers:\n", the_most_frequent_buyers)
            common.waiting()
            os.system("clear")

        elif choice == "14":
            file_name = common.get_file()
            if file_name == "":
                file_name = file
            table = common.get_table_from_file(file_name)
            the_most_frequent_buyers_ids = sales.get_the_most_frequent_buyers_ids(table, num=1)
            print("ids of the most frequent buyers:\n", the_most_frequent_buyers_ids)
            common.waiting()
            os.system("clear")

        elif choice == "15":
            os.system("clear")
            file_name = common.get_file()
            if file_name == "":
                file_name = "model/crm/customers.csv"
            table = common.get_table_from_file(file_name)
            terminal_view.print_table(table, ["* id", "* name", "* email", "* subscribed"])
            identification = common.get_input("Enter the id: ")
            print(crm.get_name_by_id_from_table(table, identification))
            common.waiting()
            os.system("clear")

        else:
            if choice != "0":
                terminal_view.print_error_message("There is no such choice.\n")
                common.waiting()
