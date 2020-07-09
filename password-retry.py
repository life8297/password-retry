# 密碼重試程式
x = 3
password = 'a123'
while True:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('登入成功')
		break
	else:
		x = x - 1
		print('密碼錯誤請重新輸入, 還有', x, '次機會')	
		if x == 0:
			print('帳戶已凍結')
			break