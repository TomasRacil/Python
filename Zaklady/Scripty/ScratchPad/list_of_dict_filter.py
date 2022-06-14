"""
Testing methods of finding dictionaries in list
"""

import timeit

dicts = [
    {"name": "Tom", "age": 10},
    {"name": "Mark", "age": 5},
    {"name": "Pam", "age": 7},
    {"name": "Dick", "age": 12},
    {"name": "Dick", "age": 12},
    {"name": "Pam", "age": 7},
]


def search_loop(name="Pam") -> dict:
    """
    Basic loop

    Args:
        name (str, optional): Item to find. Defaults to "Pam".

    Returns:
        dict: searched dictionary
    """
    for item in dicts:
        if item["name"] == name:
            return item


def search_comp(name="Pam"):
    """
    List comprehension

    Args:
        name (str, optional): Item to find. Defaults to "Pam".

    Returns:
        dict: searched dictionary
    """
    return [item for item in dicts if item["name"] == name][0]


def search_next(name="Pam"):
    """
    Using generators and next

    Args:
        name (str, optional): Item to find. Defaults to "Pam".

    Returns:
        dict: searched dictionary
    """
    return next(item for item in dicts if item["name"] == name)


def search_filter(name="Pam"):
    """
    Using filter method

    Args:
        name (str, optional): Item to find. Defaults to "Pam".

    Returns:
        dict: searched dictionary
    """
    return list(filter(lambda person: person["name"] == name, dicts))[0]


print(
    "Basic loop: ",
    timeit.timeit(
        "searchLoop()", "from __main__ import dicts, search_loop", number=10000
    ),
)
print(
    "List comprehension: ",
    timeit.timeit(
        "searchComp()", "from __main__ import dicts, search_comp", number=10000
    ),
)
print(
    "List generator + next: ",
    timeit.timeit(
        "searchNext()", "from __main__ import dicts, search_next", number=10000
    ),
)
print(
    "Filter method: ",
    timeit.timeit(
        "searchFilter()", "from __main__ import dicts, search_filter", number=10000
    ),
)
