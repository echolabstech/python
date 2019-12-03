from multiprocessing import Pool
import os

def f(name):
	print('hello', name)
	print('parent process:', os.getppid())
	print('process id:', os.getpid())

if __name__ == '__main__':
	names = ['Jerome', 'Major', 'Anthony', '欢欢', 'Alice']
	with Pool(5) as p:
		p.map(f, names)