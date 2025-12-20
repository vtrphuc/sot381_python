#Tạo List có 10 số, tìm số lớn nhất và nhỏ nhất
cs = []
while True:
    so = int( input('nhập số: '))
    cs.append(so)
    if len(cs) == 10:
        break
sln = max(cs)
snn = min(cs)
print(cs)
print(f'số lớn nhất là:{sln}')
print(f'số nhỏ nhất là:{snn}')