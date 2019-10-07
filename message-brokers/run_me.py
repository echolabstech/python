from tasks import add

for num in range(10000):
	add.delay(num, num)