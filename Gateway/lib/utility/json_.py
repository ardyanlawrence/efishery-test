from json import dumps, load, loads

from iotera.utility.object import is_basestring, is_dict, is_int, is_list, is_none, is_type_equals, is_tuple


def parse(input_, fallback=None):
    f = None
    if is_dict(fallback):
        f = fallback

    if is_dict(input_):
        return input_
    elif not is_basestring(input_):
        return f

    try:
        res = loads(input_)
        if is_dict(res):
            return res

        return f

    except:
        return f


def parse_array(input_, fallback=None):
    f = None
    if is_list(fallback):
        f = fallback

    if is_list(input_):
        return input_
    elif not is_basestring(input_):
        return f

    try:
        res = loads(input_)
        if is_list(res):
            return res

        return f

    except:
        return f


def parse_any(input_, fallback=None):
    f = None
    if is_dict(fallback) or is_list(fallback):
        f = fallback

    j = parse(input_)
    if j is None:
        j = parse_array(input_)
        if j is None:
            return f
    return j


def parse_from_file(input_):
    return load(input_)


def stringify(obj):
    return dumps(obj)


def stringify_compact(obj):
    return dumps(obj, separators=(',', ':'))


def stringify_formatted(obj):
    return dumps(obj, indent=2, separators=(',', ': '))


# TODO ignore null
def stringify_ignore_null(obj):
    return dumps(obj)


def is_empty(obj):
    if is_dict(obj):
        return not obj
    elif is_list(obj):
        return len(obj) == 0
    else:
        return True


def has(obj, key):
    if is_dict(obj) and is_basestring(key):
        return key in obj
    elif is_list(obj) and is_int(key) and key >= 0:
        return len(obj) > key
    elif is_tuple(obj) and is_int(key) and key >= 0:
        return len(obj) > key
    else:
        return False


def del_(obj, key):
    if has(obj, key):
        del obj[key]


def safe_get(obj, key_input, fallback=None):
    if has(obj, key_input):
        return obj[key_input]

    elif not is_none(obj) and is_list(key_input):
        if len(key_input) == 0:
            return obj

        key = key_input[0]
        if has(obj, key):
            return safe_get(obj[key], key_input[1:], fallback)

    return fallback


def safe_deep_get(obj, key_input, fallback=None):
    return safe_get(obj, key_input, fallback)


def safe_get_with_type(obj, key_input, fallback=None):
    if has(obj, key_input):
        value = obj[key_input]
        if not is_none(fallback):
            if not is_type_equals(value, fallback):
                return fallback
        return value

    elif not is_none(obj) and is_list(key_input):
        if len(key_input) == 0:
            if not is_none(fallback):
                if not is_type_equals(obj, fallback):
                    return fallback
            return obj

        key = key_input[0]
        if has(obj, key):
            return safe_get_with_type(obj[key], key_input[1:], fallback)

    return fallback


def safe_deep_get_with_type(obj, key_input, fallback=None):
    return safe_get_with_type(obj, key_input, fallback)


def safe_set(obj, key_input, val):
    if is_dict(obj) and is_basestring(key_input):
        if key_input in obj:
            value = obj[key_input]
            if is_type_equals(value, val):
                obj[key_input] = val
        else:
            obj[key_input] = val

    elif is_list(obj) and is_int(key_input) and key_input >= 0:
        if len(obj) > key_input:
            value = obj[key_input]
            if is_type_equals(value, val):
                obj[key_input] = val
        else:
            obj.append(val)

    elif not is_none(obj) and is_list(key_input) and len(key_input) > 0:
        key = key_input[0]
        if len(key_input) == 1:
            if is_dict(obj) and is_basestring(key):
                if key in obj:
                    value = obj[key]
                    if is_type_equals(value, val):
                        obj[key] = val
                else:
                    obj[key] = val
            elif is_list(obj) and is_int(key) and key >= 0:
                if len(obj) > key:
                    value = obj[key]
                    if is_type_equals(value, val):
                        obj[key] = val
                else:
                    obj.append(val)
        else:
            if is_dict(obj) and is_basestring(key):
                if key in obj:
                    safe_set(obj[key], key_input[1:], val)
                else:
                    next_key = key_input[1]
                    if is_basestring(next_key):
                        obj[key] = dict()
                        safe_set(obj[key], key_input[1:], val)
                    elif is_int(next_key):
                        obj[key] = list()
                        safe_set(obj[key], key_input[1:], val)
            elif is_list(obj) and is_int(key) and key >= 0:
                if len(obj) > key:
                    safe_set(obj[key], key_input[1:], val)
                else:
                    next_key = key_input[1]
                    if is_basestring(next_key):
                        value = dict()
                        obj.append(value)
                        safe_set(value, key_input[1:], val)
                    elif is_int(next_key):
                        value = list()
                        obj.append(value)
                        safe_set(value, key_input[1:], val)


def safe_deep_set(obj, key_input, val):
    safe_set(obj, key_input, val)


def force_set(obj, key_input, val):
    if is_dict(obj) and is_basestring(key_input):
        obj[key_input] = val

    elif is_list(obj) and is_int(key_input) and key_input >= 0:
        if len(obj) > key_input:
            obj[key_input] = val
        else:
            obj.append(val)

    elif not is_none(obj) and is_list(key_input) and len(key_input) > 0:
        key = key_input[0]
        if len(key_input) == 1:
            if is_dict(obj) and is_basestring(key):
                obj[key] = val
            elif is_list(obj) and is_int(key) and key >= 0:
                if len(obj) > key:
                    obj[key] = val
                else:
                    obj.append(val)
        else:
            if is_dict(obj) and is_basestring(key):
                next_key = key_input[1]
                if key in obj:
                    value = obj[key]
                    if is_basestring(next_key):
                        if not is_dict(value):
                            value = dict()
                            obj[key] = value
                        force_set(value, key_input[1:], val)
                    elif is_int(next_key):
                        if not is_list(value):
                            value = list()
                            obj[key] = value
                        force_set(value, key_input[1:], val)
                else:
                    if is_basestring(next_key):
                        obj[key] = dict()
                        force_set(obj[key], key_input[1:], val)
                    elif is_int(next_key):
                        obj[key] = list()
                        force_set(obj[key], key_input[1:], val)
            elif is_list(obj) and is_int(key) and key >= 0:
                next_key = key_input[1]
                if len(obj) > key:
                    value = obj[key]
                    if is_basestring(next_key):
                        if not is_dict(value):
                            value = dict()
                            obj[key] = value
                        force_set(value, key_input[1:], val)
                    elif is_int(next_key):
                        if not is_list(value):
                            value = list()
                            obj[key] = value
                        force_set(value, key_input[1:], val)
                else:
                    if is_basestring(next_key):
                        value = dict()
                        obj.append(value)
                        force_set(value, key_input[1:], val)
                    elif is_int(next_key):
                        value = list()
                        obj.append(value)
                        force_set(value, key_input[1:], val)


def force_deep_set(obj, key_input, val):
    force_set(obj, key_input, val)


def safe_del(obj, key_input):
    if has(obj, key_input):
        del_(obj, key_input)

    elif not is_none(obj) and is_list(key_input) and len(key_input) > 0:
        key = key_input[0]
        if len(key_input) == 1:
            del_(obj, key)
        elif has(obj, key):
            safe_del(obj[key], key_input[1:])


def safe_deep_del(obj, key_input):
    safe_del(obj, key_input)
