x = int( input('x = '))
y = int( input('y = '))
if x == 0 and y == 0:
    print('điểm ({x},{y}) nằm ở tạo độ (0,0)')
elif x == 0:
    print(f'điểm ({x},{y}) nằm trên trục tung')
elif y == 0:
    print(f'điểm ({x},{y}) nằm trên trục hoành')
elif x > 0 and y > 0:
    print(f'điểm ({x},{y}) nằm ở góc phần tư I')
elif x < 0 and y > 0:
    print(f'điểm ({x},{y}) nằm ở góc phân tư II')
elif x < 0 and y < 0:
    print(f'điểm ({x},{y}) nằm ở góc phần tư III')
else:
    print(f'điểm ({x},{y}) nằm ở góc phần tư IV')