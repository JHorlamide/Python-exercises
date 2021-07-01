def find_max_number(list_numbers):
    max_num = list_numbers[0]

    for number in list_numbers:
        if number > max_num:
            max_num = number
    return max_num
