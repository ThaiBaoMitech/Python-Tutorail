#Danh sách trong python được viết trong dấu ngoặc []
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Truy cập các danh mục list bằng cách tham khảo số chỉ mục
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Thay đỗi 1 giá trị được chọn của list 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#lặp các giá trị trong list bằng lệnh for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Để xác định xem một mục được chỉ định có trong list hay không, hãy sử dụng từ khóa trong list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Xác định list có bao nhiêu mục , sử dụng method len()
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

