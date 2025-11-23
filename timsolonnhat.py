#tìm số lớn nhất

a = int( input("nhập số a:") )
b = int( input("nhập số b:") )
c = int( input("nhập số c:") )
if a > b and a > c :
    print("số lớn nhất là" ,a)
elif b > a and b > c :
    print("số lớn nhất là" ,b)
else:
    print("số lớn nhất là" ,c);