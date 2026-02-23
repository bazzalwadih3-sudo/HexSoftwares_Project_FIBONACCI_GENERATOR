def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        a, b = b, a + b

num = int(input("Number:"))
fibonacci(num)