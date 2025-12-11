s1 = int( input('nhập số thứ nhất: '))
s2 = int( input('nhập số thứ hai: '))
s3 = int( input('nhập só thứ ba: '))
if s1 > s2 and s1 > s3:
    if s2 > s3:
        print(f'{s1} > {s2} > {s3}')
    else:
        print(f'{s1} > {s3} > {s2}')
elif s2 > s3 and s2 > s1:
    if s1 > s3:
        print(f'{s2} > {s1} > {s3}')
    else:
        print(f'{s2} > {s3} > {s1}')
else:
    if s2 > s1:
        print(f'{s3} > {s2} > {s1}')
    else:
        print(f'{s3} > {s1} > {s2}')