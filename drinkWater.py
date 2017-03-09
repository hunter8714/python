drinkWater = 0
while drinkWater<20:
	drinkWater = drinkWater + 1
	percent = drinkWater*5
	print ("%d번째 모금. 홀짝!"%drinkWater)
	print ("물을 %d퍼센트 마셨습니다."%percent)
	if drinkWater== 20:
		print("물을 다 마셔버렸네요.")

