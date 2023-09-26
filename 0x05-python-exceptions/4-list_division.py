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
        except (TypeError, ValueError):
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by zero")
        except IndexError:
            result = 0
            print("out of range")
        except Exception:
            result = 0
        finally:
            new_list.append(result)
    return new_list
