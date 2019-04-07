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
import csv
from random import randint, shuffle

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

nato_alphabet= ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliet","Kilo","Lima","Mike","November","Oscar",
                "Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","Xray","Yankee","Zulu"]
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
path = "logs.csv"
with open(path, mode='a', newline='') as file:
    writer = csv.writer(file)
randUserID = randint(0, 2**(21))



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

#timer function


#Tests if user knows password
def testPassword(pw,typ):
    userInput = "";
    timer = 0
    numTries = 0
    start = True
    for x in range(0,3):
        start = time.time()
        userInput = input("Practice entering your password: ")
        if(userInput == pw):
            end = time.time()
            timer = end-start
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
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            with open(path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([randUserID, st, typ + " Validate", "Success", timer])
            return True
            break;
        
        else:
            print("Error! Please try again\n")    
            numTries+=1
            ts = time.time()
            end = time.time()
            timer = end-start
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            with open(path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([randUserID, st, typ + " Validate", "Fail", timer])
    print("Failed to test password. Please generate a new one! \n")              
    return False

def randomPasswordTest(passList):
    randList = passList.copy()
    shuffle(randList)
    for counter, pword in enumerate(randList):
        numTries = 0
        timer = 0
        start = True
        print("================Random Password Tester================")
          

        #Email password test
        # compares first index in shuffled array with first index of sorted array of passwords
        # Sorted array has order of [Email, Shopping, Banking]
        if(pword == passList[0]):
            while(numTries != 3):
                start = time.time()
                userInput = input("Enter your email password: ")
                if(userInput == pword):
                    print("Success!\n")
                    end = time.time()
                    timer = end-start
                    ts = time.time()
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    with open(path, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([randUserID, st,"Email Login", "Success", timer])
                    break
                    break;
                else:
                    numTries+=1
                    end = time.time()
                    timer = end-start
                    print("Error! Please try again\n")
                    ts = time.time()
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    with open(path, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([randUserID, st,"Email Login", "Fail", timer])
            if(numTries == 3):
                print("Number of tries exceeded, please create a new password")
                break;
                break;

        #Shopping Password
        # If the current word in  shuffled array equals to the shopping password stored in the original array
        elif(pword == passList[1]):
            
            while(numTries != 3):
                start = time.time()
                userInput = input("Enter your shopping password: ")
                if(userInput == pword ):
                    end = time.time()
                    timer = end - start
                    ts = time.time()
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    with open(path, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([randUserID, st,"Shopping Login", "Success", timer])      
                    print("Success!\n")               
                    break;
                    break;
                    
                else:
                    print("Error! Please try again\n")
                    numTries+=1
                    ts = time.time()
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    with open(path, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([randUserID, st,"Shopping Login", "Fail", timer])
            if(numTries == 3):
                print("Number of tries exceeded, please create a new password")

                break;
                break;


        #Banking password
        elif(pword==passList[2]):
            while(numTries != 3):
                start = time.time()
                userInput = input("Enter your banking password: ")
                if(userInput == pword):
                    end = time.time()
                    timer = end-start
                    ts = time.time()
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    with open(path, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([randUserID, st,"Banking Login", "Success", timer])
                    print("Success!\n")
                    break;
                    break;
                else:
                    print("Error! Please try again\n")    
                    numTries += 1
                    ts = time.time()
                    end = time.time()
                    timer = end - start
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    with open(path, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([randUserID, st,"Banking Login", "Fail", timer])
                    
            if(numTries == 3):
                print("Number of tries exceeded, please create a new password")

                break;
                break;
        

        
       
def main():

    email = ""
    shopping =""
    banking =""
    
    runProg = True;

    success = 0
    fail = 0
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    with open(path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([randUserID, st,"Program", "Start", 0])

    
    while(runProg):
        print("================Password Generator==================")
        print("(1) Generate Passwords")
        print("(2) Password Memorizing Tips")
        print("(0) Exit");
        print("====================================================\n")
        choice = input("Select an option: ")
        if(choice == "1"):

            print("================Email Password==================")
            email = generatePassword()
            print("Your email password is: " + email +"\n")
            if(testPassword(email, "Email")==False):
                continue;
            shopping = generatePassword()

            print("================Shopping Password==================")
            print("Your shopping password is: " +shopping+"\n")
            if(testPassword(shopping, "Shopping")==False):
                continue;

            
            banking = generatePassword()
            print("================Banking Password==================")
            print("Your banking password is: " +banking+"\n")
            if(testPassword(banking, "Banking" )==False):
                continue;
            
            passList = [email,shopping,banking]

           
            randomPasswordTest(passList)
            
            
        elif(choice == "0"):
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            with open(path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([randUserID, st,"Program", "End", 0])
            file.close()
            exit()

            
            
        elif(choice == "2"):

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

    
    
    
main()
