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
# ------------------
table = [['kH34Ju#&', 'Joe Empty', '1976'], 
['jH34Ju#&', 'Barbara Streisand', '1950'], 
['tH34Ju#&', 'Jimmy Hendrix', '1972'],
['eH34Ju#&', 'Joey Tribbiani', '1950'], 
['bH34Ju#&', 'Steve Black', '1982'], 
['vH34Ju#&', 'James Brown', '1976'], 
['kH14Ju#&', 'Evelin Smile', '1950'],
['kH35Ju#&', 'Kevin Spacey', '1990'], 
['kH38Ju#&', 'Leonardo DiCaprio', '1999'],
['kH94Ju#&', 'Joe Dirt', '1986']]

def get_oldest_person(table):
    max_year = 0
    for line in table:
        if max_year < int(line[2]):
            max_year = int(line[2])      
    return max_year 
    
print(get_oldest_person(table))

def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?
    Args:
        table (list): data table to work on
    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

