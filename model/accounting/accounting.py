""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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

    table = table[:int(id_)] + table[int(id_)+1:]

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

    table = table[:int(id_)] + [record] + table[int(id_)+1:]

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    list_with_income = []
    list_with_outflow = []
    dict_years_income = {}
    dict_years_outflow = {}
    dict_profit = {}

    for element in table:
        year = int(element[-3])
        amount = int(element[-1])
        for income in element:
            if income == "in" not in list_with_income:
                list_with_income.append([year, amount])
        for outflow in element:
            if outflow == "out" not in list_with_outflow:
                list_with_outflow.append([year, amount])

    for year, income in list_with_income:
        sum_of_income = dict_years_income.get(year, 0) + income
        dict_years_income[year] = sum_of_income

    for year, outflow in list_with_outflow:
        sum_of_outflow = dict_years_outflow.get(year, 0) + outflow
        dict_years_outflow[year] = sum_of_outflow

        for year, amount in dict_years_income.items():
            dict_profit[year] = amount - dict_years_outflow.get(year, 0)

        year_highest_profit = 0
        for year, profit in dict_profit.items():
            if year_highest_profit < profit:
                year_highest_profit = profit
                year_highest_profit_key = year

    return year_highest_profit_key


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    list_with_income = []
    list_with_outflow = []
    dict_years_income = {}
    dict_years_outflow = {}
    dict_profit = {}

    for element in table:
        year0 = int(element[-3])
        amount = int(element[-1])
        for income in element:
            if income == "in" not in list_with_income:
                list_with_income.append([year0, amount])
        for outflow in element:
            if outflow == "out" not in list_with_outflow:
                list_with_outflow.append([year0, amount])

    for year0, income in list_with_income:
        sum_of_income = dict_years_income.get(year0, 0) + income
        dict_years_income[year0] = sum_of_income

    for year0, outflow in list_with_outflow:
        sum_of_outflow = dict_years_outflow.get(year0, 0) + outflow
        dict_years_outflow[year0] = sum_of_outflow

        for year0, amount in dict_years_income.items():
            dict_profit[year0] = amount - dict_years_outflow.get(year0, 0)

    counter_of_items = 0
    for year1 in dict_profit:
        for year2 in table:
            if year1 == int(year2[-3]):
                counter_of_items += 1
        dict_profit[year1] = dict_profit[year1] / counter_of_items
        counter_of_items = 0

    return dict_profit[year]
