
**HCF**

          *def HCF(num1, num2):

            final = 0
            for i in range(1, min(num1,num2)+1):
              if num1 %i == 0 and num2 %i == 0:
            
                final = i
            return final

          HCF(24,48)       
---

**LCM**

        def LCM(num1, num2):
          
          maxnum = max(num1, num2)


          while True:
            if maxnum % num1 == 0 and maxnum % num2 == 0:
              break
            maxnum += 1

          return maxnum

---
1. Check if a number is a strong number (sum of factorials of digits = number).

                def fact(n):
                  if n == 0 or n == 1:
                    return 1

                  return n * fact(n-1)

                def strong_num(num):
                  campare = num

                  ans = 0
           
                  while num > 0:
                    dig = num %10
                    ans += fact(dig)
                    num = num // 10               

                # check  (sum of factorials of digits = number).
                  if campare == ans:
                    print( "True")
                  else:
                    print("False")

---
Print first n terms of an arithmetic progression (a, d).

      AP (Arithmetic Progression)

      Nth term:

      a + (n - 1)d

-

      def AP(n, a, d):

          for i in range(n):
              term = a + i * d
              print(term)


      AP(5, 2, 3)

---
Print first n terms of a geometric progression (a, r).

    GP (Geometric Progression)

    Nth term:

    a × r^(n - 1)

-

    def GP(n, a, r):

    for i in range(n):
        term = a * (r ** i)
        print(term)
