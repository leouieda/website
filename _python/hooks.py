"""
Pre-processing of the page metadata before rendering.
"""


def process_info(info, site):
    """
    Alter the page metadata before rendering.
    """
    # Urubu doesn't split the 'tags' into multiple strings
    if 'tags' in info:
        if isinstance(info['tags'], str):
            info['tags'] = info['tags'].split(', ')
    # Identify to which folder the item belongs (paper, blog, etc)
    if 'type' not in info:
        info['type'] = '/{}'.format(info['id'].split('/')[1])
