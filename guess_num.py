import random
r = random.randint(1, 100)
while True:
	guess = input("請輸入數字")
	guess = int(guess)
	if guess == r:
		print ("你猜對了")
		break
	elif guess > r :
		print("你猜錯大")
	elif guess < r:
		print("比答案小")