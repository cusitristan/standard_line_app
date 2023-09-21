import line
# this script is for an interactive command line tool that takes
# an input of two cartesian points in the form of ints or floats.
# With this input the tool outputs the standard form of the line 
# connecting those two points. 

def run_app():
	entry_msg = "This program takes in an input of two cartesian points\n\
and outputs the standard form of the line connecting them.\n\
\n\
Inputs can be integer or decimal values however, decimal\n\
values can lead to inaccuracies due to how they are stored\n\
in the machine. \n\
\n\
Output will always be in integer form meaning fractional \n\
values will be scaled up."
	print("==========================================================")
	print(entry_msg)
	print("==========================================================")
	while(1):
		x_1 = input("Enter X coordinate of first point:")
		y_1 = input("Enter Y coordinate of first point:")
		print("1st point ==> ("+str(x_1)+", "+str(y_1)+")")
		x_2 = input("Enter X coordinate of second point:")
		y_2 = input("Enter Y coordinate of second point:")
		print("2nd point ==> ("+str(x_2)+", "+str(y_2)+")")
		A, B, C = line.standard_form( (float(x_1), float(y_1)), \
					(float(x_2), float(y_2)) )
		if(A == 0):
			line = "x = "+str(C)
		elif(B == 0):
			line = "y = "+str(C)
		else:
			line = str(A)+"x + "+str(B)+"y = "+str(C)
			
		print("==========================================================")
		print(line)
		print("==========================================================")

		user_input = input("Would you like to enter new points? Y/N \n")
		if((user_input == "Y") or (user_input == "y")):
			continue
		elif((user_input == "N") or (user_input == "n")):
			break
	exit()

if __name__ == '__main__':
	run_app()