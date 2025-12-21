#Viết hàm tìm số lớn nhất và số nhỏ nhất của 3 số a, b,c
def timso(a, b, c):
    cacso = sorted( list((a, b, c)))
    return f'số lớn nhất là {(cacso[2])} và số bé nhất là {(cacso[0])}'
a = int( input('nhập số a: '))
b = int( input('nhập số b: '))
c = int( input('nhập số c: '))
print(timso(a, b, c))