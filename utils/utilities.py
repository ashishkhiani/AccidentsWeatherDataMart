import re

def is_null_or_empty(item):
    if item is None or item.strip() == '':
        return True

    return False


def is_estimated(item):
    if item == 'E':
        return True

    return False


def is_missing_or_unavailable(item):
    if item == 'M' or item == 'NA':
        return True

    return False



