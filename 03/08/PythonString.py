#Lấy 1 kí tự từ chuối(Lưu ý kí tự đầu tiên có vị trí là 0)
a = "Hello, World!"
print(a[1])

#Láy kí từ từ vị trí số 2 đến số 5

b = "Hello, World!"
print(b[2:5])

#Sử dụng strip() để loại bỏ khoảng trắng ở đầu dòng và cuối dòng
c = " Hello, World! "
print(c.strip())

#method len() trả về độ dài của chuổi
d= "Hello, World!"
print(len(d))

#Method low() trả chuổi có kí tự hoa về kí tự thường
e = "Hello, World!"
print(e.lower())


#Method upper() trả chuỗi thành dạng kí tự hoa
f = "Hello, World!"
print(f.upper())

#Method replace() Thay thế chuỗi bằng 1 chuỗi khác
g = "Hello, World!"
print(g.replace("World","Bao"))

#Method Split() phân tách chuỗi thành các chuỗi con nếu tìm thấy kí tự đã cho
h = "Hello, World!"
print(h.split(","))


#Method format () lấy số lượng đối số không giới hạn và được đặt vào các phần giữ chỗ tương ứng:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) #có thể sử dụng các index number để các đối số có sự chính xác

