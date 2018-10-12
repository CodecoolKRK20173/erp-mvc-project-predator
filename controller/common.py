""" Common functions for controllers
implement commonly used functions here
"""
import os
from view import terminal_view


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


def all_print_table(title_list, file):
    file_name = get_input("Choose a file: ")
    if file_name == "":
        file_name = file
    table = get_table_from_file(file_name)
    terminal_view.print_table(table, title_list)
    waiting()
    os.system("clear")


def all_add(title_list, file):
    file_name = get_input("Choose a file: ")
    if file_name == "":
        file_name = file
    table = get_table_from_file(file_name)
    terminal_view.print_table(table, title_list)
    record = terminal_view.get_inputs(title_list, "Enter data: ")
    table = add(table, record)
    write_table_to_file(file_name, table)
    os.system("clear")
    terminal_view.gprint('*** Record has been added ***')
    waiting()
    os.system("clear")


def all_remove(title_list, file):
    file_name = get_input("Choose a file: ")
    if file_name == "":
        file_name = file
    table = get_table_from_file(file_name)
    terminal_view.print_table(table, title_list)
    id_ = get_input("Enter id of a record you want to remove: ")
    table = remove(table, id_)
    write_table_to_file(file_name, table)
    os.system("clear")
    terminal_view.gprint('*** Record has been removed ***')
    waiting()
    os.system("clear")


def all_updates(title_list, file):
    file_name = get_input("Choose a file: ")
    if file_name == "":
        file_name = file
    table = get_table_from_file(file_name)
    terminal_view.print_table(table, title_list)
    id_ = get_input("Enter id to update: ")
    record = terminal_view.get_inputs(title_list, "Enter data: ")
    table = update(table, id_, record)
    write_table_to_file(file_name, table)
    os.system("clear")
    terminal_view.gprint('*** Record has been updated ***')
    waiting()
    os.system("clear")


def write_table_to_file(file_name, table):
    """
    Writes list of lists into a csv file.

    Args:
        file_name (str): name of file to write to
        table (list): list of lists to write to a file

    Returns:
         None
    """
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


def waiting():
    input()


def get_table_from_file(file_name):
    """
    Reads csv file and returns it as a list of lists.
    Lines are rows columns are separated by ";"

    Args:
        file_name (str): name of file to read

    Returns:
         list: List of lists read from a file.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


def get_input(title):
    inp = input(title)
    return inp


def get_file():
    file_exists = True
    while file_exists:
        try:
            inp = input("Choose file: ")
            if inp == "":
                return inp
            with open(inp, "r") as file:
                pass
            return inp
        except FileNotFoundError:
            print("There is no such file")
