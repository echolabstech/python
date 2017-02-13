# Major Sapp III 02/12/2017

# time: O(n**2) space: O(1)
def has_unique_chars(string):
	for k,c in enumerate(string, start=0):
		if c in string[k+1:]:
			return False
	return True

if __name__ == "__main__":
	print(has_unique_chars("abcdef"))