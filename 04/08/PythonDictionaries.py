"""
Một dictionary là một bộ không có thứ tự có thể thay đổi và lập chỉ mục.
 Trong python dictionary được viết trong dấu ngoặc nhọn và chúng có các khóa giá trị
"""
thisdict= {
	"FirstName":"Thái",
	"LastName":"Bảo",
	"BirthDay" : 1996
}
print(thisdict)

#có thể truy xuất dữ liệu của các dictionary bằng cách tham khảo tên tên của nó bên trong dấu []
x = thisdict["LastName"]
print(x)
#Hoặc có thể sử dụng method get()
y= thisdict.get("FirstName")
print(y)

#Thay đỗi giá trị
thisdict["BirthDay"]="04/04/1996"
print(thisdict)

#Sử dụng lệnh for để lặp dictionary
#in ra các tên khóa trong dictionary
for x in thisdict:
	print(x)	#Lưu ýt: Trong python thục lề(tab) để thực hiện câu lệnh nếu không sẽ báo lỗi

#In ra các giá trị
for x in thisdict:
	print(thisdict[x])
#Hoặc sử dụng function values()
for x in thisdict.values():
	print(x)

#Sử dụng function items() để lặp qua cả tên khóa và giá trị
for x, y in thisdict.items():
	print(x, y)

