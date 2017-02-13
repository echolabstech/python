import hashtable

def has_duplicate_chars(string):
	container = ""
	for k,c in enumerate(string, start=0):
		if c not in container:
			container += c
		else:
			return True
	return False

if __name__ == "__main__":
	string = "bcasdf"
	print(has_duplicate_chars(string))