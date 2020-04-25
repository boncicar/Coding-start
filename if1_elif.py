age = input('請輸入年齡: ')
age = int(age)
if age <= 12:
	print('讀國小')
elif age >= 13 and age <= 15:
	print('讀國中')
elif age >= 16 and age <= 18:
	print('讀高中')
elif age >= 19 and age <= 22:
	print('讀大學')
else:
	print('出社會')
