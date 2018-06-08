"""
Define jinja filters.
"""
import random

def shuffle(seq):
    """
    Shuffle the given sequence if it can be turned into a list
    """
    try:
        randomized = list(seq)
        random.shuffle(randomized)
        return randomized
    except:
        return seq


def remove(seq, ids):
    """
    Remove a list of items with the given id attributes from the list.
    """
    return [item for item in seq if item['id'] not in ids]


filters = dict(
    shuffle=shuffle,
    remove=remove,
)
