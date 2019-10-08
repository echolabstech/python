from tasks import fetch_url
import time

search_terms = [search_term.strip() for search_term in open('search_terms.txt')]

tasks=[]
url = 'http://www.baidu.com/s?wd=test'
for search_term in search_terms[:10]:
	tasks.append(fetch_url.delay(url + search_term))

# collect results when available, igoring exceptions
start = time.time()
retry = True
while (retry):
	retry = not any([task.ready() for task in tasks])
	if time.time() - start >= 5:
		retry = False
results = [task.get(propagate=False) for task in tasks if task.ready()]
print(results)
