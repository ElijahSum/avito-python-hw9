from one_hot_encoder import fit_transform
import pytest


def test_encode():
    actual = ['hello', 'world']
    expected = [
        ('hello', [0, 1]),
        ('world', [1, 0])
    ]
    assert fit_transform(actual) == expected


def test_correct_len():
    for i in fit_transform('1', '2', '1', '2', '2', '2', '2'):
        assert len(i[1]) == 2


def test_raise_exception():
    with pytest.raises(TypeError):
        fit_transform()


def test_one_element_len():
    actual = fit_transform('Python')
    assert len(actual) == 1


def test_one_element_value():
    actual = fit_transform('Moscow')
    expected = [('Moscow', [1])]
    assert actual == expected
