""" Parse properties """


def parse_properties(filename):
    """ Parse properties files into dict """
    langs = {}
    with open(filename, 'r') as fobj:
        lines = [line.strip() for line in fobj.readlines()]
        for line in lines:
            idx = line.find('=')
            if idx == -1:
                continue

            (key, val) = (line[:idx], line[idx + 1:])
            if not key:
                continue

            langs[key] = val

    return langs
