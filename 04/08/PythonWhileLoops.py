"""chạy vòng lặp while với với điều kiện i <6
tăng biến đếm i nếu không vòng lặp sẽ chạy vv với điều kiện """
i = 1
while i<6:
	print(i)
	i+=1

"""dừng vòng lặp while khi điều kiện i==3 đúng với lệnh break"""
i = 1
while i<6:
	print(i)
	if i==3:
		break
	i+=1

#tiếp tục chạy vòng lặp while in ra i khi cả điều kiện i==3: đúng với lệnh continue
i = 1
while i<6:
	i+=1
	if i==3:
		continue
	print(i)


