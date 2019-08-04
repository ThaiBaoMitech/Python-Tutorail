#một hàm được định nghĩa bằng từ khóa def
def my_function():
    print("Hello from a function")

#để gọi 1 hàm ta gọi tên hàm kèm theo dấu ()    
my_function()

#truyền tham số
def hello(fruits):
    print(fruits + " táo")
hello("tôi muốn ăn")

#sử dụng tham số mặt định
def hello(fruits =" Nho"):
    print("Tôi muốn ăn"+ fruits)
hello()             #sử dụng tham số mặt định
hello(" Chuối")     #sử dụng truyền tham số

#truyền tham số dưới dạng danh sách:
def menu(food):
	for x in food:
		print(x)

tea=["olong","O độ","bí đao","đào"]
menu(tea)

#sử dụng return để trả hàm về một giá trị
def hamgiatri():
    return 5
print(hamgiatri())


#Đệ quy
def recursion(k):
    if k>0:
        result = k + recursion(k-1)
        print(result)
    else:
        result = 0
    return result
recursion(6)
print("\nRecursion Example Resutls")
