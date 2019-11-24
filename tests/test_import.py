import requests
from unittest.mock import patch
import importlib
import neterr


def test_with_requests():
    importlib.reload(neterr)
    assert requests.exceptions.ConnectionError in neterr.StrictHTTPErrors


def test_without_requests():
    raw_import = __import__

    def mock_import(name, *args):
        if name.startswith('requests'):
            raise ImportError()
        return raw_import(name, *args)

    with patch('builtins.__import__', side_effect=mock_import):
        importlib.reload(neterr)
    assert requests.exceptions.ConnectionError not in neterr.StrictHTTPErrors
