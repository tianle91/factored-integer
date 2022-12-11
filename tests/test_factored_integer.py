import pytest

from factored_integer.factored_integer import (convert_factorized_to_int,
                                               convert_int_to_factorization, FactoredInteger, get_modulo_power)
from tests.test_primes import PRIMES


@pytest.mark.parametrize(
    ('val', 'expected'),
    [
        pytest.param(1, {}, id='1'),
        pytest.param(2, {2: 1}, id='2'),
        pytest.param(3, {3: 1}, id='3'),
        pytest.param(4, {2: 2}, id='4'),
        pytest.param(72, {2: 3, 3: 2}, id='72'),
        pytest.param(500, {2: 2, 5: 3}, id='500'),
        *[
            pytest.param(p, {p: 1}, id=f'prime: {p}')
            for p in PRIMES
        ]
    ]
)
def test_convert_int_to_factorization(val: int, expected: dict):
    actual = convert_int_to_factorization(val=val)
    assert actual == expected


@pytest.mark.parametrize(
    ('val', 'expected'),
    [
        pytest.param({2: 1}, 2, id='2'),
        pytest.param({2: 2}, 4, id='4'),
        pytest.param({2: 3, 3: 2}, 72, id='72'),
        pytest.param({2: 2, 5: 3}, 500, id='500'),
    ]
)
def test_convert_factorized_to_int(val: int, expected: dict):
    actual = convert_factorized_to_int(val=val)
    assert actual == expected


@pytest.mark.parametrize(
    ('val', 'q'),
    [
        pytest.param(2, 2, id='2 % 2 == 0'),
        pytest.param(4, 2, id='4 % 2 == 0'),
        pytest.param(5, 2, id='5 % 2 == 1'),
        pytest.param((5**2) + 1, 5, id='26 % 5 == 1'),
    ]
)
def test_factored_integer_mod(val: int, q: int):
    expected = val % q
    fi = FactoredInteger(val=val)
    actual = fi.mod(q=q)
    assert actual == expected, fi.factorization


@pytest.mark.parametrize(
    ('a', 'b'),
    [
        pytest.param(2, 2),
        pytest.param(4, 2),
        pytest.param(5, 2),
        pytest.param(25, 4),
    ]
)
def test_factored_integer_mult(a: int, b: int):
    expected = a * b
    actual = (FactoredInteger(val=a) * FactoredInteger(val=b)).as_int()
    assert actual == expected


@pytest.mark.parametrize(
    ('r', 'q', 'pow'),
    [
        pytest.param(1, 2, 1),
        pytest.param(1, 2, 2),
    ]
)
def test_get_modulo_power(r: int, q: int, pow: int):
    expected = (r ** pow) % q
    actual = get_modulo_power(r=r, q=q, pow=pow)
    assert expected == actual
