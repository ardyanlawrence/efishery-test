from ..result.result import Result


def input_failure():
    return {
        'code': Result.INPUT_FAILURE,
        'text': Result.Message.INPUT_FAILURE,
        'headers': None,
        'body': None
    }


def timeout():
    return {
        'code': Result.TIMEOUT,
        'text': Result.Message.TIMEOUT,
        'headers': None,
        'body': None
    }


def network_failure():
    return {
        'code': Result.NETWORK_FAILURE,
        'text': Result.Message.NETWORK_FAILURE,
        'headers': None,
        'body': None
    }


def unknown_error():
    return {
        'code': Result.UNKNOWN_ERROR,
        'text': Result.Message.UNKNOWN_ERROR,
        'headers': None,
        'body': None
    }
