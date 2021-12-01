def deepish_copy(source):
    out = dict()
    if source == None:
        return None
    elif type(source) == str:
        return source
    for key, value in source.items():
        try:
            out[key] = value.copy()
        except AttributeError:
            try:
                out[key] = value[:]
            except TypeError:
                out[key] = value
    return out
