inputfile = open('mp1.in')
outputfile = open('mp1.out', 'w')
instructions = inputfile.readlines()
register = []	#register array
run = True
pointer = 0		#some counter
isJ = False		#isJ is a boolean for J commands

#removing the spaces from the input
for i in range(len(instructions)):
	instructions[i] = instructions[i].replace(" ","")

#gets the register from the instruction list and removing it from it
for i in range(0, len(instructions[0])):
	register.append(instructions[0][i])
del instructions[0]

#initial print/write
print register
outputfile.write(' '.join(register))

#sets the first instruction to current line
curr_line = instructions[0]

while run:
	#for J command
	if curr_line[0] == 'J':
		if register[int(curr_line[1])] == register[int(curr_line[2])]:
			if int(curr_line[3:]) > len(instructions):
				run = False
			else:
				pointer = int(curr_line[3:]) - 1
				curr_line = instructions[pointer]
		else:
			if pointer > len(instructions):
				run = False
			else:
				pointer += 1
				curr_line = instructions[pointer]

		isJ = True
		
	#for S command
	elif curr_line[0] == 'S':
		register[int(curr_line[1])] = str(int(register[int(curr_line[1])]) + 1)
	
	#for C command
	elif curr_line[0] == 'C':
		register[int(curr_line[2])] = register[int(curr_line[1])]

	#for Z command
	elif curr_line[0] == 'Z':
		register[int(curr_line[1])] = str(int(0))

	#print/write
	print register
	outputfile.write(' '.join(register))

	if isJ:
		isJ = False
	else:
		if pointer+1 < len(instructions):
			pointer += 1
			curr_line = instructions[pointer]
		else:
			run = False

inputfile.close()
outputfile.close()