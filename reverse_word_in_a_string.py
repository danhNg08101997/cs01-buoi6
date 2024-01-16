# Đảo ngược tất cả các từ trong chuỗi
# Ví dụ:
# Input: "Hello world"
# Output: "olleH dlrow"
import method
# Input
str_input = input("Nhập chuỗi ký tự: ")
# Output
str_output = ''
# Process
new_string = str_input.split(" ")
for word in new_string:
    reversed_str = method.chuoi_dao_nguoc(word)
    str_output += reversed_str + " "

print(str_output)