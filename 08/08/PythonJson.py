###JSON là một cú pháp để lưu trữ và trao đỗi dữ liệu
###JSON là văn bản , được viết bằng kí hiệu đối tượng JAVASCRIPT
###JSON có một gói tích hợp json , có thể sử dụng để làm việc với JSON
import json
##Chuyển đỗi từ json sang python sử dụng phương thức "json.load(<biến json>)":
x =  '{ "name":"John", "age":30, "city":"New York"}'
#chuyển đổi x
y = json.loads(x)
#dãy json đã trở thành một dictionaries
print(y["city"])

##Chuyễn đỗi từ python sang json sử dụng phương thức "json.dumps(<biến python>)":
#một đối tượng python (vd : dictionaries)
x = {"Firstname" : "Thai","Lastname" : "Bao","Birtday":1996 }
#convert thành json
y = json.dumps(x)
print(y)

###Có thể chuyển đỗi một số Python object thành các chuỗi json:	

#													Python 				JSON
print(json.dumps({"name": "John", "age": 30}))	#dạng dictionaries	-->Object
print(json.dumps(["apple", "bananas"]))			#dạng  list			-->Array
print(json.dumps(("apple", "bananas")))			#dạng tuple			-->Array
print(json.dumps("hello"))						# dạng string		-->String
print(json.dumps(42))	 						#dạng int			-->Number
print(json.dumps(31.76))						#dạng float			-->Number
print(json.dumps(True))							#dạng True			-->true
print(json.dumps(False))						#dạng False			-->false
print(json.dumps(None))							#dạng None			-->null


###Chuyển đỗi một Python Objects chứa tất cả các loại dữ liệu hợp lệ
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))  #in ra dãy json nhưng khó nhìn 
print(json.dumps(x, indent=6))# dễ nhìn hơn khi sử dụng indent(tham sô để xác định số lượng thụt lề)
print("Sửu dụng separators")	# sử dụng separators tham số để thay đỗi các dấu phân cách mặt định
print(json.dumps(x, indent=4, separators=(". ", " = "))) 
print('Sử dụng sort_keys')# sử dụng sort_key chỉ định xem kết quả có nên được sắp xếp hay không
print(json.dumps(x, indent=4, sort_keys= True))