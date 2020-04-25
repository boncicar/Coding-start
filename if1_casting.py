age = input('請輸入年齡: ')
age = int(age) #此行為型別轉換。如果沒有把age轉換成int型式，原本的age會是str型式，因此在cmd中若輸入30的話，此30會是str而非int而無法與20做比較，執行此程式會出現TypeError。故要把age轉換成int的型式。
if age >= 20: #因為age已經轉換成int，所以int才能跟int做比較。if指令最後一定要加冒號。
	print('你可以投票')