from tasks import add

tasks = []
for num in range(10):
	tasks.append(add.delay(num, num))
results = [task.get(propagate=False) for task in tasks if task.ready()]
print(results)
