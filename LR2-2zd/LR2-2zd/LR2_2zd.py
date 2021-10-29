def mk (n = int (input("Введите число: "))):
    r = 0
    o = 0
    if n<0: 
        o += 1
        n*=-1
    while n > 0:
        temp = n % 10
        r = r * 10 + temp
        n = n // 10
    if o !=0:
        print (r*-1)
    else:
        print (r)
mk()

