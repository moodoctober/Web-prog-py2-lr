def  mk(a, n):
    if a<0 and n % 2==0:
        return "Отрицательное число и четная степень"
    ap = a/n
    while True:
        x = 1/n * ((n-1)*ap + a/ap**(n-1))
        if abs(ap - x)<0.00001:
            return x
        ap = x

a = int(input("Введите число: "))
n = int(input("Введите степень корня: "))
print (mk(a,n))

