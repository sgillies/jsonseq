"""RFC 7464 GeoJSON Text Sequence decoding."""

import json
from typing import Iterable, Iterator


class JSONSeqDecoder(object):
    """Decode Python objects from a stream of JSON texts."""

    def __init__(self, **kwds):
        """Create a decoder.

        Parameters
        ----------
        kwds : dict, optional
            Keyword arguments for JSONDecoder()

        """
        self.decoder = json.JSONDecoder(**kwds)

    def decode(self, seq: Iterable) -> Iterator[object]:
        """Iterate over decoded objects in the JSON text sequence.

        Parameters
        ----------
        seq : Iterable
            JSON strings or pieces of strings.

        Yields
        ------
        object

        """
        buffer = ""
        has_rs = None

        for line in seq:

            if has_rs is None:
                has_rs = line.startswith(u"\x1e")

            if not has_rs:
                yield self.decoder.decode(line)

            else:
                if line.startswith(u"\x1e"):
                    if buffer:
                        yield self.decoder.decode(buffer)
                    buffer = line.lstrip(u"\x1e")
                else:
                    buffer += line

        if buffer:
            yield self.decoder.decode(buffer)

        return
