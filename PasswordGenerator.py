# COMP 3008 P2 
# Comp Sci Gang
# March 26, 2019
# Martin So - 101042739
# Steven Vezina - 101010889
# Liam Shaw - 101044302

# Need a password possbility of at least 2^21 (2,097,152)
# 62 possible outcomes for each bit. 
# 26 upper case letters + 10 numbers = 36

# Total password possiblities = 36^4 (1,679,616)



from random import randint
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

nato_alphabet= ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliet","Kilo","Lima","Mike","November","Oscar",
				"Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","X-ray","Yankee","Zulu"]

path = "D:/Documents/School/Third Year/Winter 2019/3008/Project 2/PasswordGenerator/logs.txt"
file = open(path,"w")

# Gets a random number between 0 and 26 that represents the position of the letter in the alphabet
def getRandomUpper():
	index = randint(0, len(upper)-1);
	return upper[index];
	
# Gets a random number between 0 and 10 that represents a single digit, non negative number
def getRandomNum():
	index = randint(0, len(numbers)-1);
	return numbers[index];
	
#Replaces a bit if the password does not contain a letter at all
def replaceWithLetter(password):

	posReplace = getRandPasswordPos(password);
	new_password = password[:(posReplace -1)] + getRandomUpper() + password[posReplace:]
	return new_password 
		
	


#Gets a random position in the password
def getRandPasswordPos(password):
	return randint(1, len(password))

#Replaces a bit in the password with a number in the event the original password does not contain any numbers
def replaceWithNum(password):
	posReplace = getRandPasswordPos(password);
	new_password = password[:(posReplace -1)] + getRandomNum() + password[posReplace:]
	return new_password 
	
#Generates a password
def generatePassword():
	
	password = ""
	hasLetter = -1
	hasNumber = -1
	# Generates a 4 bit password 
	# TODO: Can be changed based on limit 
	for x in range (0, 4):
		selector = randint(0, 1);
		if (selector == 0):
			password += getRandomUpper();
			hasLetter = 1
		else:
			password += getRandomNum();
			hasNumber = 1
	# If password generated has no letters what so ever, find and replace with a letter at a random position
	if(hasLetter == -1):
		return replaceWithLetter(password);
	
	#Finds and replaces a letter at a random position with a randomly generated number
	if(hasNumber == -1):
		return replaceWithNum(password)
			
	
	return password
	

def testPassword(pw):
	
	userInput = "";
	
	numTries = 0
		
	for x in range(0,3):
		userInput = input("Practice entering your password: ")
		if(userInput == pw):
			print("Success! Please remember your password from now on\n")
			break;
		else:
			print("Error! Please try again\n")	
			numTries+=1
			
	if(numTries == 3):
		print("Failed to test password. Please generate a new one! \n")
		
def main():
	
	email = ""
	shopping =""
	banking =""
	runProg = True;

	while(runProg):
		print("==================================")
		print("Password Generator")
		print("(1) Generate Passwords")
		print("(0) Exit");
		print("==================================\n")
		choice = input("Select an option: ")
		
		if(choice == "1"):
			email = generatePassword()
			print("Your email password is: " + email +"\n")
			testPassword(email)
			shopping = generatePassword()
			print("Your shopping password is: " +shopping+"\n")
			testPassword(shopping)
			
			
			
		elif(choice == "0"):
			exit()
		
		else:
			print("Please enter a proper selection\n")
			continue
		
	print(generatePassword())
	
	file.close()
main()
