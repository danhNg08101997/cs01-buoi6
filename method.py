import math
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

def kiem_tra_so_nguyen_to(so):
    output = True
    if so < 2:
        output = False
    uoc = 2
    while uoc <= math.sqrt(so):
        if so % uoc == 0:
            output = False
            break
        uoc += 1
    return output