def translate_numeral(number):
	if type(number) == str:  # check type of input
		# ======enter code below======
		roman_numeral = number # the roman numeral to translate
		roman_arabic_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
							 'C': 100, 'D': 500, 'M': 1000}
		index = 0  # to access 'next' roman character
		arabic_number = 0  # this will be the result
		for roman_letter in roman_numeral:  # iterate through the roman numeral
		# if we reach the last character of the roman numeral we have to take care of it 
		# specifically since there is no 'next element' we could check. (out of bounce error)
			if index + 1 == len(roman_numeral):  
				sign = +1  # the last roman character is always positive
			# if the number of the actual character is smaller than the next one we have to substract it
			elif roman_arabic_dict[roman_letter] < roman_arabic_dict[roman_numeral[index + 1]]:
				sign = -1
			# if the number of the actual character is bigger it has a positive sign
			else: 
				sign = +1
			# add the current element to the arabic number, the solution, respectively
			arabic_number = arabic_number + sign * roman_arabic_dict[roman_letter]  
			index = index + 1  # increase the index to gain access to the next element
		# =====enter code above=====
		print('{0} translated to {1}!'.format(roman_numeral, arabic_number))  # print the result
		return arabic_number 

	else:
		print('Input not valid.')

if __name__ == '__main__':
	input_numerals = ['X', 'XXVIII', 'LXXI', 'XCIX', 'MCMXCIV']
	outputs = [10, 28, 71, 99, 1994]
	results = [True, True, True, True, True]

	for index in range(5):
		if translate_numeral(input_numerals[index]) != outputs[index]:
			results[index] = False

	if False in results:
		print('Not all numerals translated correctly. Try again.')
	else:
		print('Well done! All numerals translated correctly.')


