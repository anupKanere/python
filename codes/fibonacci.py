def fib_series(n : int) -> list:
    series = []
    a , b = 1, 2

    for i in range(n):
        series.append(a)
        a , b = b , a+b
    
    return series

res = fib_series(6)
print(f"res = {res}")

