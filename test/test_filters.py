import sys
import os

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),
                             'filter_plugins'))

print(sys.path)

from named_conf import named_conf, with_key, without_key  # noqa: E402


def test_named_conf():
    assert named_conf('a') == "a;"
    assert named_conf(['a', 'b']) == "a;\nb;"
    assert named_conf({'a': 'b'}) == "a b;"
    assert named_conf({'a': ['b', 'c']}) == "a {\n  b;\n  c;\n};"
    assert named_conf({'a': {'b': 'c'}}) == "a {\n  b c;\n};"


def test_with_key():
    assert with_key({'a': 'b'}, 'a') == {'a': 'b'}
    assert with_key({}, 'b') == {}
    assert with_key({'a': 'b'}, 'b') == {}
    assert with_key({'a': 'b', 'c': 'd'}, 'a') == {'a': 'b'}


def test_without_key():
    assert without_key({}, 'a') == {}
    assert without_key({'a': 'b'}, 'a') == {}
    assert without_key({'a': 'b'}, 'c') == {'a': 'b'}
    assert without_key({'a': 'b', 'c': 'd'}, 'c') == {'a': 'b'}
