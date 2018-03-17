import random
def make_quetion():
	x = random.randint(1,100)
	y = random.randint(1,100)
	giho = random.randint(1,3)
	if giho == 1:
		giho = '+'
	elif giho == 2:
		giho = '-'
	elif giho == 3:
		giho = '*'
	quetion = str(x) + giho + str(y)
	return quetion
while_key = True
while while_key:
	print ('랜덤으로 나오는 문제들을 풀어주십시오.')
	quetion = make_quetion()
	r_a = eval(quetion)
	print ('이 문제의 답을 입력해 주세요.\n' + quetion + ' = ?')
	u_a = input()
	if int(u_a) == r_a:
		print("맞았습니다!")
	else:
		print("틀렸네요.")
	if_q = input('더 하시겠습니까?(y/n)')
	if if_q == 'n':
		while_key = False
	elif if_q != 'n''y':
		print('알 수 없는 대답이네요.')
			
	
			
