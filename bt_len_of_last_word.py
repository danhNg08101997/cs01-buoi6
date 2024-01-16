# Cho 1 chuỗi chứa các ký tự và khoảng trắng, trả về độ dài của từ cuối cùng trong chuỗi. Nếu từ cuối cùng không tồn tại trả về 0. Một từ được định nghĩa là một chuỗi ký tự liên tiếp không chứa khoảng trắng

# Input
str_input = input('Nhập chuỗi ký tự: ')
# Output
output = 0
# Process
new_string = str_input.split(" ")

last_word = new_string[len(new_string) - 1]
output = len(last_word)
print(output)