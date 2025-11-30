ngay = int( input('nhập ngày(1-31) :') )
thang = int( input('nhập tháng(1-12) :') )
nam = int( input('nhập năm :') )
if ngay > 31 or ngay < 1:
    print('ngày không hợp lệ')
    exit()
if thang < 1 or thang > 12:
    print('tháng không hợp lệ')
    exit()
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    if ngay > 30:
        print('ngày không hợp lệ')
        exit()
elif thang == 2:
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        if ngay > 29:
            print('ngày không hợp lệ')
            exit()
    else:
        if ngay > 28:
            print('ngày không hợp lệ')
            exit()
print(f'ngày {ngay} tháng {thang} năm {nam} là ngày hợp lệ')