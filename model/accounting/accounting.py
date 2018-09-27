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
    # your code

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

    # your code

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

    # your code

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
            year = int(element[-3])
            income = int(element[-1])
            sum_of_income = dict_years_income.get(year, 0) + income
            dict_years_income[year] = sum_of_income

        for year, outflow in list_with_income:
            year = int(element[-3])
            outflow = int(element[-1])
            sum_of_outflow = dict_years_income.get(year, 0) + outflow
            dict_years_outflow[year] = sum_of_outflow

        for year, amount in dict_years_income.items():
            dict_profit[year] = amount - dict_years_outflow.get(year, 0)

        year_highest_profit = 0  # -float("inf")
        for year in dict_profit:
            if year_highest_profit > dict_profit[year]:  # <
                year_highest_profit = dict_profit[year]
                year_highest_profit = year
    
    return year_highest_profit


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
