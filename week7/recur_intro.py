def countdown_with_for(n):
    for i in range(n, 0, -1):
        print(i)
    print("Blastoff")


def countdown_with_while(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blastoff")


def countdown_recursively(n: int) -> None:
    # base case
    if n == 0:
        print("Blastoff")
        return
    print(n)
    countdown_recursively(n - 1)


def sum_of_n_minus_1(n):
    if n == 1:
        return 1
    return n + sum_of_n_minus_1(n - 1)

def sum_natural_numbers_easy(n) -> int:
    return sum(range(n+1))

memo = {}
def fib(n: int) -> int:
    #base case
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n <= 2:
        return 1
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
print(fib(100))

if __name__ == '_bld':
    for i in range(10):
        number = 10**i
        print(sum_natural_numbers_easy(number), number**2, 0.5 * number**2, sep=' | ')
        print('-'*20)

# countdown_recursively(10)