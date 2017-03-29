"""
Define jinja filters.
"""
import random

def shuffle(seq):
    try:
        randomized = list(seq)
        random.shuffle(randomized)
        return randomized
    except:
        return seq


filters = dict(
    shuffle=shuffle,
)
