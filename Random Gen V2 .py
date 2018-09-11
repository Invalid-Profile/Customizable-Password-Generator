#A script to randomly generate a string
#Ver 2.0
import random
import string
import time
start = True
loops = 0
choose1 = True
choose2 = True
choose3 = True
total = ""
char_check = True
check = True
debug = ""

#START OF CHOICES
char = raw_input("How many characters? ")
char = int(char)
if char < 0:
	print("")
	print("You chose to print nothing! (must be a positive integer)")
	time.sleep(3)
	exit()

while(start == True):

    #Choose whether you want letters or not
    while(choose1 == True):
      letrs = raw_input("Letters? (y/n) ")
      if letrs == "Y" or letrs == "y":
         letrs = True
         start = False
         choose1 = False
      elif letrs == "N" or letrs == "n":
        letrs = False
        start = False
        choose1 = False
      else:
        print("Invalid Input. Please respond with Y for yes or N for no.")
    
    #Delay
    time.sleep(0.1)

    while(choose2 == True):
      #Choose whether you want numbers or not
      numbs = raw_input("Numbers? (y/n) ")
      if numbs == "Y" or numbs == "y":
        numbs = True
        start = False
        choose2 = False
      elif numbs == "N" or numbs == "n":
        numbs = False
        start = False
        choose2 = False
      else:
        print("Invalid Input. Please respond with Y for yes or N for no.")

    #Delay
    time.sleep(0.1)

    while(choose3 == True):
    #Choose whether you want symbols or not
      symbs = raw_input("Symbols? (y/n) ")
      print("")
      if symbs == "Y" or symbs == "y":
         symbs = True
         start = False
         choose3 = False
      elif symbs == "N" or symbs == "n":
        symbs = False
        start = False
        choose3 = False
      else:
        print("Invalid Input. Please respond with Y for yes or N for no.")  
    
    if letrs == False and numbs == False and symbs == False:
      print("You chose to print nothing!")
      time.sleep(3)
      exit()
#END OF CHOICES

#The Randomizerinator 9000 V5

  
while loops < char:

  #Letters
    if loops < char:
      if letrs == True:
        rando = random.randint(0,1)
        if rando == 1:
          loops = loops +1
          output = random.choice(string.ascii_letters)
          total = output + total
      
  
  #Numbers
    if loops < char:
      if numbs == True:
        rando = random.randint(0,1)
        if rando == 1:
          loops = loops + 1
          output = random.randint(0,9)
          output = str(output)
          total = output + total


  #Symbols
      if loops < char:               
        if symbs == True:
          rando = random.randint(0,1)
          if rando == 1:
            loops = loops + 1
            output = random.choice(string.punctuation)
            total = output + total
    
  #Ensures that there will be the correct ammount of characters
    if loops == char:
      if len(total) != char:
        loops = 0


#Prints the final randomized product!
if letrs == True:
  debug = debug + "Letters "
if numbs == True:
  debug = debug + "Numbers "
if symbs == True:
  debug = debug + "Symbols"
print("")
print(total)
print("")
print("Length: %s" % (len(total)))
print("Contains: %s" % (debug))
print("")
print("Press enter to coninue...")
close = raw_input("")
