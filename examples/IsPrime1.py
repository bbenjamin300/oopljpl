#!/usr/bin/env python3

# -----------
# IsPrime1.py
# -----------

from math import sqrt

def is_prime (n) :
    assert(n > 0)
    if (n < 2) or ((n % 2) == 0) :
        return False
    for i in range(3, int(sqrt(n))) :
        if (n % i) == 0:
            return False
    return True

print("IsPrime1.py")

assert(not is_prime( 1));
assert(    is_prime( 3));
assert(not is_prime( 4));
assert(    is_prime( 5));
assert(not is_prime( 6));
assert(    is_prime( 7));
assert(not is_prime( 8));
assert(not is_prime(10));
assert(    is_prime(11));

print("Done.")

"""
% coverage run --branch IsPrime1.py
IsPrime1.py
Done.

% coverage report
Name       Stmts   Miss Branch BrMiss  Cover
--------------------------------------------
IsPrime1      21      1      6      1    93%
"""