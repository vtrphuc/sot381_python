#tính tổng từ 1 -> n
n = int( input("nhập số n: ") )
tong = 0
for i in range(1, n+1):
    tong = tong + i
    print(f"+ thêm {i} -> tổng: {tong}")
print(f"kết quả: 1 + 2 + ... + {n} = {tong}")
