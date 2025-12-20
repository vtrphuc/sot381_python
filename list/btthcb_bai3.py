#Nhập List số nguyên, đếm số chẵn và số lẻ
cs = [3, 5, 2, 1, 6, 3, 7, 5, 10, 4]
sochan = []
sole = []
for i in cs:
    if i % 2 == 0:
        sochan.append(i)
    else:
        sole.append(i)
slsc = len(sochan)
slsl = len(sole)
print(f'số lượng số chẵn là {slsc}')
print(f'số lượng số lẻ là {slsl}')