# Viết chương trình cho phép người dùng nhập vào chuỗi số yêu cầu in ra các chữ số trong chuỗi là số nguyên tố, nếu không có số nguyên tố nào trong chuỗi thì in ra kết quả là không có số nguyên tố nào cả
import method

# Input
str_input = input("Nhập vào chuỗi số: ")
# Output
output = ''
# Process
for str_num in str_input:
    num = int(str_num)
    if method.kiem_tra_so_nguyen_to(num):
        output += f'{num} '
print(f'Các số nguyên tố của dãy số {str_input} là: {output}')
