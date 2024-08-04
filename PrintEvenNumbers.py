def print_even_numbers(x,y):
    for i in range(x, y):
        _n = i%2
        if _n == 0:
            print(i)
    return

print(print_even_numbers(0,10))
