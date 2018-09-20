# jsonseq

[RFC 7464 JSON Text Sequences](https://tools.ietf.org/html/rfc7464) encoding and decoding for Python.

[![Build
Status](https://travis-ci.com/sgillies/jsonseq.svg?branch=master)](https://travis-ci.com/sgillies/jsonseq)
[![Coverage
Status](https://coveralls.io/repos/github/sgillies/jsonseq/badge.svg?branch=master)](https://coveralls.io/github/sgillies/jsonseq?branch=master)

## Usage

The `jsonseq.encode.JSONSeqEncoder` class takes streams of JSON-serializable
Python objects and yields for each object its JSON representation sandwiched
between an optional ASCII record separator (RS, `\x1e`) and a newline (`\n`).

```python
>>> from jsonseq.encode import JSONSeqEncoder
>>> for chunk in JSONSeqEncoder().encode(({"a": i, "b": i} for i in range(3))):
...     print(repr(chunk))
...
'{"a": 0, "b": 0}\n'
'{"a": 1, "b": 1}\n'
'{"a": 2, "b": 2}\n'
```

The RS allows pretty-printed JSON to be streamed out in sequences that can be
decoded again.

```python
>>> for chunk in JSONSeqEncoder(with_rs=True, indent=2).encode(({"a": i, "b": i} for i in range(3))):
...     print(repr(chunk))
...
'\x1e{\n  "a": 0,\n  "b": 0\n}\n'
'\x1e{\n  "a": 1,\n  "b": 1\n}\n'
'\x1e{\n  "a": 2,\n  "b": 2\n}\n'
```

You can also get small chunks of the JSON sequences as they are encoded with
the `iterencode()` method.

```python
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
```
