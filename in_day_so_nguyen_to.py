# Cho phép người dùng nhập vào 1 số n bất kỳ. In ra các số nguyên tố từ 2 đến nhỏ hơn bằng n (nếu n là số nguyên tố)
import method
# Input
so_n = int(input('Nhập vào số n: '))
# Output
output = ''
# Process
for so_hang in range(2, so_n + 1):
    if method.kiem_tra_so_nguyen_to(so_hang):
        output += str(so_hang) + ' '

if output != '':
    print(f'Các số nguyên tố từ 2 - {so_n}: {output}')
else:
    print('Không có số nguyên tố nào cả!')