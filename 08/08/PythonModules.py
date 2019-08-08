#sử dụng module bằng cách sử dụng lệnh import
# cú pháp <import> <tên module>
#Lấy file module mymodule đã tạo trước đó
import mymodule
#cú pháp sử dụng chức năng của mmodule
# <tên module>.<tên chức năng>(<biến giá trị>)
mymodule.greeting("Bảo")

#gọi thuộc thính từ trong mảng của module
import mymodule as mx  # có thể đặt tên bất kì với module vừa import bằng từ khoá "as". lưu ý nếu đã đặt tên mới sẽ không gọi lại được tên cũ
a = mymodule.person1["name"]  # thay vì gọi tên chính của module ta có thể gọi tên mới vừa đặt
print(a)

##sử dụng module tích hợp trong pyth
import platform
x = platform.system()
print(x)
## sử dụng hàm dựng sẳn "dif()" để liệt kê tất cả các hàm (hoặc tên biến) trong một module
#có thể sử dụng "dif()" trên tất cả các module từ module tích hợp tới module tự tạo
x = dir(mymodule)
print(x)
#chọn chỉ nhập các phần tử từ module bằng từ khoá from
#VD: Chỉ nhập phần từ person1 từ mô đun mymodule
from mymodule import person1 # Lưu ý khi sử dụng từ khoá from không cần sử dụng tên mô đun khi tham chiếu đến các phần tử
print(person1["age"])  # lấy ra thuộc tính age

mymodule.greeting(person1["name"])
print("Tôi ",person1["age"],"tuổi")