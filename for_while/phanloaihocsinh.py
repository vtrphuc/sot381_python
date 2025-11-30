diem_so = [8.5, 7.0, 9.2, 6.8, 5.5, 8.8]
for diem in diem_so:
    if diem >= 8:
        xep_loai = "giỏi"
    elif diem >= 6.5:
        xep_loai = "khá"
    elif diem >= 5:
        xep_loai = "trung bình"
    else:
        xep_loai = "yếu"
    print(f"điểm: {diem} -> xếp loại {xep_loai}")
    
        
    