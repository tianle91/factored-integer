from functools import lru_cache


@lru_cache(maxsize=None)
def get_prime_by_index(i=0):
    if i == 0:
        return 2
    assert i > 0
    previous_primes = [get_prime_by_index(k) for k in range(i)]
    n = previous_primes[-1]
    while any([n % p == 0 for p in previous_primes]):
        n += 1
    return n


def is_prime(n: int):
    i = 0
    p = get_prime_by_index(i)
    while p <= n:
        if n == p:
            return True
        else:
            i += 1
            p = get_prime_by_index(i)
    return False
