""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
"""

# everything you'll need is imported:
from model import data_manager
from model import common


def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    table = table + [record]
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    for a in range(0, len(table)):
        if id_ == table[a][0]:
            table = table[:a] + table[a+1:]
            return table


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """

    for a in range(0, len(table)):
        if id_ == table[a][0]:
            table[a] = record
    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    lowest_price = 10000000
    item = ''
    for i in table:
        if int(i[2]) < lowest_price:
            lowest_price = int(i[2])
            item = i[0]
    return item


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
    table_year = []
    for i in table:
        if int(i[5]) > year_from and int(i[5]) < year_to:
            table_year = table_year + [i]
    table_month = []
    for i in table_year:
        if int(i[3]) > month_from and int(i[3]) < month_to:
            table_month = table_month + [i]
    table_day = []
    for i in table_month:
        if int(i[4]) > day_from and int(i[4]) < day_to:
            table_day = table_day + [i]

    return table_day


# functions supports data abalyser
# --------------------------------


def get_title_by_id_from_table(table, identification):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """
    for element in table:
        title = element[1]
        if identification == element[0]:
            return title


def get_item_id_title_sold_last(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    if not table:
        return None

    latest_year = int(table[0][-2])
    for game in table[1:]:
        youngest_year = int(game[-2])
        if youngest_year > latest_year:
            latest_year = youngest_year

    greatest_year_games = []
    for game in table:
        identity = game[0]
        title = game[1]
        if int(game[-2]) == latest_year:
            greatest_year_games.append(game)

    latest_month = int(greatest_year_games[0][-4])
    for game in greatest_year_games[1:]:
        youngest_month = int(game[-4])
        if youngest_month > latest_month:
            latest_month = youngest_month

    greatest_month_games = []
    for game in greatest_year_games:
        identity = game[0]
        title = game[1]
        if int(game[-4]) == latest_month:
            greatest_month_games.append(game)

    latest_day = int(greatest_month_games[0][-3])
    for game in greatest_month_games[1:]:
        youngest_day = int(game[-3])
        if youngest_day > latest_day:
            latest_day = youngest_day

    greatest_day_games = []
    for game in greatest_month_games:
        identity = game[0]
        title = game[1]
        if int(game[-3]) == latest_day:
            greatest_day_games.append(game)
            return identity, title


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    sum_price = []
    for element in table:
        #product_id = element[0]
        product_id = 'kH34Ju#&'
        item_id = element[0]  
        if product_id in item_id:
            item_price = int(element[2])
            sum_price.append(item_price)
            result =  sum(sum_price)
            
    return result


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    for element in table:
        customer_id = element[-1]
        if sale_id == element[0]:
            return customer_id


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """
    all_customers_id = []
    for element in table:
        single_customer_id = element[-1]
        if single_customer_id not in all_customers_id:
            all_customers_id.append(single_customer_id)

    return all_customers_id


def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """
    all_sales_id = []
    for element in table:
        single_sales_id = element[0]
        if single_sales_id not in all_sales_id:
            all_sales_id.append(single_sales_id)
    return all_sales_id


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code

# ----------------- from data_analyzer --------------------


def get_the_last_buyer_name(table_from_customers, table_from_sales):
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    identity_from_sales = get_the_last_buyer_id(table_from_sales)
    for customer in table_from_customers:
        identity_from_customers = customer[0]
        name = customer[1]
        if identity_from_sales == identity_from_customers:
            return name


def get_the_last_buyer_id(table):
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    if not table:
        return None

    latest_year = int(table[0][-2])
    for game in table[1:]:
        youngest_year = int(game[-2])
        if youngest_year > latest_year:
            latest_year = youngest_year

    greatest_year_games = []
    for game in table:
        identity = game[-1]
        if int(game[-2]) == latest_year:
            greatest_year_games.append(game)

    latest_month = int(greatest_year_games[0][-4])
    for game in greatest_year_games[1:]:
        youngest_month = int(game[-4])
        if youngest_month > latest_month:
            latest_month = youngest_month

    greatest_month_games = []
    for game in greatest_year_games:
        identity = game[-1]
        if int(game[-4]) == latest_month:
            greatest_month_games.append(game)

    latest_day = int(greatest_month_games[0][-3])
    for game in greatest_month_games[1:]:
        youngest_day = int(game[-3])
        if youngest_day > latest_day:
            latest_day = youngest_day

    greatest_day_games = []
    for game in greatest_month_games:
        identity = game[-1]
        if int(game[-3]) == latest_day:
            greatest_day_games.append(game)
            return identity


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    # your code


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    # your code


def get_the_most_frequent_buyers_names(table_from_customers, table_from_sales, num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    list_of_id_and_number_sales = get_the_most_frequent_buyers_ids(table_from_sales, num)
    for i in range(0, len(list_of_id_and_number_sales)):
        for w in table_from_customers:
            if w[0] == list_of_id_and_number_sales[i][0]:
                list_of_id_and_number_sales[i] = (w[1], list_of_id_and_number_sales[i][1])
    return list_of_id_and_number_sales


def get_the_most_frequent_buyers_ids(table, num=1):  # table from sales

    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """
    list_of_buyers = []
    for i in table:
        for w in list_of_buyers:
            if i[-1] == w:
                continue
                list_of_buyers = list_of_buyers + [i[-1]]
    for i in range(0, len(list_of_buyers)):
        n = 0
        for w in table:
            if list_of_buyers[i] == w[1]:
                n = n + 1
        list_of_buyers[i] = (list_of_buyers, n)
    return list_of_buyers
