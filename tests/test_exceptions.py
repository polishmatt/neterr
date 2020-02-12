import pytest
from unittest.mock import MagicMock
from neterr import (
    SocketErrors,
    StrictHTTPErrors,
    AmbiguousHTTPErrors,
    HTTPErrors
)


class TestException(Exception):
    pass


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
            pytest.fail('Ambiguous cannot be caught by strict')
        except HTTPErrors:
            pass


def test_add_single_catches_other():
    try:
        raise TestException()
    except HTTPErrors + TestException:
        pass


def test_add_single_catches_http():
    try:
        raise HTTPErrors[0]()
    except HTTPErrors + TestException:
        pass


def test_add_multiple_catches_other():
    try:
        raise TestException()
    except HTTPErrors + [TestException]:
        pass


def test_add_multiple_catches_http():
    try:
        raise HTTPErrors[0]()
    except HTTPErrors + [TestException]:
        pass


def test_add_unsupported():
    with pytest.raises(TypeError):
        HTTPErrors + None
