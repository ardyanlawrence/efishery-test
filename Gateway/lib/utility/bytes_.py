from sys import version_info

from ..utility.object import is_basestring


def __is_python_3():
    major = version_info[0]
    return major == 3


if __is_python_3():
    def is_bytes(obj):
        return isinstance(obj, bytes)


    def from_basestring(obj):
        if is_basestring(obj):
            return obj.encode()
        elif is_bytes(obj):
            return obj
        return None


    def to_basestring(b):
        if is_bytes(b):
            return b.decode()
        elif is_basestring(b):
            return b
        return None


else:
    def is_bytes(obj):
        return isinstance(obj, bytearray)


    def from_basestring(obj):
        if is_basestring(obj):
            return bytearray(obj)
        elif is_bytes(obj):
            return obj
        return None


    def to_basestring(b):
        if is_bytes(b):
            return str(b.decode())
        elif is_basestring(b):
            return b
        return None


def opt_bytes(obj, fallback):
    return obj if is_bytes(obj) else (fallback if is_bytes(fallback) else None)
