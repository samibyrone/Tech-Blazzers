
def sequence_separated_number():

    numbers = input("Enter your comma-separated numbers: ")

    display_list = numbers.split(",")
    tuple_display_list = tuple(display_list)

    return display_list, tuple_display_list

    print(display_list)
    print(tuple_display_list)

