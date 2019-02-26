# Chapter 7 exercises


def find_odd(lst):
    num_odd = 0
    for i in lst:
        if i % 2 == 0:
           continue
        else:
            num_odd += 1
    print(num_odd)


def find_sum_even(lst):
    total = 0
    for i in lst:
        if i % 2 == 0:
            total = total + i
        else:
            continue
    print(total)


def find_sum_odd(lst):
    total = 0
    for i in lst:
        if i % 2 == 0:
            continue
        else:
            total += i
    print(total)


def numLen(s, n):
    words = s.split()
    counter = 0
    for word in words:
        if len(word) == n:
            counter += 1
    return counter


def sumAllstopEven(lst):
    total = 0
    for n in lst:
        if n % 2 == 0:
            break
        else:
            total += n
    return total


def wordsPlusSam(w):
    words = 0
    for n in w:
        words += 1
        if n == "sam":
            break
    return words


# Skipped #7 & 8


def print_triangular_numbers(n):
    x = 1
    for i in range(n):
        print(x, end="    ")
        y = (x * (x + 1) / 2)
        print(int(y))
        x += 1
        if x > n == True:
            break

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True


# Skipped #11


def num_digits(n):
    count = 0
    n = abs(n)
    if n == 0:
        count = 1
        return count
    else:
        while n != 0:
            count = count + 1
            n = n // 10
        return count


def num_even_digits(ns):
    count = 0
    ns = str(ns)
    for n in ns:
        n = int(n)
        if n % 2 == 0:
            count += 1
    return count

def sum_of_squares(xs):
    sum = 0
    for n in xs:
        nsum = n * n
        sum += nsum
    return sum
        
            