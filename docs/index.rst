.. jsonseq documentation master file, created by
   sphinx-quickstart on Thu Sep 20 08:53:37 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

jsonseq
=======

`RFC 7464 JSON Text Sequences <https://tools.ietf.org/html/rfc7464>`__ encoding and decoding for Python.

.. image:: https://travis-ci.com/sgillies/jsonseq.svg?branch=master
   :target: https://travis-ci.com/sgillies/jsonseq
   :alt: Build Status

.. image:: https://coveralls.io/repos/github/sgillies/jsonseq/badge.svg?branch=master
   :target: https://coveralls.io/github/sgillies/jsonseq?branch=master
   :alt: Coverage Status

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   index

Introduction
============

The JSONSeqEncoder class takes streams of JSON-serializable Python objects and
yields for each object its JSON representation sandwiched between an optional
ASCII record separator (RS, ``\x1e``) and a newline (``\n``).

.. code-block:: python

    >>> from jsonseq.encode import JSONSeqEncoder
    >>> for chunk in JSONSeqEncoder().encode(({"a": i, "b": i} for i in range(3))):
    ...     print(repr(chunk))
    ...
    '{"a": 0, "b": 0}\n'
    '{"a": 1, "b": 1}\n'
    '{"a": 2, "b": 2}\n'

The RS allows pretty-printed JSON to be streamed out in sequences that can be
decoded again.

.. code-block:: python

    >>> for chunk in JSONSeqEncoder(with_rs=True, indent=2).encode(({"a": i, "b": i} for i in range(3))):
    ...     print(repr(chunk))
    ...
    '\x1e{\n  "a": 0,\n  "b": 0\n}\n'
    '\x1e{\n  "a": 1,\n  "b": 1\n}\n'
    '\x1e{\n  "a": 2,\n  "b": 2\n}\n'

You can also get small chunks of the JSON sequences as they are encoded with
JSONSeqEncoder's iterencode method.

.. code-block:: python

    >>> for chunk in JSONSeqEncoder(with_rs=True).iterencode(({"a": i} for i in range(3))):
    ...     print(repr(chunk))
    ...
    '\x1e'
    '{'
    '"a"'
    ': '
    '0'
    '}'
    '\n'
    '\x1e'
    '{'
    '"a"'
    ': '
    '1'
    '}'
    '\n'
    '\x1e'
    '{'
    '"a"'
    ': '
    '2'
    '}'
    '\n'

You can use either encode or iterencode to copy JSON text sequences to a file.

.. code-block:: python

    with open("/tmp/example.jsons", "w") as f:
        for chunk in JSONSeqEncoder(with_rs=True, indent=2).iterencode(({"a": i, "b": i} for i in range(3))):
            f.write(chunk)

There is no need to add a newline when calling the file's write method.
JSONSeqEncoder ensures that it's already there where it needs to be.

The JSONSeqDecoder class takes streams of JSON texts sandwiched between the
optional RS and a newline and yields decoded Python objects.

.. code-block:: python

    >>> stream = ['\x1e', '{', '"a"', ': ', '0', '}', '\n', '\x1e', '{', '"a"', ': ', '1', '}', '\n', '\x1e', '{', '"a"', ': ', '2', '}', '\n']
    >>> for obj in JSONSeqDecoder().decode(stream):
    ...     print(repr(obj))
    ...
    {'a': 0}
    {'a': 1}
    {'a': 2}

Objects can be read from a file in the same way.

.. code-block:: python

    >>> with open("/tmp/example.jsons") as f:
    ...     for obj in JSONSeqDecoder().decode(f):
    ...         print(repr(obj))
    ...
    {'a': 0, 'b': 0}
    {'a': 1, 'b': 1}
    {'a': 2, 'b': 2}


API Documentation
=================

jsonseq package
---------------

.. automodule:: jsonseq

jsonseq.decode module
---------------------

.. automodule:: jsonseq.decode
    :members:
    :undoc-members:
    :show-inheritance:
    :member-order: groupwise

jsonseq.encode module
---------------------

.. automodule:: jsonseq.encode
    :members:
    :undoc-members:
    :show-inheritance:
    :member-order: groupwise

Project Home
============

`https://github.com/sgillies/jsonseq <https://github.com/sgillies/jsonseq>`__

See Also
========

- `RFC 7464 JSON Text Sequences <https://tools.ietf.org/html/rfc7464>`__


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
