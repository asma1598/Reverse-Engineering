def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_fibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1

    while a < n:
        a, b = b, a + b

    return a == n



def main():
    num = 121

    print("Number:", num)
    print("Prime:", is_prime(num))
    print("Palindrome:", is_palindrome(num))
    print("Fibonacci:", is_fibonacci(num))



if __name__ == "__main__":
    main()