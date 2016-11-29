class Primes:
    __int_number = None

    def __init__(self, int_number):
        self.__int_number = int_number

    def sieve_of_eratosthenes(self, max_count_primes):
        array_range_until_max_count = [[] for k in range(max_count_primes)]

