#Tạo 1 class đơn giản
class myclass:
    x="41"        
#gọi class vừa tạo
p1 = myclass()
print(p1.x)

##
class Demo:
    def __init__(self,name, age):
        self.name = name
        self.age = age
p1 = Demo("Bảo",23)
p2 = Demo("Tùng",22)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

####
class Person:
  def __init__(thamchieu, name, age):
    thamchieu.name = name
    thamchieu.age = age

  def myfunc(giatri):
    print("Tôi tên là " + giatri.name)
p1 = Person("John", 36)
p1.myfunc()


