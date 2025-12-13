#tính tổng các số lẻ hoặc chẵn từ 1 đến n
n = int( input('nhập số n: '))
while n <= 0:
    n = int( input('vui lòng nhập số nguyên dương'))
cl = input('bạn muốn tính tổng số chẵn hay lẻ(chan, le): ')
while cl not in ['chan', 'le']:
    print('không hợp lệ')
    cl = input('bạn muốn tính tổng số chẵn hay lẻ(chan, le): ')
tong = 0
if cl == 'chan':
    for i in range(1, n + 1):
        if i % 2 == 0:
            tong += i
            print(f'+ thêm {i} -> tổng = {tong}')
    print(f'tổng số chẳn từ 1 đến {n} là: {tong}')
else:
    for i in range(1, n + 1):
        if i % 2 == 1:
            tong += i
            print(f'+ thêm {i} -> tổng = {tong}')
    print(f'tổng số lẻ từ 1 đến {n} là: {tong}')