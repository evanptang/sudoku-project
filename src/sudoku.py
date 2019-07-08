import common
import all_functions

# Import modules for CGI handling
import cgi, cgitb


class bcolors:
	RED    = ""
	GREEN  = ""

def check_result(sudoku, show):
	result=True
	for y in range(9):
		v=""
		for x in range(9):
			value = sudoku[y][x];
			sudoku[y][x]=0
			if (value!=0 and common.can_yx_be_z(sudoku,y,x,value)):
				v+=bcolors.GREEN
			else:
				result = False
				v+=bcolors.RED
			v+=str(value)
			sudoku[y][x]=value
		if (show):
			print(v)
	return result


def check_new_entry(data, btlimit, fclimit, mrvlimit):
	result=True

	sudoku = common.init_sudoku();
	common.set_sudoku(sudoku, data);
	bt1 = all_functions.sudoku_backtracking(sudoku);
	if ( not check_result(sudoku,False)):
		print("FAIL")
		result=False;
	return result

def run_experiment(data, btlimit, fclimit, mrvlimit):
	result=True

	sudoku = common.init_sudoku();
	common.set_sudoku(sudoku, data);
	bt1 = all_functions.sudoku_backtracking(sudoku);
	if ( not check_result(sudoku,False)):
		print("<br>Backtracking results: "+bcolors.RED+"FAIL"+bcolors.NORMAL)
		check_result(sudoku,True);
		result=False;
	else:
		print("<br>Backtracking results: ")

	if (bt1>btlimit):
		print("<br>Backtracking count: "+str(bt1)  +""+""+"")
		result=False
	else:
		print("<br>Backtracking count: "+str(bt1) +""+""+"")

	common.set_sudoku(sudoku, data)
	fc1 = all_functions.sudoku_forwardchecking(sudoku)
	if (not check_result(sudoku,False)):
		print("<br>Forwardchecking results: "+"")
		check_result(sudoku,True)
		result=False
	else:
		print("<br>Forwardchecking results: ")

	if (fc1>fclimit):
		print("<br>Forwardchecking count: "+str(fc1) +"("+bcolors.RED+"FAIL"+bcolors.NORMAL+")")
		result=False;
	else:
		print("<br>Forwardchecking count: "+str(fc1) +" "+" "+" ")

	common.set_sudoku(sudoku, data);
	mrv1 = all_functions.sudoku_mrv(sudoku);
	if (not check_result(sudoku,False)):
		print("<br>MRV results: "+bcolors.RED+"FAIL"+bcolors.NORMAL)
		check_result(sudoku,True)
		result=False
	else:
		print("<br>MRV results: ")

	if (mrv1>mrvlimit):
		print("<br>MRV count: "+str(mrv1) +"("+bcolors.RED+"FAIL"+bcolors.NORMAL+")")
		result=False;
	else:
		print("<br>MRV count: "+str(mrv1) +" "+" "+" ")

	return result

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
board = form.getvalue('board')

print "Content-type:text/html\r\n"

if (len(board) != 81):
    print "bad input"
    exit()

for c in board:
    if ((c < '0') or (c > '9')):
        print "bad input"
        exit()

check = form.getvalue('check')
if (check == "YES"):
    exp1 = check_new_entry(board, 35000, 4000, 2500)
else:
    exp1 = run_experiment(board, 35000, 4000, 2500)

exit(0)
