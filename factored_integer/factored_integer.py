from __future__ import annotations

from functools import reduce
from typing import Dict, Optional

from factored_integer.primes import get_prime_by_index


def convert_factorized_to_int(val: Dict[int, int]) -> int:
    return reduce(lambda a, b: a * b, [k**v for k, v in val.items()])


def convert_int_to_factorization(val: int) -> Dict[int, int]:
    out = {}
    i = 0
    p = get_prime_by_index(i)
    while val > 1:
        while val % p == 0:
            out[p] = out.get(p, 0) + 1
            val = val // p
        i += 1
        p = get_prime_by_index(i)
    assert val == 1, val
    return out


def get_modulo_power(r: int, q: int, pow: int) -> int:
    if not r < q:
        raise ValueError('Need r < q')
    return (r ** pow) % q


class FactoredInteger:
    def __init__(self, factorization: Optional[dict] = None, val: Optional[int] = None):
        if factorization is None:
            if val is None:
                raise ValueError('Factorization was not provided. Val needed.')
            factorization = convert_int_to_factorization(val=val)
        self.factorization = factorization

    def as_int(self) -> int:
        return convert_factorized_to_int(val=self.factorization)

    def __str__(self) -> str:
        return str(self.as_int())

    def __mul__(self, other: FactoredInteger) -> FactoredInteger:
        new_factorization = {}
        for k in set(list(self.factorization.keys()) + list(other.factorization.keys())):
            self_v = self.factorization.get(k, 0)
            other_v = other.factorization.get(k, 0)
            new_factorization[k] = self_v + other_v
        return FactoredInteger(factorization=new_factorization)

    def mod(self, q: int) -> int:
        r = None
        for p, k in self.factorization.items():
            p_r = get_modulo_power(r=p % q, q=q, pow=k)
            r = p_r if r is None else (r * p_r) % q
        return r
