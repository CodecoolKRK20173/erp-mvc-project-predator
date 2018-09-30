def get_choice(options):
    x = input("Enter a number:  ")
    return x


def gprint(a):
    print(a)


def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """

    column_width = list()

    for i, title in enumerate(title_list):
        column_width.append(len(title))

    for items in table:
        for i, item in enumerate(items):
            try:
                if column_width[i] < len(str(item)):
                    column_width[i] = len(str(item))
            except:
                column_width.append(len(item))

    table_size = 1
    for dash in column_width:
        table_size += (dash + 3)

    print('/', ('-' * (table_size-2)), '\\', sep='')

    for i, title in enumerate(title_list):
        if i == 0:
            print('|', end="")
        print(' {:{width}} |'.format(title, width=column_width[i]), end="")

    print('\n' + '|' + ('-' * (table_size-2)) + '|')

    for items in table:
        for i, item in enumerate(items):
            if i == 0:
                print('|', end="")
            print(' {:{width}} |'.format(str(item).replace('\|\|/', ';'), width=column_width[i]), end="")
        print()

    print('\\' + ('-' * (table_size-2)) + '/')


def print_result(result, label=""):
    print("\n" + label)
    if type(result) == list:
        print("")
        for element in result:
            print(element)
        print("")
    elif type(result) == dict:
        for key, value in result.items():
            print(key, value)
        print("")
    else:
        print(result)
        print("")


def print_dictionary(title, dictionary):
    print(title + ':')
    i = 1
    for key in dictionary:
        print('\t', key, ' :', dictionary[key])
        i = i + 1


def print_menu(title, list_options, exit_message):
    print(title + ':')
    i = 1
    for element in list_options:
        print('\t' + str([i]) + ' ' + element)
        i += 1
    print('\t[0] ' + exit_message)


def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for element in list_labels:
        x = input(element + ": ")
        inputs.append(x)
    return inputs


def print_error_message(message):
    print("\n" + message)


def print_predator():
    print('''
                            888        888
                            888        888
                            888        888
88888b. 888d888 .d88b.  .d88888 8888b. 888888 .d88b. 888d888
888 "88b888P"  d8P  Y8bd88" 888    "88b888   d88""88b888P"
888  888888    88888888888  888.d888888888   888  888888
888 d88P888    Y8b.    Y88b 888888  888Y88b. Y88..88P888
88888P" 888     "Y8888  "Y88888"Y888888 "Y888 "Y88P" 888
888
888
888

''')
