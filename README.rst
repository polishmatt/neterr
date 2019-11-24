neterr
======

Groupings of exceptions for working with network requests.

When making network requests in python there are a number of possible exceptions to due network issues. These are often a temporarily problem that should be prioritized separately from a bug in code. As a result handling them with a bare except is not safe but knowing exactly what exceptions to handle can be difficult.

Installation
============

.. code-block:: bash

    pip install neterr


Error Groups
============

neterr provides the exception groups SocketErrors, StrictHTTPErrors, AmbiguousHTTPErrors and HTTPErrors.

Usage Example
-------------

.. code-block:: python

    import urllib.request
    from neterr import HTTPErrors
    try:
        urllib.request.urlopen('http://127.0.0.1').read()
    except HTTPErrors:
        print('caught!')

SocketErrors
------------

SocketErrors contains exceptions that may be raised while working with the socket module.

StrictHTTPErrors
----------------

StrictHTTPErrors contains exceptions that may be raised while working with the http module and some common modules that use it (such as urllib and requests). This grouping only contains exceptions that are clearly not the result of code. They may be caused by an infrastructure or configuration problem and are often temporary.

StrictHTTPErrors is a superset of SocketErrors.

AmbiguousHTTPErrors
-------------------

AmbiguousHTTPErrors contains exceptions that may be raised while working with the http module and some common modules that use it (such as urllib and requests). This grouping contains exceptions that may or may not be caused by code. The most common reason for this ambiguity is that they are the result of an HTTP response with a 4xx or 5xx status. It is recommended to handle 4xx and 5xx responses separately. 4xx responses are often caused by unvalidated user input or another code issue. 5xx responses are often caused by temporarily unavailability in a dependent service.

HTTPErrors
----------

StrictHTTPErrors contains exceptions that may be raised while working with the http module and some common modules that use it (such as urllib and requests).

HTTPErrors is a superset of StrictHTTPErrors and AmbiguousHTTPErrors.

Versioning
==========

This package strictly follows `semantic versioning <https://semver.org>`_.
