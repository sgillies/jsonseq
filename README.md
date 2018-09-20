# jsonseq

[RFC 7464 JSON Text Sequences](https://tools.ietf.org/html/rfc7464) encoding and decoding for Python.

[![Build
Status](https://travis-ci.com/sgillies/jsonseq.svg?branch=master)](https://travis-ci.com/sgillies/jsonseq)
[![Coverage
Status](https://coveralls.io/repos/github/sgillies/jsonseq/badge.svg?branch=master)](https://coveralls.io/github/sgillies/jsonseq?branch=master)
[![Documentation Status](https://readthedocs.org/projects/jsonseq/badge/?version=latest)](https://jsonseq.readthedocs.io/en/latest/?badge=latest)

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

You can use either `encode()` or `iterencode()` to copy JSON text sequences to a file.

```python
with open("/tmp/example.jsons", "w") as f:
    for chunk in JSONSeqEncoder(with_rs=True, indent=2).iterencode(({"a": i, "b": i} for i in range(3))):
        f.write(chunk)
```

There is no need to add a newline when calling the file's `write()` method.
JSONSeqEncoder ensures that it's already there where it needs to be.

The `jsonseq.decode.JSONSeqDecoder` class takes streams of JSON texts
sandwiched between the optional ASCII record separator (RS, `\x1e`) and
a newline (`\n`) and yields decoded Python objects.

```python
>>> stream = ['\x1e', '{', '"a"', ': ', '0', '}', '\n', '\x1e', '{', '"a"', ': ', '1', '}', '\n', '\x1e', '{', '"a"', ': ', '2', '}', '\n']
>>> for obj in JSONSeqDecoder().decode(stream):
...     print(repr(obj))
...
{'a': 0}
{'a': 1}
{'a': 2}
```

Objects can be read from a file in the same way.

```python
>>> with open("/tmp/example.jsons") as f:
...     for obj in JSONSeqDecoder().decode(f):
...         print(repr(obj))
...
{'a': 0, 'b': 0}
{'a': 1, 'b': 1}
{'a': 2, 'b': 2}
````
