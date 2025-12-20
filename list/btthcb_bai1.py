#Nhập 5 số từ bàn phím vào List và tính tổng
s1 = int( input('nhập số thứ nhất: '))
s2 = int( input('nhập số thứ hai: '))
s3 = int( input('nhập số thứ ba: '))
s4 = int( input('nhập số thứ tư: '))
s5 = int( input('nhập số thứ năm: '))
cs = list((s1, s2, s3, s4, s5))
tong = sum(cs)
print(tong)