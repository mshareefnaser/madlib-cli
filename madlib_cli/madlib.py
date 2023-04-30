import re  # regular expression


def read_template(path):
    ''' a function that read file from specific path'''
    with open(path) as file:
        content = file.read()
        return content


def parse_template(content):
    '''
    a function that extract the words between curly braces '{}' inside a string , 
    it returns two arguments:
    srtipped: the string after removing the words
    parts: the words taken from the string
    '''

    pattern = r"\{([^}]+)\}"
    stripped = re.sub(pattern, "{}", content)
    parts = re.findall(pattern, content)
    return stripped, tuple(parts)


def merge(stripped, parts):
    '''
    Merges the given parts into the stripped string by replacing any
    curly-braced placeholders with the corresponding part.
    '''
    return stripped.format(*parts)
