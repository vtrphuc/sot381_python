#Viết hàm kiểm tra số nguyên tố
def so(n):
    if n <= 1:
        return f'số {n} không phải số nguyên tố'
    for i in range(2, n + 1):
        if i == n:
            continue
        elif n % i == 0:
            return f'số {n} không phải số nguyên tố'
    return f'số {n} là số nguyên tố'
n = int( input('nhập số cần kiểm tra: '))
print(so(n))