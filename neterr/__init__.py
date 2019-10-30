import socket
import ssl
import http.client
import urllib.error

__all__ = [
    'HTTP_EXCEPTIONS'
]

optional_exceptions = []

try:
    import requests
    optional_exceptions += (
        requests.exceptions.HTTPError,
        requests.exceptions.ConnectionError
    )
except ImportError:
    pass

HTTP_EXCEPTIONS = (
    ConnectionError,
    socket.timeout,
    ssl.SSLError,
    http.client.BadStatusLine,
    http.client.LineTooLong,
    urllib.error.URLError,
    urllib.error.HTTPError
) + optional_exceptions
