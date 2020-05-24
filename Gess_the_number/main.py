import random
 
n = random.randint(1, 99) #randpom fucntioon
print(n)
guess = int(input("Enter an integer from 1 to 99: ")) #user to input integer in that range
while n != "guess": 		#only when the condition nis not equslto user guess goinside loop
    #print
    if guess < n:
      print ("guess is low")
      guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
      print ("guess is high")
      guess = int(input("Enter an integer from 1 to 99: "))
    else:
      print ("you guessed it!")
      break
   # print
