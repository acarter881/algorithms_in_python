def bs_algorithm(s_list, key):
    """'s_list must be a sorted list'"""

    mid = int(len(s_list) / 2)

    print(f'Searching midpoint at {s_list[mid]}')

    if mid == 0:
        print(f'Key of {key} could not be found')
    elif s_list[mid] == key:
        print(f'Found your key: {s_list[mid]}')
    elif s_list[mid] < key:
        print(f'New list is {s_list[mid:len(s_list)]}')
        bs_algorithm(s_list[mid:len(s_list)], key)
    else:
        print(f'New list is {s_list[:mid]}')
        bs_algorithm(s_list[:mid], key)

sorted_list = list(range(1,21))
bs_algorithm(sorted_list, key=7)
