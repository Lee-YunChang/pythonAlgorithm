def solution(N):

    primes = find_primes(26)
    result = []
    for i in range(0, len(primes)):
        if N % primes[i] == 0:
            minimum_primes = primes[i]
            break

    letters = [chr(ord('a') + i) for i in range(26)]

    minimum_primes = minimum_primes
    m = int(N / minimum_primes)
    k = int(N / m)
    while m > 0:
        for letter in letters:
            if m == 0:
                break

            for j in range(k):
                result.append(letter)
            m -= 1

    return ''.join(result)




def find_primes(n):
    primes = []
    if n >= 2:
        primes.append(2)
    for num in range(3, n + 1, 2):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

n = 3
result = solution(n)
print(result)