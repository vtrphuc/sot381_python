so_luong = [15, 8, 22, 5, 12, 3]
ten_san_pham = ["Áo", "Quần", "Giày", "Túi", "Mũ", "Ví"]
for i in range(len(so_luong)):
    sp = ten_san_pham[i]
    sl = so_luong[i]
    if sl < 10:
        print(f"sản phẩm cần nhập là {sp} còn {sl} cái");