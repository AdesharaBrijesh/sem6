
def encryptRF(text, key): 
	rail = [['\n' for i in range(len(text))] 
				for j in range(key)] 
	
	dir_down = False
	row, col = 0, 0
	for i in range(len(text)): 
		if (row == 0) or (row == key - 1): 
			dir_down = not dir_down 
		rail[row][col] = text[i] 
		col += 1
		if dir_down: 
			row += 1
		else: 
			row -= 1
	result = [] 
	for i in range(key): 
		for j in range(len(text)): 
			if rail[i][j] != '\n': 
				result.append(rail[i][j]) 
	return("" . join(result)) 
	
def decryptRF(ciphertext, key): 
	rail = [['\n' for i in range(len(ciphertext))] 
				for j in range(key)] 
	
	dir_down = None
	row, col = 0, 0
	for i in range(len(ciphertext)): 
		if row == 0: 
			dir_down = True
		if row == key - 1: 
			dir_down = False
		rail[row][col] = '*'
		col += 1
		if dir_down: 
			row += 1
		else: 
			row -= 1 
	index = 0
	for i in range(key): 
		for j in range(len(ciphertext)): 
			if ((rail[i][j] == '*') and
			(index < len(ciphertext))): 
				rail[i][j] = ciphertext[index] 
				index += 1
	result = [] 
	row, col = 0, 0
	for i in range(len(ciphertext)): 
		if row == 0: 
			dir_down = True
		if row == key-1: 
			dir_down = False
		if (rail[row][col] != '*'): 
			result.append(rail[row][col]) 
			col += 1
		if dir_down: 
			row += 1
		else: 
			row -= 1
	return("".join(result)) 


pt=input("Enter Plain Text:")
p=int(input("Enter key:"))
en_str=encryptRF(pt,p)
de_str=decryptRF(en_str,p)
print(en_str)
print(de_str)