""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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

    table = table[:int(id_)] + [record] +table[int(id_)+1:]

    return table


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """
    
    available_durability = []
    all_data_with_available_durability = []
    for element in table:
        year_from_table = int(element[-2])
        durability_from_table = int(element[-1])
        sum_durability = year_from_table + durability_from_table
        if sum_durability >= 2017:
            available_durability.append(element)
            for digit in available_durability:
                digit[-2] = int(digit[-2])
                digit[-1] = int(digit[-1])
    return available_durability


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """
    list_of_manufacture_durability = []
    dict_of_manufacture_sum_durability = {}

    for element in table:
        manufacturer = element[-3]
        durability = int(element[-1])
        if manufacturer not in list_of_manufacture_durability:
            list_of_manufacture_durability.append([manufacturer, durability])
            
    for manufacturer, durability in list_of_manufacture_durability:
        if manufacturer in dict_of_manufacture_sum_durability:
            dict_of_manufacture_sum_durability[manufacturer] += durability
        else:
            dict_of_manufacture_sum_durability[manufacturer] = durability
    
    counter_of_manufacturers = 0

    for manufacturer1 in dict_of_manufacture_sum_durability:
        for manufacturer2 in list_of_manufacture_durability:
            if manufacturer1 == manufacturer2[0]:
                counter_of_manufacturers += 1
        dict_of_manufacture_sum_durability[manufacturer1] = dict_of_manufacture_sum_durability[manufacturer1] / counter_of_manufacturers
        counter_of_manufacturers = 0
    return dict_of_manufacture_sum_durability

