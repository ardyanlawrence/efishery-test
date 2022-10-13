from http.client import InvalidURL
from socket import timeout as socket_timeout
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from ..result.result import Result
from ..utility.json_ import parse_any
from ..webservice.wsresponse import network_failure, input_failure, timeout as wsresponse_timeout, unknown_error


def REQUEST(request, timeout, resp_content_type='json'):
    try:
        response = urlopen(request, timeout=timeout)
        code = response.getcode()

        # Headers
        headers_message = response.headers
        headers = {}
        for header in headers_message.keys():
            header_list = headers_message.get_all(header)
            if len(header_list) > 1:
                headers[header] = header_list
            else:
                headers[header] = header_list[0]

        # Body
        body = response.read()
        if resp_content_type == 'json' or resp_content_type == 'text':
            content_charset = response.info().get_content_charset('utf-8')
            body = body.decode(content_charset, errors='ignore')
            if resp_content_type == 'json':
                body = parse_any(body)
                if body is None:
                    body = ''

        return {
            'code': code,
            'text': Result.HTTP.Message.get(code),
            'headers': headers,
            'body': body
        }

    except HTTPError as e:
        code = e.getcode()

        # Headers
        headers_message = e.headers
        headers = {}
        for header in headers_message.keys():
            header_list = headers_message.get_all(header)
            if len(header_list) > 1:
                headers[header] = header_list
            else:
                headers[header] = header_list[0]

        # Body
        body = e.read()
        if resp_content_type == 'json' or resp_content_type == 'text':
            content_charset = e.info().get_content_charset('utf-8')
            body = body.decode(content_charset, errors='ignore')
            if resp_content_type == 'json':
                body = parse_any(body)
                if body is None:
                    body = ''

        return {
            'code': code,
            'text': Result.HTTP.Message.get(code),
            'headers': headers,
            'body': body
        }

    except socket_timeout:
        return wsresponse_timeout()

    except URLError as e:
        if e.reason.__str__() == 'timed out':
            return wsresponse_timeout()
        else:
            return network_failure()

    except InvalidURL:
        return input_failure()

    except:
        pass

    return unknown_error()
