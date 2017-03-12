coffee = 10
while 1:
	money = int(input("insert coin plz: "))
	if money == 300:
		print("커피를 줍니다")
		coffee -= 1
		print ("남은 커피의 수량은 %d캔입니다"%coffee)
	elif money > 300:
		print ("거스름돈 %d원을 주고 커피를 줍니다."%(money -300))
		coffee -= 1
		print ("남은 커피의 수량은 %d캔입니다"%coffee)
	else:
		print("돈이 부족합니다. 돈을 반환합니다.")
		print("남은 캔커피의 수량은 %d 캔 입니다" % coffee)
	if not coffee:
		print("커피가 다 떨어졌습니다. 판매를 중지합니다. ")
		break

