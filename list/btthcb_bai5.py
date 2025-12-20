#Kiểm tra số x có trong List không, nếu có thì ở vị trí nào
cs = [2, 1, 4, 6, 9, 7]
sokt = int( input('bạn muốn kiểm tra số nào: '))
vitri = cs.index(sokt)
print(f'có và ở vị trí số {vitri}')