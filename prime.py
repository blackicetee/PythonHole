def is_prime(x):
    if x > 2:
        condition = True
        for i in range(2, x):
            if x % i == 0:
                condition = False
        return condition
    elif x == 2:
        return True
    else:
        return False


print("Is 3 prime? {}".format(is_prime(3)))
print("Is 4 prime? {}".format(is_prime(4)))


def list_all_primes(x):
    primes = []
    num = 2
    while len(primes) < x:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def list_to_string(l):
    concat_string = ""
    counter = 1
    for i in l:
        concat_string += "\nThe " + str(counter) + ". prime is = " + str(i)
        counter += 1
    return concat_string


print("Get all primes until 100: {}".format(list_to_string(list_all_primes(100))))
