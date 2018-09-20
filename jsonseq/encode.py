"""RFC 7464 GeoJSON Text Sequence encoding."""

import json
from typing import Iterable, Iterator


class JSONSeqEncoder(object):
    """Encodes sequences of Python objects."""

    def __init__(self, with_rs: bool = True, **kwds):
        """Create a new encoder.

        Parameters
        ----------
        with_rs : bool, optional
            Whether to encode using RFC 7464 RS delimiters
        kwds : dict
            Keyword arguments for JSONEncoder()

        """
        self.encoder = json.JSONEncoder(**kwds)
        self.with_rs = with_rs

    def encode(self, iterable: Iterable) -> Iterator[str]:
        """Yield JSON representations of objects.

        Parameters
        ----------
        iterable : Iterable
            An iterable object, the source of Python objects to encode.

        Yields
        ------
        str

        """
        leader = u"\x1e" if self.with_rs else ""
        for o in iterable:
            yield "{}{}\n".format(leader, self.encoder.encode(o))

    def iterencode(self, iterable: Iterable) -> Iterator[str]:
        """Yield parts of JSON representations as available.

        Parameters
        ----------
        iterable : Iterable
            An iterable object, the source of Python objects to encode.

        Yields
        ------
        str

        """
        for o in iterable:
            if self.with_rs:
                yield u"\x1e"
            for part in self.encoder.iterencode(o):
                yield part
            yield "\n"
