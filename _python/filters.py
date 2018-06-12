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
        ids = []
        for tag in page['tags']:
            content = site['reflinks']['/tag/{}'.format(tag)]['content']
            ids.extend([page['id'] for page in content])
        # Use the set to remove any duplicates (pages that share more than 1
        # tag with this one)
        related = [site['reflinks'][i] for i in set(ids)]
        related = remove(related, [page['id']])
    return related


def pages(site, ids):
    """
    Select only the pages with the given ids from the site.
    """
    return [site['reflinks'][i] for i in ids]


def tagnames(site):
    """
    Get a list of all tags (just the names) from the site.
    """
    return [tag['title'] for tag in site['reflinks']['/tag']['content']]


filters = dict(
    shuffle=shuffle,
    remove=remove,
    related=related,
    pages=pages,
    tagnames=tagnames,
)
