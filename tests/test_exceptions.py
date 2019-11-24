from pytest import fail
from unittest.mock import MagicMock
from neterr import (
    SocketErrors,
    StrictHTTPErrors,
    AmbiguousHTTPErrors,
    HTTPErrors
)


def test_socket_exception():
    try:
        raise SocketErrors[0]()
    except SocketErrors:
        pass


def test_strict_http_exception():
    try:
        raise StrictHTTPErrors[0]()
    except StrictHTTPErrors:
        pass


def test_ambiguous_http_exception():
    try:
        raise AmbiguousHTTPErrors[0](MagicMock())
    except AmbiguousHTTPErrors:
        pass


def test_http_exception():
    try:
        raise HTTPErrors[0]()
    except HTTPErrors:
        pass


def test_strict_is_http():
    try:
        raise StrictHTTPErrors[0]()
    except HTTPErrors:
        pass

def test_ambiguous_is_http():
    try:
        raise AmbiguousHTTPErrors[0](MagicMock())
    except HTTPErrors:
        pass

def test_ambigious_is_not_strict():
    for error in AmbiguousHTTPErrors:
        try:
            raise error(MagicMock())
        except StrictHTTPErrors:
            fail('Ambiguous cannot be caught by strict')
        except HTTPErrors:
            pass
