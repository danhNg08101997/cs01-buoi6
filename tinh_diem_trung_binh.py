# Viết chương trình yêu cầu người dùng nhập vào các thông tin điểm số toán, lý, hóa yêu cầu in ra điểm trung bình và xếp loại theo công thức sau:
# DTB = (toán + lý + hóa)/3
# Loại yếu: DTB < 5
# Loại TB: 5 <= DTB < 6.5
# Loại Khá: 6.5 <= DTB < 8
# Loại Giỏi: 8 <= DTB <= 10
# Không xếp loại: trường hợp còn lại

# input
diem_toan = float(input("Nhập điểm toán: "))
diem_ly = float(input("Nhập điểm lý: "))
diem_hoa = float(input("Nhập điểm hóa: "))
# output
diem_trung_binh = 0
xep_loai = ''
# process
# Không có function
# tong_diem = diem_toan + diem_ly + diem_hoa
# diem_trung_binh = tong_diem / 3
# if diem_trung_binh < 5:
#     xep_loai = 'Loại yếu'
# elif 5 <= diem_trung_binh < 6.5:
#     xep_loai = 'Loại TB'
# elif 6.5 <= diem_trung_binh < 8:
#     xep_loai = 'Loại Khá'
# elif 8 <= diem_trung_binh <= 10:
#     xep_loai = 'Loại Giỏi'
# else:
#     xep_loai = 'Không xếp loại'
# print(f'Điểm trung bình - {diem_trung_binh} - được xếp loại {xep_loai}')

# Có function
def tinh_diem_trung_binh(dToan, dLy, dHoa):
    '''
    Hàm này nhận vào các giá trị 
    input: điểm toán, lý, hóa
    output: điểm trung bình được tính theo công thức (điểm toán + điểm lý + điểm hóa)/3
    '''
    output = 0
    output = (dToan + dLy + dHoa) / 3
    return output

def xep_loai_sinh_vien(dtb):
    if dtb < 5:
        xep_loai = 'Yếu'
    elif 5 <= dtb < 6.5:
        xep_loai = 'Trung Bình'
    elif 6.5 <= dtb < 8:
        xep_loai = 'Khá'
    elif 8 <= dtb <= 10:
        xep_loai = 'Giỏi'
    else:
        xep_loai = 'Không xếp loại'
    return xep_loai

diem_trung_binh = tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa)
xep_loai = xep_loai_sinh_vien(diem_trung_binh)
print(f'Điểm trung bình {diem_trung_binh} - được xếp loại {xep_loai}')