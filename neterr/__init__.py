import socket
import ssl
import http.client
import urllib.error

__all__ = (
    'SocketErrors',
    'StrictHTTPErrors',
    'HTTPErrors',
    'AmbiguousHTTPErrors',
    'ExceptionTuple'
)


class ExceptionTuple(tuple):
    def __add__(self, other):
        if isinstance(other, type) and issubclass(other, BaseException):
            other = (other,)
        else:
            other = tuple(other)
        return super().__add__(other)


SocketErrors = (
    ConnectionError,
    socket.timeout
)

StrictHTTPErrors = SocketErrors + (
    ssl.SSLError,
    http.client.IncompleteRead,
    http.client.BadStatusLine,
    http.client.LineTooLong,
)

AmbiguousHTTPErrors = (
    urllib.error.URLError,
)

try:
    import requests.exceptions
    StrictHTTPErrors += (
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        requests.exceptions.TooManyRedirects,
        requests.exceptions.ChunkedEncodingError
    )
    AmbiguousHTTPErrors += (
        requests.exceptions.HTTPError,
    )
except ImportError:
    pass

HTTPErrors = StrictHTTPErrors + AmbiguousHTTPErrors

for error in __all__:
    if isinstance(locals()[error], tuple):
        locals()[error] = ExceptionTuple(locals()[error])
