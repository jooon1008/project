import turtle as t
import random as r
def up(): #거북이가 왼쪽으로 고개를 돌림 
	t.left(2)
def down(): #거북이가 오른쪽으로 고개를 돌림
	t.right(2)
def fire(): #거북이 발사
	ang = t.heading()
	while t.ycor() > 0:
		t.color = ('black')
		t.down
		t.fd(15)
		t.right(4)
	dis = t.distance(target,0)
	t.sety(r.randint(10,100))
	if dis < 25:
		t.color = ('red')
		t.write("good",False,"center",("",15))
	else:
		t.color = ('yellow')
		t.write("bad",False,"center",("",15))
	
	t.goto(-200,10)
	t.setheading(ang)
		
t.color('blue')
t.goto(-300,0)
t.down()
t.goto(300,0)
t.up()
target = r.randint(50,150)
t.goto(target - 25,0)
t.down()
t.pensize(7)
t.color('green')
t.goto(target + 50,0)
t.up()
t.goto(-200,10)
t.onkeypress(up,'Up')
t.onkeypress(down,'Down')
t.onkeypress(fire,'space')
loc = t.pos()
t.listen()
t.mainloop()




