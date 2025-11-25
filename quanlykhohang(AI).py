so_luong = [15, 8, 22, 5, 12, 3]
ten_san_pham = ["Áo", "Quần", "Giày", "Túi", "Mũ", "Ví"]
kho_hang = dict(zip(ten_san_pham, so_luong))
toi_thieu = 10
for sp, sl in kho_hang.items():
    if sl < toi_thieu:
        print(f"sản phẩm cần nhập là {sp} chỉ còn {sl} cái")