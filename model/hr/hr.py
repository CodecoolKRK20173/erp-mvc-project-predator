""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
#from model import data_manager
#from model import common



def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    

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



def get_oldest_person(table):
    max_year = 0
    for line in table:
        if max_year < int(line[2]):
            max_year = int(line[2])      
    return max_year 
    


def get_persons_closest_to_average(table):
    latest_n = 100000
    nearest_year = 0
    n = 10000#n
    number_of_year = 0   
    year_sum = 0
    for line in table:
        year_sum =year_sum + int(line[2])
        number_of_year +=1
        average_year = year_sum/number_of_year
    for line in table:
        n = average_year -int(line[2])
        if n < 0:
            n = n * (-1)
        if latest_n > n:
            latest_n = n
            nearest_number = int(line[2]) 
    for line in table:
        if int(line[2]) == nearest_number:
            return line[1]

