# Taking 1st two fibonacci numbers as 0 and 1
 
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
 
# Driver Program
 
print(fibonacci(9))

def fib():
     n = int(input())
     a = 0
     b = 1
     p = []
     for i in range(n):
         p.append(a)
         a,b = b,a+b
     print(p)
fib()
