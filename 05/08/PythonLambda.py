# cú pháp lambda :  <giá trị truyền vào>= lambda <tham số>:<biểu thức> 
x = lambda a: a *3
print(x(3))

#có thể có nhiều tham số nhưng chỉ có 1 biểu thức
x = lambda a, b, c : a+ 3* b/ 2 -c
print(x(4, 3, 12))

#sử dụng lambda làm chức hàm ẩn danh
def giatrian(x):
    return lambda a: a * x
giatrinhap1 = giatrian(10)
giatrinhap2 = giatrian(20)
print(giatrinhap1(30))
print(giatrinhap2(100))