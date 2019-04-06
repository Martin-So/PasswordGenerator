# COMP 3008 P2 
# Comp Sci Gang
# March 26, 2019
# Martin So - 101042739
# Steven Vezina - 101010889
# Liam Shaw - 101044302


# Need a password possbility of at least 2^21 (2,097,152)
# 26 upper case letters + 10 numbers = 36
# Total password possiblities = 36^4 (1,679,616)

import random 
import time
import datetime
import os
import sys
from random import randint, shuffle

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

nato_alphabet= ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliet","Kilo","Lima","Mike","November","Oscar",
                "Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","Xray","Yankee","Zulu"]
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
passwords =["email", "shopping", "banking"]


path = "logs.txt"
file = open(path,"a")
file.write("================Password Generator Logs==================\n")
file.flush()
os.fsync(file.fileno())

# Gets a random number between 0 and 26 that represents the position of the letter in the alphabet
def getRandomLetter():
    index = randint(0, len(nato_alphabet)-1);
    return nato_alphabet[index];
    
# Gets a random number between 0 and 10 that represents a single digit, non negative number
def getRandomNum():
    index = randint(0, len(numbers)-1);
    return numbers[index];
    
#Replaces a bit if the password does not contain a letter at all
def replaceWithLetter(password):

    posReplace = getRandPasswordPos(password);
    new_password = password[:(posReplace -1)] + getRandomLetter() + password[posReplace:]
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

    # Generates a 5 character long password 
    # TODO: Can be changed based on limit 
    for x in range (0, 5):
        selector = randint(0, 1);
        if (selector == 0):
            randoLetter = getRandomLetter()
            password += randoLetter
            hasLetter += 1
        
        else:
            randoNum = getRandomNum()
            password += randoNum

            hasNumber = 1
        
    
    # If password generated has no letters what so ever, find and replace with a letter at a random position
    if(hasLetter == -1):
        return replaceWithLetter(password);
    
    #Finds and replaces a letter at a random position with a randomly generated number
    if(hasNumber == -1):
        return replaceWithNum(password)
            
    
    return password


    

def testPassword(pw):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    file.write(st + ": Starting Random Password Test\n")
    file.flush()
    os.fsync(file.fileno())
    userInput = "";
    timer = 0
    numTries = 0
        
    for x in range(0,2):
        userInput = input("Practice entering your password: ")
        timer+=1
        if(userInput == pw):
            print("Success! Please remember your password from now on\n")
            print("================Tips to Remember your Password==================")
            print("A = Alpha        H = Hotel           O = Oscar           V = Victor")
            print("B = Bravo        I = India           P = Papa            W = Whiskey")
            print("C = Charlie      J = Juliet          Q = Quebec          X = Xray")
            print("D = Delta        K = Kilo            R = Romeo           Y = Yankee")
            print("E = Echo         L = Lima            S = Sierra          Z = Zulu")
            print("F = Foxtrot      M = Mike            T = Tango")
            print("G = Golf         N = November        U = Uniform")
            print("===============================================================\n")
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file.write(st + ": Password succesfully created and tested | Time taken to test: "+str(timer)+" seconds \n")
            file.flush()
            os.fsync(file.fileno())
            break;
        else:
            print("Error! Please try again\n")    
            numTries+=1
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file.write(st + ": Initial password test failed, creating a new password\n")
            file.flush()
            os.fsync(file.fileno())
    if(numTries == 3):
        print("Failed to test password. Please generate a new one! \n")
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        file.write(st + ": Initial password test failed. Redirecting to main\n")
        file.flush()
        os.fsync(file.fileno())
        
