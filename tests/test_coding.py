"""Tests of encoding and decoding"""

from jsonseq.encode import JSONSeqEncoder
from jsonseq.decode import JSONSeqDecoder


def test_decode_empty():
    """Decoding an empty sequence produces an empty sequence"""
    decoder = JSONSeqDecoder()
    assert list(decoder.decode([])) == []


def test_roundtrip_no_rs():
    """Compact sequences without RS round-trip correctly"""
    encoder = JSONSeqEncoder(with_rs=False)
    results = list(encoder.encode(range(100)))
    decoder = JSONSeqDecoder()
    results = list(decoder.decode(results))
    assert results == list(range(100))


def test_roundtrip_default_rs():
    """Sequences with RS round-trip correctly"""
    encoder = JSONSeqEncoder()
    results = list(encoder.encode(({"a": i, "b": 2, "c": None} for i in range(100))))
    decoder = JSONSeqDecoder()
    results = list(decoder.decode(results))
    assert results == list({"a": i, "b": 2, "c": None} for i in range(100))


def test_roundtrip_default_rs_pretty_printed():
    """Sequences with RS round-trip correctly"""
    encoder = JSONSeqEncoder(indent=2)
    results = list(encoder.iterencode(({"a": i, "b": 2, "c": None} for i in range(10))))
    decoder = JSONSeqDecoder()
    results = list(decoder.decode(results))
    assert results == list({"a": i, "b": 2, "c": None} for i in range(10))


def test_fio_output(coutwildrnp_geojsons_path):
    """Test with real world pretty-printed geojsons"""
    decoder = JSONSeqDecoder()
    with open(coutwildrnp_geojsons_path) as f:
        results = list(decoder.decode(f))
    assert len(results) == 67


def test_fio_output_terse(coutwildrnp_geojsons_path):
    """Test terse usage with pretty-printed geojsons"""
    results = list(JSONSeqDecoder().decode(open(coutwildrnp_geojsons_path)))
    assert len(results) == 67
