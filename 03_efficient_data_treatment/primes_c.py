import pyximport
pyximport.install()
from cython_primes import check_if_prime


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
          67, 71, 73, 79, 83, 89, 97]
NUM_PRIMES = 50000


if __name__ == '__main__':
    primes = [number for number in range(2, NUM_PRIMES)
              if check_if_prime(number)]
    assert primes[:len(PRIMES)] == PRIMES
    print(primes)
