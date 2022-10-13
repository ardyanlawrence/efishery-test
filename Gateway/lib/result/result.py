class Result:

    def __init__(self):
        pass

    SUCCESS = 0
    FAILED = 1
    WAITING = 2
    UNAVAILABLE = 3
    INPUT_FAILURE = 4
    SERVER_FAILURE = 5
    INTERRUPTED = 7
    BUSY = 8
    TIMEOUT = 9
    NETWORK_FAILURE = 10
    NO_INTERNET_CONNECTION = 11
    NO_WIFI_CONNECTION = 12
    NO_ETH_CONNECTION = 13

    SETTING_EXPIRED = 21
    INVALID_CREDENTIALS = 22

    EXCEPTION = 900
    UNKNOWN_ERROR = 999

    class Message:

        def __init__(self):
            pass

        SUCCESS = 'Success'
        FAILED = 'Failed'
        WAITING = 'Waiting'
        UNAVAILABLE = 'Unavailable'
        INPUT_FAILURE = 'Input Failure'
        SERVER_FAILURE = 'Server Failure'
        INTERRUPTED = 'Interrupted'
        BUSY = 'Busy'
        TIMEOUT = 'Timeout'
        NETWORK_FAILURE = 'Network Failure'
        NO_INTERNET_CONNECTION = 'No Internet Connection'
        NO_WIFI_CONNECTION = 'No Wifi Connection'
        NO_ETH_CONNECTION = 'No Eth Connection'

        SETTING_EXPIRED = 'Setting Expired'
        INVALID_CREDENTIALS = 'Invalid Credentials'

        EXCEPTION = 'Exception'
        UNKNOWN_ERROR = 'Unknown Error'

        @staticmethod
        def get(result):
            switcher = {
                Result.SUCCESS: Result.Message.SUCCESS,
                Result.FAILED: Result.Message.FAILED,
                Result.WAITING: Result.Message.WAITING,
                Result.UNAVAILABLE: Result.Message.UNAVAILABLE,
                Result.INPUT_FAILURE: Result.Message.INPUT_FAILURE,
                Result.SERVER_FAILURE: Result.Message.SERVER_FAILURE,
                Result.INTERRUPTED: Result.Message.INTERRUPTED,
                Result.BUSY: Result.Message.BUSY,
                Result.TIMEOUT: Result.Message.TIMEOUT,
                Result.NETWORK_FAILURE: Result.Message.NETWORK_FAILURE,
                Result.NO_INTERNET_CONNECTION: Result.Message.NO_INTERNET_CONNECTION,
                Result.NO_WIFI_CONNECTION: Result.Message.NO_WIFI_CONNECTION,
                Result.NO_ETH_CONNECTION: Result.Message.NO_ETH_CONNECTION,
                Result.SETTING_EXPIRED: Result.Message.SETTING_EXPIRED,
                Result.INVALID_CREDENTIALS: Result.Message.INVALID_CREDENTIALS,
                Result.EXCEPTION: Result.Message.EXCEPTION,
                Result.UNKNOWN_ERROR: Result.Message.UNKNOWN_ERROR
            }
            return switcher.get(result, Result.Message.UNKNOWN_ERROR)

    class HTTP:

        def __init__(self):
            pass

        CONTINUE = 100
        SWITCHING_PROTOCOLS = 101
        PROCESSING = 102

        OK = 200
        CREATED = 201
        ACCEPTED = 202
        NON_AUTHORITATIVE_INFORMATION = 203
        NO_CONTENT = 204
        RESET_CONTENT = 205
        PARTIAL_CONTENT = 206
        MULTI_STATUS = 207
        ALREADY_REPORTED = 208
        IM_USED = 226

        MULTIPLE_CHOICES = 300
        MOVED_PERMANENTLY = 301
        FOUND = 302
        SEE_OTHER = 303
        NOT_MODIFIED = 304
        USE_PROXY = 305
        TEMPORARY_REDIRECT = 307
        PERMANENT_REDIRECT = 308

        BAD_REQUEST = 400
        UNAUTHORIZED = 401
        PAYMENT_REQUIRED = 402
        FORBIDDEN = 403
        NOT_FOUND = 404
        METHOD_NOT_ALLOWED = 405
        NOT_ACCEPTABLE = 406
        PROXY_AUTHENTICATION_REQUIRED = 407
        REQUEST_TIMEOUT = 408
        CONFLICT = 409
        GONE = 410
        LENGTH_REQUIRED = 411
        PRECONDITION_FAILED = 412
        PAYLOAD_TOO_LARGE = 413
        REQUEST_URI_TOO_LONG = 414
        UNSUPPORTED_MEDIA_TYPE = 415
        REQUESTED_RANGE_NOT_SATISFIABLE = 416
        EXPECTATION_FAILED = 417
        I_AM_A_TEAPOT = 418
        MISDIRECTED_REQUEST = 421
        UNPROCESSABLE_ENTITY = 422
        LOCKED = 423
        FAILED_DEPENDENCY = 424
        UPGRADE_REQUIRED = 426
        PRECONDITION_REQUIRED = 428
        TOO_MANY_REQUESTS = 429
        REQUEST_HEADER_FIELDS_TOO_LARGE = 431
        CONNECTION_CLOSED_WITHOUT_RESPONSE = 444
        UNAVAILABLE_FOR_LEGAL_REASONS = 451
        CLIENT_CLOSED_REQUEST = 499

        INTERNAL_SERVER_ERROR = 500
        NOT_IMPLEMENTED = 501
        BAD_GATEWAY = 502
        SERVICE_UNAVAILABLE = 503
        GATEWAY_TIMEOUT = 504
        HTTP_VERSION_NOT_SUPPORTED = 505
        VARIANT_ALSO_NEGOTIATES = 506
        INSUFFICIENT_STORAGE = 507
        LOOP_DETECTED = 508
        NOT_EXTENDED = 510
        NETWORK_AUTHENTICATION_REQUIRED = 511
        NETWORK_CONNECT_TIMEOUT_ERROR = 599

        class Message:

            def __init__(self):
                pass

            CONTINUE = 'Continue'
            SWITCHING_PROTOCOLS = 'Switching Protocols'
            PROCESSING = 'Processing'

            OK = 'OK'
            CREATED = 'Created'
            ACCEPTED = 'Accepted'
            NON_AUTHORITATIVE_INFORMATION = 'Non-Authoritative Information'
            NO_CONTENT = 'No Content'
            RESET_CONTENT = 'Reset Content'
            PARTIAL_CONTENT = 'Partial Content'
            MULTI_STATUS = 'Multi-Status'
            ALREADY_REPORTED = 'Already Reported'
            IM_USED = 'IM Used'

            MULTIPLE_CHOICES = 'Multiple Choices'
            MOVED_PERMANENTLY = 'Moved Permanently'
            FOUND = 'Found'
            SEE_OTHER = 'See Other'
            NOT_MODIFIED = 'Not Modified'
            USE_PROXY = 'User Proxy'
            TEMPORARY_REDIRECT = 'Temporary Redirect'
            PERMANENT_REDIRECT = 'Permanent Redirect'

            BAD_REQUEST = 'Bad Request'
            UNAUTHORIZED = 'Unauthorized'
            PAYMENT_REQUIRED = 'Payment Required'
            FORBIDDEN = 'Forbidden'
            NOT_FOUND = 'Not Found'
            METHOD_NOT_ALLOWED = 'Method Not Allowed'
            NOT_ACCEPTABLE = 'Not Acceptable'
            PROXY_AUTHENTICATION_REQUIRED = 'Proxy Authentication Required'
            REQUEST_TIMEOUT = 'Request Timeout'
            CONFLICT = 'Conflict'
            GONE = 'Gone'
            LENGTH_REQUIRED = 'Length Required'
            PRECONDITION_FAILED = 'Precondition Failed'
            PAYLOAD_TOO_LARGE = 'Payload Too Large'
            REQUEST_URI_TOO_LONG = 'Request-URI Too Long'
            UNSUPPORTED_MEDIA_TYPE = 'Unsupported Media Type'
            REQUESTED_RANGE_NOT_SATISFIABLE = 'Requested Range Not Satisfiable'
            EXPECTATION_FAILED = 'Expectation Failed'
            I_AM_A_TEAPOT = "I'm a teapot"
            MISDIRECTED_REQUEST = 'Misdirected Request'
            UNPROCESSABLE_ENTITY = 'Unprocessable Entity'
            LOCKED = 'Locked'
            FAILED_DEPENDENCY = 'Failed Dependency'
            UPGRADE_REQUIRED = 'Upgrade Required'
            PRECONDITION_REQUIRED = 'Precondition Required'
            TOO_MANY_REQUESTS = 'Too Many Requests'
            REQUEST_HEADER_FIELDS_TOO_LARGE = 'Request Header Fields Too Large'
            CONNECTION_CLOSED_WITHOUT_RESPONSE = 'Connection Closed Without Response'
            UNAVAILABLE_FOR_LEGAL_REASONS = 'Unavailable For Legal Reasons'
            CLIENT_CLOSED_REQUEST = 'Client Closed Request'

            INTERNAL_SERVER_ERROR = 'Internal Server Error'
            NOT_IMPLEMENTED = 'Not Implemented'
            BAD_GATEWAY = 'Bad Gateway'
            SERVICE_UNAVAILABLE = 'Service Unavailable'
            GATEWAY_TIMEOUT = 'Gateway Timeout'
            HTTP_VERSION_NOT_SUPPORTED = 'HTTP Version Not Supported'
            VARIANT_ALSO_NEGOTIATES = 'Variant Also Negotiates'
            INSUFFICIENT_STORAGE = 'Insufficient Storage'
            LOOP_DETECTED = 'Loop Detected'
            NOT_EXTENDED = 'Not Extended'
            NETWORK_AUTHENTICATION_REQUIRED = 'Network Authentication Required'
            NETWORK_CONNECT_TIMEOUT_ERROR = 'Network Connect Timeout Error'

            @staticmethod
            def is_informational(code):
                return (code / 100) == 1

            @staticmethod
            def is_success(code):
                return (code / 100) == 2

            @staticmethod
            def is_redirect(code):
                return (code / 100) == 3

            @staticmethod
            def is_client_error(code):
                return (code / 100) == 4

            @staticmethod
            def is_server_error(code):
                return (code / 100) == 5

            @staticmethod
            def get(result):
                switcher = {
                    Result.HTTP.CONTINUE: Result.HTTP.Message.CONTINUE,
                    Result.HTTP.SWITCHING_PROTOCOLS: Result.HTTP.Message.SWITCHING_PROTOCOLS,
                    Result.HTTP.PROCESSING: Result.HTTP.Message.PROCESSING,
                    Result.HTTP.OK: Result.HTTP.Message.OK,
                    Result.HTTP.CREATED: Result.HTTP.Message.CREATED,
                    Result.HTTP.ACCEPTED: Result.HTTP.Message.ACCEPTED,
                    Result.HTTP.NON_AUTHORITATIVE_INFORMATION: Result.HTTP.Message.NON_AUTHORITATIVE_INFORMATION,
                    Result.HTTP.NO_CONTENT: Result.HTTP.Message.NO_CONTENT,
                    Result.HTTP.RESET_CONTENT: Result.HTTP.Message.RESET_CONTENT,
                    Result.HTTP.PARTIAL_CONTENT: Result.HTTP.Message.PARTIAL_CONTENT,
                    Result.HTTP.MULTI_STATUS: Result.HTTP.Message.MULTI_STATUS,
                    Result.HTTP.ALREADY_REPORTED: Result.HTTP.Message.ALREADY_REPORTED,
                    Result.HTTP.IM_USED: Result.HTTP.Message.IM_USED,
                    Result.HTTP.MULTIPLE_CHOICES: Result.HTTP.Message.MULTIPLE_CHOICES,
                    Result.HTTP.MOVED_PERMANENTLY: Result.HTTP.Message.MOVED_PERMANENTLY,
                    Result.HTTP.FOUND: Result.HTTP.Message.FOUND,
                    Result.HTTP.SEE_OTHER: Result.HTTP.Message.SEE_OTHER,
                    Result.HTTP.NOT_MODIFIED: Result.HTTP.Message.NOT_MODIFIED,
                    Result.HTTP.USE_PROXY: Result.HTTP.Message.USE_PROXY,
                    Result.HTTP.TEMPORARY_REDIRECT: Result.HTTP.Message.TEMPORARY_REDIRECT,
                    Result.HTTP.PERMANENT_REDIRECT: Result.HTTP.Message.PERMANENT_REDIRECT,
                    Result.HTTP.BAD_REQUEST: Result.HTTP.Message.BAD_REQUEST,
                    Result.HTTP.UNAUTHORIZED: Result.HTTP.Message.UNAUTHORIZED,
                    Result.HTTP.PAYMENT_REQUIRED: Result.HTTP.Message.PAYMENT_REQUIRED,
                    Result.HTTP.FORBIDDEN: Result.HTTP.Message.FORBIDDEN,
                    Result.HTTP.NOT_FOUND: Result.HTTP.Message.NOT_FOUND,
                    Result.HTTP.METHOD_NOT_ALLOWED: Result.HTTP.Message.METHOD_NOT_ALLOWED,
                    Result.HTTP.NOT_ACCEPTABLE: Result.HTTP.Message.NOT_ACCEPTABLE,
                    Result.HTTP.PROXY_AUTHENTICATION_REQUIRED: Result.HTTP.Message.PROXY_AUTHENTICATION_REQUIRED,
                    Result.HTTP.REQUEST_TIMEOUT: Result.HTTP.Message.REQUEST_TIMEOUT,
                    Result.HTTP.CONFLICT: Result.HTTP.Message.CONFLICT,
                    Result.HTTP.GONE: Result.HTTP.Message.GONE,
                    Result.HTTP.LENGTH_REQUIRED: Result.HTTP.Message.LENGTH_REQUIRED,
                    Result.HTTP.PRECONDITION_FAILED: Result.HTTP.Message.PRECONDITION_FAILED,
                    Result.HTTP.PAYLOAD_TOO_LARGE: Result.HTTP.Message.PAYLOAD_TOO_LARGE,
                    Result.HTTP.REQUEST_URI_TOO_LONG: Result.HTTP.Message.REQUEST_URI_TOO_LONG,
                    Result.HTTP.UNSUPPORTED_MEDIA_TYPE: Result.HTTP.Message.UNSUPPORTED_MEDIA_TYPE,
                    Result.HTTP.REQUESTED_RANGE_NOT_SATISFIABLE: Result.HTTP.Message.REQUESTED_RANGE_NOT_SATISFIABLE,
                    Result.HTTP.EXPECTATION_FAILED: Result.HTTP.Message.EXPECTATION_FAILED,
                    Result.HTTP.I_AM_A_TEAPOT: Result.HTTP.Message.I_AM_A_TEAPOT,
                    Result.HTTP.MISDIRECTED_REQUEST: Result.HTTP.Message.MISDIRECTED_REQUEST,
                    Result.HTTP.UNPROCESSABLE_ENTITY: Result.HTTP.Message.UNPROCESSABLE_ENTITY,
                    Result.HTTP.LOCKED: Result.HTTP.Message.LOCKED,
                    Result.HTTP.FAILED_DEPENDENCY: Result.HTTP.Message.FAILED_DEPENDENCY,
                    Result.HTTP.UPGRADE_REQUIRED: Result.HTTP.Message.UPGRADE_REQUIRED,
                    Result.HTTP.PRECONDITION_REQUIRED: Result.HTTP.Message.PRECONDITION_REQUIRED,
                    Result.HTTP.TOO_MANY_REQUESTS: Result.HTTP.Message.TOO_MANY_REQUESTS,
                    Result.HTTP.REQUEST_HEADER_FIELDS_TOO_LARGE: Result.HTTP.Message.REQUEST_HEADER_FIELDS_TOO_LARGE,
                    Result.HTTP.CONNECTION_CLOSED_WITHOUT_RESPONSE: Result.HTTP.Message.CONNECTION_CLOSED_WITHOUT_RESPONSE,
                    Result.HTTP.UNAVAILABLE_FOR_LEGAL_REASONS: Result.HTTP.Message.UNAVAILABLE_FOR_LEGAL_REASONS,
                    Result.HTTP.CLIENT_CLOSED_REQUEST: Result.HTTP.Message.CLIENT_CLOSED_REQUEST,
                    Result.HTTP.INTERNAL_SERVER_ERROR: Result.HTTP.Message.INTERNAL_SERVER_ERROR,
                    Result.HTTP.NOT_IMPLEMENTED: Result.HTTP.Message.NOT_IMPLEMENTED,
                    Result.HTTP.BAD_GATEWAY: Result.HTTP.Message.BAD_GATEWAY,
                    Result.HTTP.SERVICE_UNAVAILABLE: Result.HTTP.Message.SERVICE_UNAVAILABLE,
                    Result.HTTP.GATEWAY_TIMEOUT: Result.HTTP.Message.GATEWAY_TIMEOUT,
                    Result.HTTP.HTTP_VERSION_NOT_SUPPORTED: Result.HTTP.Message.HTTP_VERSION_NOT_SUPPORTED,
                    Result.HTTP.VARIANT_ALSO_NEGOTIATES: Result.HTTP.Message.VARIANT_ALSO_NEGOTIATES,
                    Result.HTTP.INSUFFICIENT_STORAGE: Result.HTTP.Message.INSUFFICIENT_STORAGE,
                    Result.HTTP.LOOP_DETECTED: Result.HTTP.Message.LOOP_DETECTED,
                    Result.HTTP.NOT_EXTENDED: Result.HTTP.Message.NOT_EXTENDED,
                    Result.HTTP.NETWORK_AUTHENTICATION_REQUIRED: Result.HTTP.Message.NETWORK_AUTHENTICATION_REQUIRED,
                    Result.HTTP.NETWORK_CONNECT_TIMEOUT_ERROR: Result.HTTP.Message.NETWORK_CONNECT_TIMEOUT_ERROR
                }
                return switcher.get(result, Result.Message.UNKNOWN_ERROR)
