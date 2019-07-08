import common
import student_code

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


def run_experiment(data, btlimit, fclimit, mrvlimit):
	result=True

	sudoku = common.init_sudoku();
	common.set_sudoku(sudoku, data);
	bt1 = student_code.sudoku_backtracking(sudoku);
	if ( not check_result(sudoku,False)):
		print("Backtracking results: ")
		check_result(sudoku,True);
		result=False;
	else:
		print("Backtracking results: ")

	if (bt1>btlimit):
		print("Backtracking count: "+str(bt1))
		result=False
	else:
		print("Backtracking count: "+str(bt1))

	common.set_sudoku(sudoku, data)
	fc1 = student_code.sudoku_forwardchecking(sudoku)
	if (not check_result(sudoku,False)):
		print("Forwardchecking results: ")
		check_result(sudoku,True)
		result=False
	else:
		print("Forwardchecking results: ")

	if (fc1>fclimit):
		print("Forwardchecking count: "+str(fc1))
		result=False;
	else:
		print("Forwardchecking count: "+str(fc1))

	common.set_sudoku(sudoku, data);
	mrv1 = student_code.sudoku_mrv(sudoku);
	if (not check_result(sudoku,False)):
		print("MRV results: ")
		check_result(sudoku,True)
		result=False
	else:
		print("MRV results: ")

	if (mrv1>mrvlimit):
		print("MRV count: "+str(mrv1))
		result=False;
	else:
		print("MRV count: "+str(mrv1))

	return result



data1 = ("900670000"
"006800470"
"800010003"
"003000001"
"005406900"
"600000300"
"300060008"
"068005200"
"000082006")

data2 = ("006100050"
"200605008"
"000090002"
"000019300"
"002000800"
"003570000"
"900040000"
"800301009"
"040006100")

data3 = ("530070000"
"600195000"
"098000060"
"800060003"
"400803001"
"700020006"
"060000280"
"000419005"
"000080079")

data4 = ("009000400"
"600400020"
"840031090"
"008007041"
"500060003"
"160800700"
"070290065"
"020005004"
"005000900")
print "Content-type:text/html\r\n"

print ("Board 1")
exp1 = run_experiment(data1, 35000, 4000, 2500)
print ("Board 2")
exp2 = run_experiment(data2, 200000, 30000, 3500)
print ("Board 3")
exp3 = run_experiment(data3, 40000, 4500, 300)
print ("Board 4")
exp4 = run_experiment(data4, 6000, 800, 650)

all_passed = exp1 and exp2 and exp3 and exp4


if all_passed:
	exit(0)
else:
	exit(1)
