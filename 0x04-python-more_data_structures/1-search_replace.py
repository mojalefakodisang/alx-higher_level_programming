#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ Searches an element then replaces it
        Args:
            my_list: input list
            search: element to be searched
            replace: replaces searched element

        Returns:
            returns a list with replaced element
    """
    r_list = []

    if replace == "":
        return my_list
    for contents in my_list:
        if contents == search:
            contents = replace
        r_list.append(contents)

    return r_list
