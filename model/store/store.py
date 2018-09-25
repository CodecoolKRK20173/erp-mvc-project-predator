""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""
'''
# everything you'll need is imported:
from model import data_manager
from model import common
'''

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

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    table = [['kH34Ju#&', 'Age of Empires II: The Age of Kings', 'Ensemble Studios', '32', '32'], ['jH34Ju#&', 'Age of Mythology', 'Ensemble Studios', '40', '4'], ['tH34Ju#&', 'Age of Empires II: The Conquerors', 'Ensemble Studios', '30', '3'], ['eH34Ju#&', 'Astebreed', 'Edelweiss', '25', '5'], ['bH34Ju#&', "Age of Wonders II: The Wizard's Throne", 'Triumph Studios', '20', '10'], ['vH34Ju#&', 'AudioSurf', 'Dylan Fitterer', '23', '1']]
    dictionary = {}
    for record in table :
        dictionary[record[2]] = dictionary.get(record[2], 0) + 1
    return dictionary
print(get_counts_by_manufacturers('table'))


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
