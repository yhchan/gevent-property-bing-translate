def parse_properties(filename):
    langs = {}
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            idx = line.find('=')
            if idx == -1:
                continue

            (key, val) = (line[:idx], line[idx + 1:])
            if not key:
                continue

            langs[key] = val

    return langs
