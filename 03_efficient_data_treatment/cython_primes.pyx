def check_if_prime(int number):
    cdef int i = 2

    while i < number:
        if number % i == 0:
            return False
        i += 1

    return True
