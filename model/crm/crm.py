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

    # your code

    table = table[:int(id_)] + [record] +table[int(id_)+1:]

    return table


# special functions:
# ------------------

def get_longest_name_id(table):

    # your code

    longest_name_number_of_id = len(max(table, key=lambda x: len(x[1]))[1])
    longest = []
    for item in table:
        if len(item[1]) == longest_name_number_of_id:
            longest.append([item[0], item[1]])
    first = min(longest, key=lambda x: x[1])[0]
    #ui.print_result(first, "ID of the person with the longest name?")
    return first


# the question: Which customers has newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code
    name_of_subscribers = []
    for line in table:
        if line[3] == "1":
            name_of_subscribers.extend([line[2] + ";" + line[1]])
    #terminal_view.print_result(name_of_subscribers, "subscribers:")
    return name_of_subscribers
