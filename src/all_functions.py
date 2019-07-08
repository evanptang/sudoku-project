import common

class variables:
	counter=0

## SUDOKU functions
## There are three-Each of them are wrapped in a function which initiates the
## recursive call.
## 		-backtracking
## 		-forwardchecking
## 		-mrv (minimum remaining value)

## Wrapper functions
##		-sudoku_backtracking
##		-sudoku_forwardchecking
##		-sudoku_mrv
def sudoku_backtracking(sudoku):
	sudoku_backtracking_recursive(sudoku)
	return variables.counter

def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	sudoku_forwardchecking_recursive(sudoku)
	return variables.counter

def sudoku_mrv(sudoku):
	variables.counter = 0
	sudoku_mrv_recursive(sudoku)
	return variables.counter

## Recursive functions
##		-sudoku_backtracking_recursive
##		-sudoku_forwardchecking_recursive
##		-sudoku_mrv_recursive

def sudoku_backtracking_recursive(sudoku):
	if complete(sudoku):
		return True
	a, b = find_first_empty(sudoku)
	for val in range (1,10):
		variables.counter += 1
		if common.can_yx_be_z(sudoku ,b, a, val) is True:
			sudoku[b][a] = val
			if sudoku_backtracking_recursive(sudoku) is True:
				return True
			else:
				sudoku[b][a] = 0
	return False

def sudoku_forwardchecking_recursive(sudoku):
	if complete(sudoku):
		return True
	if is_any_domain_empty(sudoku):
		return False
	a, b = find_first_empty(sudoku)
	variables.counter += 1
	domain = get_domain(sudoku, a, b)
	for item in range(len(domain)):
		sudoku[b][a] =  domain[item]
		if sudoku_forwardchecking_recursive(sudoku) is True:
			return True
		sudoku[b][a] = 0
	return False

def sudoku_mrv_recursive(sudoku):
	if complete(sudoku):
		return True
	if is_any_domain_empty(sudoku):
		return False
	a, b = min_remaining_value(sudoku)
	variables.counter += 1
	domain = get_domain(sudoku, a, b)
	for item in range(len(domain)):
		sudoku[b][a] =  domain[item]
		if sudoku_mrv_recursive(sudoku) is True:
			return True
		sudoku[b][a] = 0
	return False

## Find Next Value to check functions:
##		-find_first_empty: Used by both backtracking and forwardchecking
##		-min_remaining_value: Used only for MRV

def find_first_empty(sudoku):
	for j in range(9):
		for i in range(9):
			if sudoku[j][i] == 0:
				return (i,j)

def min_remaining_value(sudoku):
	min = 99999
	final_x = 0
	final_y = 0
	for x in range(9):
		for y in range(9):
			if sudoku[y][x] == 0:
				if len(get_domain(sudoku, x, y))<min:
					min = len(get_domain(sudoku, x, y))
					final_x = x
					final_y = y
	return (final_x, final_y)


## Additional Helper Functions
##		-get_domain
##		-is_any_domain_empty
##		-complete

def get_domain(board, x, y):
	domain = []
	for item in range(1,10):
		if common.can_yx_be_z(board, y, x, item):
			domain.append(item)
	return domain

def is_any_domain_empty(sudoku):
	for x in range(9):
		for y in range(9):
			if sudoku[y][x] == 0:
				if len(get_domain(sudoku, x, y)) == 0:
					return True
	return False

def complete(sudoku):
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				return False
	return True
