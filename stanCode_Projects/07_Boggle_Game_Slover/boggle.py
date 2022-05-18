"""
File: boggle.py
Name:Zoey
----------------------------------------
Find all words in 4x4 boggle game, and the length of word is more than or equal to 4.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
dictionary = []


def main():
	board = []
	for i in range(4):
		row = input(f'{i+1} row of letter: ').lower().split()
		if not check_format(row):
			print('Illegal format')
			break
		else:
			board.append(row)
	start = time.time()
	read_dictionary()
	find_words(board)
	end = time.time()
	print('-----------------------------------------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')
	print('-----------------------------------------------------------------')


def find_words(board):
	"""
	:param board: list, [['f','y','c','l'], ['i','o','m','g'],['o','r','i','l'],['h','j','h','u']]
	"""
	word_lst = []
	for row in range(4):
		for col in range(4):
			word = board[row][col]
			row_col = [(row, col)]		# list stored the row & col of board
			find_word_helper(board, word, row_col, word_lst)
	print(f'There are {len(word_lst)} words in total.')


def find_word_helper(board, word, row_col, word_lst):
	if len(word) >= 4:
		if word in dictionary:
			if word not in word_lst:
				print(f'Found "{word}"')
				word_lst.append(word)
	for x in range(-1, 2, 1):
		for y in range(-1, 2, 1):
			row = row_col[-1][0] + x
			col = row_col[-1][1] + y
			if 0 <= row < 4 and 0 <= col < 4:
				if (row, col) not in row_col:
					# Choose
					word += board[row][col]
					row_col.append((row, col))

					if has_prefix(word):
						# Explore
						find_word_helper(board, word, row_col, word_lst)

					# Un-choose
					word = word[:(-1)]
					row_col.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for word in f:
			word = word.strip()
			if len(word) >= 4:
				dictionary.append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


def check_format(row):
	if len(row) != 4:
		return False
	else:
		for ch in row:
			if len(ch) != 1:
				return False
		return True


if __name__ == '__main__':
	main()
