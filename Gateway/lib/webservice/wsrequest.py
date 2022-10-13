from sys import version_info

from iotera.utility.bytes_ import from_basestring, is_bytes
from iotera.utility.json_ import parse, parse_array, stringify_ignore_null
from iotera.utility.object import is_basestring, is_dict, is_list, opt_basestring, opt_int
from iotera.webservice.wsresponse import input_failure

TIMEOUT = 5


def __is_python_3():
    major = version_info[0]
    return major == 3


if __is_python_3():
    from urllib.parse import urlencode as urlencode_3
    from urllib.request import Request as Request_3
    from iotera.webservice.__wsrequest_3 import REQUEST as REQUEST_3

    urlencode = urlencode_3


    def Request(url, method, headers, data):
        return Request_3(url, method=method, headers=headers, data=data)


    REQUEST = REQUEST_3

else:
    from urllib import urlencode as urlencode_2
    from urllib2 import Request as Request_2
    from iotera.webservice.__wsrequest_2 import REQUEST as REQUEST_2

    urlencode = urlencode_2


    def Request(url, method, headers, data):
        return Request_2(url, headers=headers, data=data)


    REQUEST = REQUEST_2


def __REQUEST_WITHOUT_BODY(url, method='GET', query_params=None, headers=None, timeout=TIMEOUT,
                           resp_content_type='json'):
    if not is_basestring(url):
        return input_failure()

    method = opt_basestring(method, 'GET')
    timeout = opt_int(timeout, TIMEOUT)
    resp_content_type = opt_basestring(resp_content_type, 'json')

    option_query_params = ''
    if is_dict(query_params):
        option_query_params = '?' + urlencode(query_params, True)
    url += option_query_params

    option_headers = {}
    if is_dict(headers):
        option_headers = headers

    request = Request(url, method=method, headers=option_headers, data=None)
    return REQUEST(request, timeout, resp_content_type)


def __REQUEST_WITH_BODY(url, method='POST', query_params=None, body=None, headers=None, timeout=TIMEOUT,
                        req_content_type='json', resp_content_type='json'):
    if not is_basestring(url):
        return input_failure()

    method = opt_basestring(method, 'POST')
    timeout = opt_int(timeout, TIMEOUT)
    req_content_type = opt_basestring(req_content_type, 'json')
    resp_content_type = opt_basestring(resp_content_type, 'json')

    option_query_params = ''
    if is_dict(query_params):
        option_query_params = '?' + urlencode(query_params, True)
    url += option_query_params

    option_headers = {}
    if is_dict(headers):
        option_headers = headers

    if req_content_type == 'json':
        if 'Content-Type' not in option_headers:
            option_headers['Content-Type'] = 'application/json'
        option_body = ''
        if is_dict(body) or is_list(body):
            option_body = stringify_ignore_null(body)
        elif is_dict(parse(body)):
            option_body = body
        elif is_list(parse_array(body)):
            option_body = body
    elif req_content_type == 'text':
        if 'Content-Type' not in option_headers:
            option_headers['Content-Type'] = 'application/text'
        option_body = ''
        if is_basestring(body):
            option_body = body
    elif req_content_type == 'bytes':
        if 'Content-Type' not in option_headers:
            option_headers['Content-Type'] = 'application/octet-stream'
        option_body = from_basestring('')
        if is_bytes(body) or isinstance(body, bytearray):
            option_body = body
    else:
        option_body = ''

    if not is_bytes(option_body):
        option_body = from_basestring(option_body)

    request = Request(url, method=method, headers=option_headers, data=option_body)
    return REQUEST(request, timeout, resp_content_type)


def GET(url, query_params=None, headers=None, timeout=TIMEOUT, resp_content_type='json'):
    return __REQUEST_WITHOUT_BODY(url, 'GET', query_params, headers, timeout, resp_content_type)


def POST(url, query_params=None, body=None, headers=None, timeout=TIMEOUT, req_content_type='json',
         resp_content_type='json'):
    return __REQUEST_WITH_BODY(url, 'POST', query_params, body, headers, timeout, req_content_type, resp_content_type)


def PUT(url, query_params=None, body=None, headers=None, timeout=TIMEOUT, req_content_type='json',
        resp_content_type='json'):
    return __REQUEST_WITH_BODY(url, 'PUT', query_params, body, headers, timeout, req_content_type, resp_content_type)


def DELETE(url, query_params=None, headers=None, timeout=TIMEOUT, resp_content_type='json'):
    return __REQUEST_WITHOUT_BODY(url, 'DELETE', query_params, headers, timeout, resp_content_type)


def PATCH(url, query_params=None, body=None, headers=None, timeout=TIMEOUT, req_content_type='json',
          resp_content_type='json'):
    return __REQUEST_WITH_BODY(url, 'PATCH', query_params, body, headers, timeout, req_content_type, resp_content_type)


def TGET(url, query_params=None, headers=None, timeout=TIMEOUT):
    return GET(url, query_params, headers, timeout, 'text')


def JGET(url, query_params=None, headers=None, timeout=TIMEOUT):
    return GET(url, query_params, headers, timeout, 'json')


def TPOST(url, query_params=None, body=None, headers=None, timeout=TIMEOUT):
    return POST(url, query_params, body, headers, timeout, 'text', 'text')


def JPOST(url, query_params=None, body=None, headers=None, timeout=TIMEOUT):
    return POST(url, query_params, body, headers, timeout, 'json', 'json')


def TPUT(url, query_params=None, body=None, headers=None, timeout=TIMEOUT):
    return PUT(url, query_params, body, headers, timeout, 'text', 'text')


def JPUT(url, query_params=None, body=None, headers=None, timeout=TIMEOUT):
    return PUT(url, query_params, body, headers, timeout, 'json', 'json')


def TDELETE(url, query_params=None, headers=None, timeout=TIMEOUT):
    return DELETE(url, query_params, headers, timeout, 'text')


def JDELETE(url, query_params=None, headers=None, timeout=TIMEOUT):
    return DELETE(url, query_params, headers, timeout, 'json')


def TPATCH(url, query_params=None, body=None, headers=None, timeout=TIMEOUT):
    return PATCH(url, query_params, body, headers, timeout, 'text', 'text')


def JPATCH(url, query_params=None, body=None, headers=None, timeout=TIMEOUT):
    return PATCH(url, query_params, body, headers, timeout, 'json', 'json')
