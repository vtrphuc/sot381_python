la1 = input('nhập lá thứ nhất: ').upper()
la2 = input('nhập lá thứ hai: ').upper()
la3 = input('nhập lá thứ ba: ').upper()
if la1 not in ['J', 'Q', 'K', 'A']:
    la1 = int(la1)
if la2 not in ['J', 'Q', 'K', 'A']:
    la2 = int(la2)
if la3 not in ['J', 'Q', 'K', 'A']:
    la3 = int(la3)
bai = [la1, la2, la3]
sotay = 0
diem = 0
for la in bai:
    if la not in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']:
        print(f'lá {la} không hợp lệ')
        exit()
    if la in ['J', 'Q', 'K']:
        diem += 10
        sotay += 1
    elif la == 'A':
        diem += 1
    else:
        diem += la
if la1 == la2 == la3:
    print(f'SÁP {la1}')
elif sotay == 3:
    print('BA TIÊN')
elif la1 in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10] and la2 in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10] and la3 in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if la1 == 'A':
        la1p = 1
    else:
        la1p = la1
    if la2 == 'A':
        la2p = 1
    else:
        la2p = la2
    if la3 == 'A':
        la3p = 1
    else:
        la3p = la3
    if (la1p + 1 == la2p) and (la2p + 1 == la3p):
        print(f'LIÊNG {la1} {la2} {la3}')
    elif (la1p + 1 == la3p ) and (la3p + 1 == la2p):
        print(f'LIÊNG {la1} {la3} {la2}')
    elif (la2p + 1 == la1p ) and (la1p + 1 == la3p):
        print(f'LIÊNG {la2} {la1} {la3}')
    elif (la2p + 1 == la3p ) and (la3p + 1 == la1p):
        print(f'LIÊNG {la2} {la3} {la1}')
    elif (la3p + 1 == la1p ) and (la1p + 1 == la2p):
        print(f'LIÊNG {la3} {la1} {la2}')
    elif (la3p + 1 == la2p ) and (la2p + 1 == la1p):
        print(f'LIÊNG {la3} {la2} {la1}')
    else:
        while diem >= 10:
            diem -= 10
        print(f'điểm của bạn là {diem} nút')
else:
    while diem >= 10:
        diem -= 10
    print(f'điểm của bạn là {diem} nút')