###Tạo 1 lớp và lớp đầu tiên sẽ là lớp cha
class Lopcha:
	def __init__(giatrilopcha, fname, lname):  #def là từ khoá khi tạo 1 hàm
		giatrilopcha.firstname = fname
		giatrilopcha.lastname = lname

	def printname(ingiatrilopcha): #cú pháp def <tên hàm>([Tham số truyền vào])
		print(ingiatrilopcha.firstname, ingiatrilopcha.lastname)  # phương thức của lớp cha

class Lopcon(Lopcha):  #Tạo 1 lớp con và kế thừa toàn bộ thuộc tính và phương thức từ lớp cha
	pass   #sử dụng từ khoá pass nếu không muốn thêm bất kì phương thức hay thuộc tính nào vào lớp con

x = Lopcon("Thái", " Bảo")  #Tạo 1 đối tượng với các thuộc tính của lớp con
x.printname()    #gọi hàm printname vừa tạo


#####################################################################################################
#Sử dụng hàm __init__ khi tạo lớp con
class Lopcha:
	def __init__(giatrilopcha, fname, lname): 
		giatrilopcha.firstname = fname
		giatrilopcha.lastname = lname

	def printname(ingiatrilopcha):
		print(ingiatrilopcha.firstname, ingiatrilopcha.lastname)  # phương thức của lớp cha

class Lopcon(Lopcha):
#Khi sử dụng __init__ ở lớp con sẽ không kế thừa chức năng của lớp cha
	def __init__(giatrilopcha, fname, lname, age):
#để giữ quyền thừa kế __init__ của lớp cha , thêm 1 __init__ gọi lớp cha
		Lopcha.__init__(giatrilopcha, fname, lname)
		#Có thể thêm thuộc tính vào lớp con
		giatrilopcha.age = age

	def phuongthuc(inphuongthuc):
		print(inphuongthuc.firstname,inphuongthuc.lastname,"Năm nay nó", inphuongthuc.age)

x = Lopcon("Thằng","Bờm",18) #tạo đối tượng có thuộc tính của lớp con
y = Lopcha("Tùng","tùng") # tương tựơng có thuộc tính của lớp cha
x.phuongthuc()#Gọi hàm chứa phương thức, cú pháp : <Tên đối tượng>.<Tên hàm>()
y.printname()# gọi hàm chứa phương thức của lớp cha