from itertools import groupby


def sum_consecutives(s):
    return [sum(list(igroup)) for key, igroup in groupby(s, lambda x: x)]
