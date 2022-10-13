from numbers import Number
from types import FunctionType

# basestring
try:
    basestring
except NameError:
    basestring = (str, bytes)


def is_basestring(obj):
    return isinstance(obj, basestring)


def opt_basestring(obj, fallback):
    return obj if is_basestring(obj) else (fallback if is_basestring(fallback) else None)


def is_string(obj):
    return isinstance(obj, str)


def opt_string(obj, fallback):
    return obj if is_string(obj) else (fallback if is_string(fallback) else None)


def is_number(obj):
    return isinstance(obj, Number)


def opt_number(obj, fallback):
    return obj if is_number(obj) else (fallback if is_number(fallback) else None)


def is_int(obj):
    return isinstance(obj, int)


def opt_int(obj, fallback):
    return obj if is_int(obj) else (fallback if is_int(fallback) else None)


def is_float(obj):
    return isinstance(obj, float)


def opt_float(obj, fallback):
    return obj if is_float(obj) else (fallback if is_float(fallback) else None)


def is_bool(obj):
    return isinstance(obj, bool)


def opt_bool(obj, fallback):
    return obj if is_bool(obj) else (fallback if is_bool(fallback) else None)


def is_dict(obj):
    return isinstance(obj, dict)


def opt_dict(obj, fallback):
    return obj if is_dict(obj) else (fallback if is_dict(fallback) else None)


def is_list(obj):
    return isinstance(obj, list)


def opt_list(obj, fallback):
    return obj if is_dict(obj) else (fallback if is_dict(fallback) else None)


def is_function(obj):
    return isinstance(obj, FunctionType)


def opt_function(obj, fallback):
    return obj if is_function(obj) else (fallback if is_function(fallback) else None)


def is_tuple(obj):
    return isinstance(obj, tuple)


def is_none(obj):
    return obj is None


def is_either_none(*objs):
    for obj in objs:
        if is_none(obj):
            return True
    return False


def is_neither_none(*objs):
    for obj in objs:
        if is_none(obj):
            return False
    return True


def is_basestring_empty(obj):
    if is_basestring(obj):
        return not obj
    return True


def is_either_basestring_empty(*objs):
    for obj in objs:
        if is_basestring_empty(obj):
            return True
    return False


def is_neither_basestring_empty(*objs):
    for obj in objs:
        if is_basestring_empty(obj):
            return False
    return True


def is_type_equals(value1, value2):
    if is_basestring(value1):
        return is_basestring(value2)
    else:
        type1 = type(value1)
        type2 = type(value2)
        return type1 == type2
