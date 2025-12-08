#tính tổng từ 1 đến n (while)
n = int( input('nhập số n '))
tong = 0
i = 0
while i <= n:
    i += 1
    tong += i
    print(f'+ thêm {i} tổng bằng {tong}')