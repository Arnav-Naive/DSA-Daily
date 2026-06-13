Armstrong Number ✅
ex 1:
153

1³ + 5³ + 3³
= 1 + 125 + 27
= 153

-----

1634

1⁴ + 6⁴ + 3⁴ + 4⁴
= 1 + 1296 + 81 + 256
= 1634

----------
-----
-> to check a single no. is prime

        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

        N = int(input())
        if is_prime(N):
            print("Prime")
        else:
            print("Not Prime")
---
print from 1 to 100

        for i in range(2, 101):
            prime = True

            for p in range(2, i):
                if i % p == 0:
                    prime = False
                    break

            if prime:
                print(i)
---
---
Fibonaci (2 in 1)

                def fibo(n):
                    if n == 1 or n == 2:
                        return 1

                    return fibo(n - 1) + fibo(n - 2)


                n = 10

                for i in range(1, n + 1):
                    print(fibo(i), end=" ")
  
---
---
