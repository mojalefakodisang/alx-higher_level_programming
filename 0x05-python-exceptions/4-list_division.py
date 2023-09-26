#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ Divides element by element 2 lists

        Args:
            my_list_1: list 1
            my_list_2: list 2
            list_length: length of resultant list

        Return:
            returns a new list, with length list_length
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except ZeroDivisionError:
            print("division by zero")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            pass
    return new_list
