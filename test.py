x = input()
lst = []
try:
    for i in range(1,5):
        lst.append(x*i)
    print(sum(map(int,lst)))
except:
    print('我只会算算数')


    