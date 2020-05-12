def translate_numeral(number): #wir wollen funktion die roemische in arabische Zahlen wandelt
	if type(number) == str:  # check type of input
		romans=["M","D","C","L","X","V","I"] #liste aller moeglichen roem. ziffern, geordnet nach groesse
		arabics=[1000,500,100,50,10,5,1] #liste derselben in arabischen zahlen
		roman_numeral = number 
		arabic_number=0
		for i in romans: #i durchlaeuft alle roem. ziffern der groesse nach
			while roman_numeral.find(i)!=-1: #das alles passiert nur, wenn die ziffer i in der zahl vorkommt!
				zahl = arabics[romans.index(i)] #roem. zahl i in arabisch
				i_stelle=roman_numeral.find(i) #ist i an erster oder zweiter stelle (->ist davor eine zahl zum abziehen?)
				if i == "D" or i == "L" or i == "V": #falls i eine der "5er"-ziffern ist...
					zahl = zahl - arabics[romans.index(i)+1]*i_stelle #kann an der pot. stelle vor i nur die jeweils kleinere 1er-ziffer stehen, auf die wir durch einen schritt in der romans-liste kommen. Falls i an zweiter stelle, wird diese abgezogen
				elif i == "M" or i == "C" or i == "X":
					zahl = zahl - arabics[romans.index(i)+2]*i_stelle #wenn i 1er-zahl kann davor nur das zehntel davon --> zwei schritte in liste
				else: zahl = zahl #vor I kann nichts stehen, da kleinste Einheit. wenn man versucht in der Liste weiterzulaufen als letzter Eintrag --> Fehler
				roman_numeral=roman_numeral[i_stelle+1:] #der noch nicht "arabisierte" Teil der roem. Zahl wird behalten um weiter verabritet zu werden
				arabic_number = arabic_number+zahl #alles bisher in arabisch umgewandelte aufaddieren
		

		print('{0} translated to {1}!'.format(number, arabic_number))  # print the result
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