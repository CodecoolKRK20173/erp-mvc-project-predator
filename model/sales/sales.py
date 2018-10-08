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
'''
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

    record_between_year = []
    for i in table:
        if i[5] >= year_from and i[5] <= year_to:
            record_between_year += [i]
    record_between_month = []
    for i in table:
        if i[4] >= month_from and i[4] <= month_to:
            record_between_month += [i]
    record_between_days = []
    for i in table:
        if i[3] >= day_from and i[3] <= day_to:
            record_between_days += [i]

    for i in range(0, len(record_between_days) - 1):
        for j in range(i + 1, len(record_between_days)):
            if record_between_days[i] > record_between_days[j]:
                temp = record_between_days[i]
                record_between_days[i] = record_between_days[j]
                record_between_days[j] = temp
    print(record_between_days)



return list
sort_abc(table)



'''


def change_sign_to_number(sign):
    if sign == '1':
        sign = 1
    elif sign == '2':
        sign = 2
    elif sign == '3':
        sign = 3
    elif sign == '4':
        sign = 4
    elif sign == '5':
        sign = 5
    elif sign == '6':
        sign = 6
    elif sign == '7':
        sign = 7
    elif sign == '8':
        sign = 8
    elif sign == '9':
        sign = 9
    elif sign == '0':
        sign = 0
    elif sign == 'a':
        sign = 10
    elif sign == 'b':
        sign = 11
    elif sign == 'c':
        sign = 12
    elif sign == 'd':
        sign = 13
    elif sign == 'e':
        sign = 14
    elif sign == 'f':
        sign = 15
    elif sign == 'g':
        sign = 16
    elif sign == 'h':
        sign = 17
    elif sign == 'i':
        sign = 18
    elif sign == 'j':
        sign = 19
    elif sign == 'k':
        sign = 20
    elif sign == 'l':
        sign = 21
    elif sign == 'm':
        sign = 22
    elif sign == 'n':
        sign = 23
    elif sign == 'o':
        sign = 24
    elif sign == 'p':
        sign = 25
    elif sign == 'q':
        sign = 26
    elif sign == 'r':
        sign = 27
    elif sign == 's':
        sign = 28
    elif sign == 't':
        sign = 29
    elif sign == 'u':
        sign = 30
    elif sign == 'w':
        sign = 31
    elif sign == 'x':
        sign = 32
    elif sign == 'y':
        sign = 33
    elif sign == 'z':
        sign = 34
    else:
        sign = 35
    return sign


def comparison(word_1, word_2):   # jesli false to slowa sa ulozone w porzadku alfabetycznym
    if_change = False               # jesli true trzeba zamienic
    n = 0

    try:
        while word_1[n] == word_2[n]:
            n = n + 1
    except:
        if len(word_1) < len(word_2):
            return False
        else:
            return True
    nr_1 = change_sign_to_number(word_1[n])
    nr_2 = change_sign_to_number(word_2[n])
    if nr_2 < nr_1:
        if_change = True
    return if_change


def do_line_string(table):
    new_table = []
    for i in table:
        new_table = new_table + [i[0]+'\t'+i[1]+'\t'+i[2]+'\t'+i[3]+'\t'+i[4]]
    return new_table


def sort_abc(table):
    new_table = []
    for k in table:
        new_table = new_table + [k[0] + [k[1].lower()] + k[2:]]
    for i in range(0, len(new_table)-1):
        for w in range(i+1, len(new_table)):
            if comparison(new_table[i][1], new_table[w][1]):
                t = table[i]
                table[i] = table[w]
                table[w] = t
                t = new_table[i]
                new_table[i] = new_table[w]
                new_table[w] = t
#    new_table = []
#    for k in table:
#        new_table = new_table + [k[1]]
    return table
