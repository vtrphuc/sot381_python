#Viết hàm tính giai thừa của một số nguyên dương
def tinhgt(n):
    if n < 0:
        return 'hãy nhập số nguyên dương'
    kq = 1
    for i in range(1, n+1):
        kq *= i
    return kq
so = int( input('bạn muốn tính giai thừa số: '))
print(tinhgt(so))