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


def related(page, site):
    """
    Make a list of related pages that share the same tags.
    """
    related = []
    if 'tags' in page:
        for tag in page['tags']:
            related.extend(site['reflinks']['/tag/{}'.format(tag)]['content'])
        related = remove(related, [page['id']])
    return related


filters = dict(
    shuffle=shuffle,
    remove=remove,
    related=related,
)
