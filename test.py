def check(x):
    if x % 2 == 0:
        return x
lst = filter(check, range(1000,3001))

print(lst)