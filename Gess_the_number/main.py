print("Gess the number")

	
# generate random integer values
from random import seed
from random import randint
# seed random number generator
#seed(1)
# generate some integers
 

while True:
  value = randint(0, 10)
  print(value)
  user_input =int(input("Enter your choice btw 0-10"))
   


 
  if user_input ==value:
    print("Guess correct")
    play_again=input("Do you want to play again( Y or N")
    if play_again == " Y ":
      continue

  elif user_input<value:
    print("your guess is less than actual value")
  else:
    
    print("your guess is greater than actual value")
  
