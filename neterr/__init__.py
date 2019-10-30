import socket
import ssl
import http.client
import urllib.error

__all__ = [
    'SocketErrors',
    'StrictHTTPErrors',
    'HTTPErrors',
    'AmbiguousHTTPErrors'
]

SocketErrors = [
    ConnectionError,
    socket.timeout
]

StrictHTTPErrors = SocketErrors + [
    ssl.SSLError,
    http.client.IncompleteRead,
    http.client.BadStatusLine,
    http.client.LineTooLong,
]

AmbiguousHTTPErrors = [
    urllib.error.HTTPError
]

try:
    import requests.exceptions
    StrictHTTPErrors += [
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        requests.exceptions.TooManyRedirects,
        requests.exceptions.ChunkedEncodingError
    ]
    HTTPErrors += [
        requests.exceptions.HTTPError
    ]
    AmbiguousHTTPErrors += [
        requests.exceptions.HTTPError
    ]
except ImportError:
    pass

HTTPErrors = StrictHTTPErrors + AmbiguousHTTPErrors + [
    urllib.error.URLError,
]

for error in __all__:
    locals()[error] = tuple(locals()[error])
