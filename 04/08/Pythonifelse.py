#câu điều kiện if 
a =10
b=20
if a< b:
	print("a < b")

#câu điều kiện if ... else
a =100
b=100
if a>b:
	print("a lơn hơn b")
else:
	print("a bằng b")

#câu điều kiện if... elif... else
#Nếu điều kiện đầu không đúng thì so sánh điều kiện tiếp theo 
a =10
b =20
if a> b:
	print("a lớn hơn b")
elif a==b:
	print("a bằng b")
else:
	print("a bé hơn b")


#sử dụng từ toán tử logic kết hợp với câu điều kiện
a=10
b=20
c=20
if a >b and c>a:
	print("đúng với cả 2 trường hợp")
elif a>b or b>c:
	print("đúng với 1 trường hợp trong 2 trường hợp")
elif b==c:
	print("Đúng với trường hợp này")
else:
	print("Không có trường hợp nào đúng")
