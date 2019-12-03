from multiprocessing import Pool, Lock, Queue
import os
import time

lock = Lock()
queue = Queue()

def get_num_cpu():
	return round(os.cpu_count() / 2)

def info():
	return os.getpid()

def find_duplicates(source_word):
	with open('file.txt','r') as file:
		word = file.readline()
		while word:
			if source_word == word:
				with lock:
					print(f"matched '{word.strip()}' by process id: {info()}")
					with open('duplicates-file.txt', 'a+') as duplicates_file:
						duplicates_file.writelines(word)
				queue.put(word) # thread & process safe - no need for lock
			word = file.readline()

if __name__ == '__main__':
	# count num duplicates
	# report count back to parent process
	start = time.time()

	num_cpu = get_num_cpu()
	with Pool(processes=num_cpu) as pool:
		with open('file.txt','r') as file:
			words = [file.readline() for cpu in range(num_cpu)]
			pool.map(find_duplicates, words)

	end = time.time()
	duplicate_words = []
	while not queue.empty():
		duplicate_words.append(queue.get().strip())
	print(f"\nmatched {len(duplicate_words)} duplicates in {end - start}'s using {num_cpu} cpu's")
	print(f'duplicate words: {duplicate_words}')
