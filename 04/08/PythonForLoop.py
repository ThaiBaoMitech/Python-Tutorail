#lặp danh sách trái cây
fruits =["mango","cherry","banana"]
for x in fruits:
    print(x)

#lặp qua một đối tượng
for x in "banana":
    print(x)

#dừng vòng lặp tại điều kiện dừng với break
fruits=["applle","banana","mango","cherry"]
for x in fruits:
    print(x)
    if x == "mango":
        break
  
#tương tự nhưng dừng trước khi in điều kiện 
fruits=["applle","banana","mango","cherry"]
for x in fruits:
    if x == "mango":
        break
    print(x)

#với lệnh continue trong vòng lặp for sẽ dừng vòng lặp hiện tại của vòng lặp và thực hiện câu lệnh tiếp
fruits=["applle","banana","mango","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#function range()
for x in range(6):  #đánh số bắt đầu mặc định là 0
    print(x)
#tuy nhiên tham số bắt đầu có thể được chỉ định đúng
for x in range(2,6):  #không bao gồm 6
    print(x)
#mặc định tăng chuối lên 1 nhưng có thể thay đỗi giá trị tăng khi thêm 1 tham số thứ 3
for x in range(2,100,3):
    print(x)

#các lệnh else trong vòng lặp for xác định một khối lệnh được thực thi khi vòng lặp kết thúc:
for x in range(2,44,3):
    print(x)
else:
    print("Hello World!")

chuoia=["qe","đưa","fkhw"]
chuoib=["fằ","đă","dằ"]
for x in chuoia:
    for y in chuoib:
        print(x,y)