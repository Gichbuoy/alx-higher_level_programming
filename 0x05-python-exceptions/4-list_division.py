#!/usr/bin/python3
""" function that divides element by element 2 lists"""


def list_division(my_list_1, my_list_2, list_length):
    print_list = []
    for a in range(0, list_length):
        try:
            divide = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("Wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0

        finally:
            print_list.append(divide)
    return (print_list)
