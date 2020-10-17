"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'		# This is the our dictionary file
LEVEL = 4					# The rows of the letters
DIC_NAMES = []				# The list of names from FILE
ans = []					# The list of words from Boggle
tmp = []					# The list of visited point
count = 0


def main():
	"""
	TODO:
	"""

	target = []
	read_dictionary()

	for i in range(LEVEL):
		t = []
		s = input(f'{i+1} row of letters: ')
		if check_input(s):
			print('Illegal input')
			break
		else:
			for ch in s:
				if ch.isalpha():
					t.append(ch.lower())
			target.append(t)

	find_boggle(target, '')
	print(f'Ans = {ans}')
	print(f'There are {len(ans)} words in total')
	# print(f'{count}')


def find_boggle(t, curr):
	"""
	This function will resolve the boggle game.
	:param t: The target string
	:param curr: The current string
	"""
	global DIC_NAMES
	global ans
	global tmp
	global count
	count += 1
	valid_grid = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]		# Neighbor zone

	if curr in DIC_NAMES and curr not in ans:
		# Base case : The current string is in the dictionary and not been found yet.
		ans.append(curr)
		print(f'Found: "{ans[len(ans)-1]}"')
		# Keep checking is there any longer word in the dictionary starts with current string
		if has_prefix(curr):
			find_boggle(t, curr)
	else:
		for x in range(len(t)):
			for y in range(len(t)):
				ch = t[x][y]
				point = (x, y)
				# Handle the first letter
				if len(tmp) == 0:
					# Choose
					tmp.append(point)
					curr += ch
					if has_prefix(curr):
						# Explore
						find_boggle(t, curr)
					# Un-choose
					curr = curr[:-1]
					tmp = tmp[:-1]
				else:
					# Check the new letter is in the neighbor zone
					if point not in tmp and (point[0]-tmp[len(tmp)-1][0], point[1] - tmp[len(tmp)-1][1]) in valid_grid:
						tmp.append(point)
						curr += ch
						if has_prefix(curr):
							find_boggle(t, curr)
						curr = curr[:-1]
						tmp = tmp[:-1]


def check_input(s):
	"""
	This function checks the input is in correct format or not
	:param s: The input string of each row
	:return: (bool) If the input format is correct
	"""
	for i in range(len(s)):
		if i % 2 == 1 and s[i] != ' ':
			return True
		elif len(s) != 7:
			return True
		elif i % 2 == 0 and s[i].isalpha() is False:
			return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global DIC_NAMES
	with open(FILE) as f:
		for line in f:
			name = line.strip()
			if len(name) >= 4:
				DIC_NAMES.append(name)


def has_prefix(sub_s):
	"""
	This function will check is there any word starts with the given sub string.
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	flag = 0
	for name in DIC_NAMES:
		if name.startswith(sub_s):
			flag += 1

	if flag > 0:
		return True
	return False


if __name__ == '__main__':
	main()
