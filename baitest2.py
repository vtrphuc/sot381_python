#viết chương trình nhập vào một số kiểm tra xem có chia hết cho 3 và 5 hay không
n = int(input('nhập số nguyên n: '))
if n % 3 == 0 and n % 5 == 0:
  print(f'{n} chia hết cho 3 và 5')
else:
  print(f"{n} không chia hết cho 3 và 5")
