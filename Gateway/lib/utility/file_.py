from iotera.utility.json_ import is_empty, parse, stringify_formatted
from iotera.utility.object import is_basestring, is_dict
from ruamel.yaml import YAML


def load_config_file(path):
    obj = load_yaml_file(path)
    if obj is None:
        return load_json_file(path)
    return obj


def save_config_file(json, path):
    return save_yaml_file(json, path)


def merge_config_file(json, path):
    if not is_basestring(path) or not is_dict(json):
        return False

    file_ = None
    try:
        file_ = open(path, 'r+')
        yaml = YAML(typ='safe')
        obj = yaml.load(file_)
        if obj is None:
            data = file_.read()
            obj = parse(data, {})
        obj.update(json)
        file_.truncate(0)
        file_.seek(0)
        if is_empty(obj):
            file_.write('')
        else:
            yaml = YAML()
            yaml.indent(mapping=2, sequence=4, offset=2)
            yaml.dump(obj, file_)

    except IOError:
        try:
            file_ = open(path, 'w')
            if is_empty(json):
                file_.write('')
            else:
                yaml = YAML()
                yaml.indent(mapping=2, sequence=4, offset=2)
                yaml.dump(json, file_)

        except IOError:
            pass

    if file_ is not None:
        file_.close()

    return True


def load_json_file(path):
    if not is_basestring(path):
        return None

    file_ = None
    try:
        file_ = open(path, 'r')
        data = file_.read()
        obj = parse(data)
    except IOError:
        obj = None

    if file_ is not None:
        file_.close()

    return obj


def save_json_file(json, path):
    if not is_dict(json) or not is_basestring(path):
        return False

    file_ = None
    try:
        file_ = open(path, 'w')
        if is_empty(json):
            file_.write('')
        else:
            file_.write(stringify_formatted(json))
    except IOError:
        pass

    if file_ is not None:
        file_.close()

    return True


def merge_json_file(json, path):
    if not is_basestring(path) or not is_dict(json):
        return False

    file_ = None
    try:
        file_ = open(path, 'r+')
        data = file_.read()
        obj = parse(data, {})
        obj.update(json)
        file_.truncate(0)
        file_.seek(0)
        if is_empty(obj):
            file_.write('')
        else:
            file_.write(stringify_formatted(obj))
    except IOError:
        try:
            file_ = open(path, 'w')
            if is_empty(json):
                file_.write('')
            else:
                file_.write(stringify_formatted(json))
        except IOError:
            pass

    if file_ is not None:
        file_.close()

    return True


def load_yaml_file(path):
    if not is_basestring(path):
        return None

    file_ = None
    try:
        file_ = open(path, 'r')
        yaml = YAML(typ='safe')
        obj = yaml.load(file_)
    except IOError:
        obj = None

    if file_ is not None:
        file_.close()

    return obj


def save_yaml_file(json, path):
    if not is_dict(json) or not is_basestring(path):
        return False

    file_ = None
    try:
        file_ = open(path, 'w')
        if is_empty(json):
            file_.write('')
        else:
            yaml = YAML()
            yaml.indent(mapping=2, sequence=4, offset=2)
            yaml.dump(json, file_)
    except IOError:
        pass

    if file_ is not None:
        file_.close()

    return True


def merge_yaml_file(json, path):
    if not is_basestring(path) or not is_dict(json):
        return False

    file_ = None
    try:
        file_ = open(path, 'r+')
        yaml = YAML(typ='safe')
        obj = yaml.load(file_)
        obj.update(json)
        file_.truncate(0)
        file_.seek(0)
        if is_empty(obj):
            file_.write('')
        else:
            yaml = YAML()
            yaml.indent(mapping=2, sequence=4, offset=2)
            yaml.dump(obj, file_)
    except IOError:
        try:
            file_ = open(path, 'w')
            if is_empty(json):
                file_.write('')
            else:
                yaml = YAML()
                yaml.indent(mapping=2, sequence=4, offset=2)
                yaml.dump(json, file_)
        except IOError:
            pass

    if file_ is not None:
        file_.close()

    return True
