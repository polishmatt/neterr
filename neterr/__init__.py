import socket
import ssl
import http.client
import urllib.error

__all__ = [
    'HTTP_EXCEPTIONS'
]

optional_exceptions = []

try:
    import requests.exceptions
    optional_exceptions += (
        requests.exceptions.ConnectionError
        requests.exceptions.HTTPError,
        requests.exceptions.Timeout,
        requests.exceptions.TooManyRedirects,
        requests.exceptions.ChunkedEncodingError
    )
except ImportError:
    pass

HTTP_EXCEPTIONS = (
    ConnectionError,
    socket.timeout,
    ssl.SSLError,
    http.client.IncompleteRead,
    http.client.BadStatusLine,
    http.client.LineTooLong,
    urllib.error.URLError,
) + optional_exceptions

AMBIGUOUS_EXCEPTIONS = (
    requests.exceptions.HTTPError,
    urllib.error.HTTPError
)
