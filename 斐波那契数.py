def fib(number):
    if number in cache:
        return cache[number]
    if number == 0 or number == 1:
        return 1
    else:
        cache[number] = fib(number - 1) + fib(number - 2)
    return cache[number]

if __name__ == '__main__':
    cache = {}
    # print(fib(35))
    print(fib(10))
    print(fib(15))
    print(cache)