def randomPasswordTest(passList):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    file.write(st + ": Starting Random Password Test\n")
    file.flush()
    os.fsync(file.fileno())
    randList = passList.copy()
    shuffle(randList)
    
    for counter, pword in enumerate(randList):
        numTries = 0
        timer = 0
        print("================Random Password Tester================")
  

        #Email password test
        # compares first index in shuffled array with first index of sorted array of passwords
        # Sorted array has order of [Email, Shopping, Banking]
        if(pword == passList[0]):
            while(numTries != 3):
                userInput = input("Enter your email password: ")
                timer+=1
                if(userInput == pword):
                    
                    print("Success!\n")
                    ts = time.time()
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    file.write(st + ": Email Random Password succesfully tested | Time taken to test: "+str(timer)+" seconds \n")
                    file.flush()
                    os.fsync(file.fileno())
                    break
                    break;
                else:
                    print("Error! Please try again\n")    
                    numTries += 1
                    ts = time.time()
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    line = st + ": Email Random Password Test - Incorrect password entered | Number of tries: "+ str(numTries) + " | Time taken: " +str(timer)+ " seconds \n"
                    file.write(line)
                    file.flush()
                    os.fsync(file.fileno())
                    
            if(numTries == 3):
                print("Number of tries exceeded, please create a new password")
                ts = time.time()
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                file.write(st + ": Number of Tries exceeded, creating a new password\n")
                file.flush()
                os.fsync(file.fileno())
                passSelect = -1
        
                break;
                break;

        #Shopping Password
        # If the current word in  shuffled array equals to the shopping password stored in the original array
        elif(pword == passList[1]):
            
            while(numTries != 3):
                timer+=1
                userInput = input("Enter your shopping password: ")
                if(userInput == pword ):
                    ts = time.time()
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    file.write(st + ": Shopping Random Password succesfully tested | Time taken to test: "+str(timer)+" seconds \n")
                    file.flush()
                    os.fsync(file.fileno())
                    print("Success!\n")
                   
                    break;
                    break;
                    
                else:
                    print("Error! Please try again\n")
                    numTries+=1
                    #Gets current date & time and logs it to logs.txt
                    ts = time.time()
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    line = st + ": Shopping Random Password Test - Incorrect password entered | Number of tries: "+ str(numTries) + " | Time taken: " +str(timer)+ " seconds \n"
                    file.write(line)
                    file.flush()
                    os.fsync(file.fileno())
            if(numTries == 3):
                print("Number of tries exceeded, please create a new password")
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                file.write(st + ": Number of Tries exceeded, creating a new password\n")
                file.flush()
                os.fsync(file.fileno())
                break;
                break;


        #Banking password
        elif(pword==passList[2]):
            while(numTries != 3):
                userInput = input("Enter your banking password: ")
                if(userInput == pword):
                    ts = time.time()
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    file.write(st + ": Shopping Random Password succesfully tested | Time taken to test: "+str(timer)+" seconds \n")
                    file.flush()
                    os.fsync(file.fileno())
                    print("Success!\n")
                    break;
                    break;
                else:
                    print("Error! Please try again\n")    
                    numTries += 1
                    ts = time.time()
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') #Gets current time
                    line = st + ": Banking Random Password Test - Incorrect password entered | Number of tries: "+ str(numTries) + " | Time taken: " +str(timer)+ " seconds \n"
                    file.write(line)
                    file.flush()
                    os.fsync(file.fileno())
            if(numTries == 3):
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                print("Number of tries exceeded, please create a new password")
                file.write(st + ": Number of Tries exceeded, creating a new password\n")
                file.flush()
                os.fsync(file.fileno())
                break;
                break;
        

        
       
def main():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    file.write(st + ": Program start\n")
    file.flush()
    os.fsync(file.fileno())
    
    email = ""
    shopping =""
    banking =""
    
    runProg = True;

    while(runProg):
        print("================Password Generator==================")
        print("(1) Generate Passwords")
        print("(2) Password Memorizing Tips")
        print("(0) Exit");
        print("====================================================\n")
        choice = input("Select an option: ")
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        file.write(st + ": Main Menu\n")
        file.flush()
        os.fsync(file.fileno())
        if(choice == "1"):
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file.write(st + ": Generating Email password\n")
            file.flush()
            os.fsync(file.fileno())
            email = generatePassword()
            print("================Email Password==================")
            print("Your email password is: " + email +"\n")
            testPassword(email)
            shopping = generatePassword()
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file.write(st + ": Generating Shopping password\n")
            file.flush()
            os.fsync(file.fileno())
            print("================Shopping Password==================")
            print("Your shopping password is: " +shopping+"\n")
            testPassword(shopping)
            banking = generatePassword()
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file.write(st + ": Generating Banking password\n")
            file.flush()
            os.fsync(file.fileno())
            print("================Banking Password==================")
            print("Your banking password is: " +banking+"\n")
            testPassword(banking)
            
            passList = [email,shopping,banking]

           
            randomPasswordTest(passList)
            
            
        elif(choice == "0"):
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file.write(st + ": Program exiting\n")
               
            file.write("========================================================\n")
            file.flush()
            os.fsync(file.fileno())
            exit()
            file.close()
            
            
        elif(choice == "2"):
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file.write(st + ": Viewing Password tips\n")
            file.flush()
            os.fsync(file.fileno())
            print("================Tips to Remember your Password==================")
            print("A = Alpha        H = Hotel           O = Oscar           V = Victor")
            print("B = Bravo        I = India           P = Papa            W = Whiskey")
            print("C = Charlie      J = Juliet          Q = Quebec          X = Xray")
            print("D = Delta        K = Kilo            R = Romeo           Y = Yankee")
            print("E = Echo         L = Lima            S = Sierra          Z = Zulu")
            print("F = Foxtrot      M = Mike            T = Tango")
            print("G = Golf         N = November        U = Uniform")
            print("===============================================================")
            continue;
            
        else:
            print("Please enter a proper selection\n")
            continue
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file.write(st + ": Incorrect menu selection")
            file.flush()
            os.fsync(file.fileno())
    
    
    
main()
