"""Ngày trong python không phải là kiễu dữ liệu, nhưng chúng ta có thể nhập một module tích hợp
có tên datetime để làm việc với các ngày như các đối tượng ngày"""
import datetime
x = datetime.datetime.now() #Thời gian hiện tại hôm nay

#sử dụng phương thức "strftime()" để định dạng ngày tháng thành chuối có thể đọc được.
print(x.strftime("%A"))	#Thứ trong tuần(bằng chữ)
print(x.strftime("%B"))	#Tháng trong năm(bằng chữ)

##Tạo đối tượng ngày
x = datetime.datetime(2015,11,22)
print(x)



