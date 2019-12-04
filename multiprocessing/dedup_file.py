from multiprocessing import Pool, Lock, Queue
import os
import time

lock = Lock()
queue = Queue()
deduped_file = open('deduped-file.txt', 'w+')
CPU_COUNT_RATIO = 1 # exm: 1 = 100%

def get_num_cpu():
	return round(os.cpu_count() / CPU_COUNT_RATIO)

def info():
	return os.getpid()

def dedup_file(source_word):
	with open('deduped-file.txt','r') as file:
		duplicate_found = False
		word = file.readline()
		while word:
			if source_word.strip() == word.strip():
				print(f"duplicate found: '{source_word.strip()}' by process id: {info()}")
				duplicate_found = True
				break
			word = file.readline()
	if not duplicate_found:
		with lock:
			deduped_file.writelines(source_word)
			deduped_file.flush()

def get_word():
	with open('file.txt','r') as file:
		word = file.readline()
		while word:
			yield word
			word = file.readline()

if __name__ == '__main__':
	start = time.time()

	num_cpu = get_num_cpu()
	with Pool(processes=num_cpu) as pool:
		pool.map(dedup_file, get_word())

	end = time.time()
	deduped_file.close()
	print(f"\nwrote unique words in {end - start}'s using {num_cpu} cpu's")
