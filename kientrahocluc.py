#xếp loại học lực

diem = float( input("nhập số điểm:") )
if diem > 10 or diem < 0:
    print("điểm không hợp lệ")
elif diem >= 8:
    print("học sinh giỏi")
elif diem >= 6.5:
    print("học sinh khá")
elif diem >= 5:
    print("học sinh trung bình")
else:
    print("học sinh yếu");