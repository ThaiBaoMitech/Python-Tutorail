#Sử dụng kết hợp type và lệnh print để xuất ra kiểu dữ liệu của biến vừa khai báo
x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))


#Chuyển đỗi từ kiểu dữ liệu này sang kiểu dữ liệu khác
x = 1 # int
y = 2.8 # float
z = 1j # complex

#convert từ int thành float:
a = float(x)

#convert từ float thành int:
b = int(y)

#convert từ int thành complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
