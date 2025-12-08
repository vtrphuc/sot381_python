so = int( input('nhập số lá bài của bạn(2-5): ') )
if so < 2 or so > 5:
    print('số lá bài không hợp lệ')
    exit()
elif so == 2:
    la_1 = input('nhập lá bài thứ nhất: ')
    la_2 = input('nhập lá bài thứ hai: ')
    if la_1 in ['J', 'Q', 'K']:
        la_1 = 10
    elif la_1 == 'A':
        la_1 = 11
    else:
        la_1 = int(la_1)
    if la_2 in ['J', 'Q', 'K']:
        la_2 = 10
    elif la_2 == 'A':
        la_2 = 11
    else:
        la_2 = int(la_2)
    diem = la_1 + la_2
    if diem == 22:
        print('XÌ BÀN')
        exit()
    elif diem == 21:
        print('XÌ DÁCH')
        exit()
    print(f'điểm của bạn là {diem}')
elif so == 3:
    la_1 = input('nhập lá bài thứ nhất: ')
    la_2 = input('nhập lá bài thứ hai: ')
    la_3 = input('nhập lá bài thứ ba: ')
    la_bai = [la_1, la_2, la_3]
    diem = 0
    so_At = 0
    for la in la_bai:
        if la in ['J', 'Q', 'K']:
            diem = diem + 10
        elif la == 'A':
            diem = diem + 11
            so_At = so_At + 1
        else:
            diem = diem + int(la)
    while diem > 21 and so_At > 0:
        diem = diem - 1
        so_At = so_At - 1
        if diem > 21:
            diem = diem - 9
    if diem <= 21:
        print(f'điểm của bạn là {diem}')
    else:
        print(f'QUẮC {diem} điểm')
elif so == 4:
    la_1 = input('nhập lá bài thứ nhất: ')
    la_2 = input('nhập lá bài thứ hai: ')
    la_3 = input('nhập lá bài thứ ba: ')
    la_4 = input('nhập lá bài thứ tư: ')
    la_bai = [la_1, la_2, la_3, la_4]
    diem = 0
    so_At = 0
    for la in la_bai:
        if la in ['J', 'Q', 'K']:
            diem = diem + 10
        elif la == 'A':
            diem = diem + 11
            so_At = so_At + 1
        else:
            diem = diem + int(la)
    while diem > 21 and so_At > 0:
        diem = diem - 1
        so_At = so_At - 1
        if diem > 21:
            diem = diem - 9
    if diem <= 21:
        print(f'điểm của bạn là {diem}')
    else:
        print(f'QUẮC {diem} điểm')
else:
    la_1 = input('nhập lá bài thứ nhất: ')
    la_2 = input('nhập lá bài thứ hai: ')
    la_3 = input('nhập lá bài thứ ba: ')
    la_4 = input('nhập lá bài thứ tư: ')
    la_5 = input('nhập lá bài thứ năm: ')
    diem = 0
    so_At = 0
    la_bai = [la_1, la_2, la_3, la_4, la_5]
    for la in la_bai:
        if la in ['J', 'Q', 'K']:
            diem = diem + 10
        elif la == 'A':
            diem = diem + 11
            so_At = so_At + 1
        else:
            diem = diem + int(la)
    while diem > 21 and so_At > 0:
        diem = diem - 1
        so_At = so_At - 1
        if diem > 21:
            diem = diem - 9
    if diem <= 21:
        print(f'NGŨ LINH {diem} điểm')
    else:
        print(f'QUẮC {diem} điểm')