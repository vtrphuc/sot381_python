def dem(tu):
    sotu = tu.split()
    return len(sotu)
tu = input('nhập văn bản: ')
print(f'số từ: {dem(tu)}')