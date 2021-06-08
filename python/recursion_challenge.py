def factorial(x):
	if x == 1 or x == 0:
		return 1
	else:
		return x * factorial(x-1)

def palindrome(string):
	pass

def bottles(num):
	#primary recursive logic
	if num > 2:
		print(f'{num} bottles of beer on the wall...{num-1} bottle of beer on the wall')
		bottles(num-1)

def roman_num(num, return_str=''): 
	numeral_key = {'M': 1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
	if num == 0:
		return return_str
	else:
		for key in numeral_key:
			if numeral_key[key] < num:
				num -= numeral_key[key]
				return_str += key
		return (roman_num, return_str) 



print(roman_num(55))
