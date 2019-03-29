# COMP 3008 P2 
# Comp Sci Gang
# March 26, 2019
# Martin So - 101042739
# Steven Vezina - 101010889
# Liam Shaw - 101044302

# Need a password possbility of at least 2^21 (2,097,152)
# 62 possible outcomes for each bit. 
# 26 upper case letters + 26 lower case + 10 numbers = 62

# Total password possiblities = 62^4 (14,776,336)

from random import randint

upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

nato_alphabet= ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliet","Kilo","Lima","Mike","November","Oscar",
				"Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","X-ray","Yankee","Zulu"]

# Gets a random number between 0 and 26 that represents the position of the letter in the alphabet
def getRandomUpper():
	index = randint(0, len(upper)-1);
	return upper[index];
# Gets a random number between 0 and 26 that represents the position of the letter in the alphabet
def getRandomLower():
	index = randint(0, len(lower)-1);
	return lower[index];
	
# Gets a random number between 0 and 10 that represents a single digit, non negative number
def getRandomNum():
	index = randint(0, len(numbers)-1);
	return numbers[index];
	
#Replaces a bit if the password does not contain a letter at all
def generateNewLetter(password):
	
	letterSelect = randint(0, 1);
		#Gets a random upper case letter if RNG results in 0
	posReplace = getRandPasswordPos(password);
	if(letterSelect == 0):
		password = password[:(posReplace -1)] + getRandomUpper() + password[posReplace:]
		return password 
	else:
		password = password[:(posReplace -1)] + getRandomLower() + password[posReplace:]
		return password 

#Gets a random position in the password
def getRandPasswordPos(password):
	return randint(1, len(password))

#Replaces a bit in the password with a number in the event the original password does not contain any numbers
def generateNewNum(password):
	posReplace = getRandPasswordPos(password);
	password = password[:(posReplace -1)] + getRandomNum() + password[posReplace:]
	
	
def main():

	password = ""
	
	hasLetter = -1
	hasNumber = -1
	
	for x in range (0, 4):
		selector = randint(0, 2);
		if (selector == 0):
			password += getRandomUpper();
			hasLetter = 1
		elif (selector == 1):
			password += getRandomLower();
			hasLetter = 1
		else:
			password += getRandomNum();
			
		# If password generated has no letters what so ever, drop first number and replace with a letter
		if(hasLetter == -1):
			generateNewLetter(password);
		
		if(hasNumber == -1):
			generateNewNum(password)
		
	print(password)

main()
