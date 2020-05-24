# generate random integer values
from random import seed
from random import randint
# seed random number generator
#seed(1)
# generate some integers
print('Dice rolling SImulaltor')

value = randint(1, 6) ##min 1 max 6
print(value)
while True:
  C=input('do you want to roll again')

  if C== "Y" :
    value = randint(1, 6) ##min 1 max 6
    
    print(value)
  elif C== "N":
    break
   
