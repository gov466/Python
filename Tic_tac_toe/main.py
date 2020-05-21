#Tic tac toe using python
#General fucntions to be included
#Board
#Display Board
#paly game
#handle a turn
#check win
  #check Row
  #check comlm
  #check diagonal
#check tie
#flip player
#---global variable

game_still_going= True
winner = None
board =["-","-","-",
        "-","-","-",
        "-","-","-",]
current_player= "X "
def display_board() :
  print(" | " +board[0]+ " | " +board[1]+ " | "+board[2]+ " | ")
  print(" | " +board[3]+ " | " +board[4]+ " | "+board[5]+ " | ")
  print(" | " +board[6]+ " | " +board[7]+ " | "+board[8]+ " | ")

def play_game():
  #display initail board
  display_board()

  while game_still_going:
    #habdle a turn of player
    handle_turn( current_player)
    #check is hgame is over
    check_if_game_over()
    #flip to other player
    flip_player()
  
  #game has ended
  if winner =="X" or winner =="O":
    print(winner + " won ")
  else:
    print("Tie")
def handle_turn(player):
  posistion= input("choose a posisition from 1-9: ")
  posistion= int(posistion)-1
  board[posistion]="X"
  display_board()

def check_if_game_over():
  check_if_winner()
  chech_if_tie()

def check_if_winner():

  #set up global variuable
  global winner
  #check rows
  row_winner=check_rows()

  #cehck column
  column_winner=check_columns

  #chck diagnl
  diagonal_winner=check_diagonals()
  if row_winner:
    winner= row_winner
    #there was a winner
  elif column_winner:
    winner=column_winner
    #there was a winner
  elif diagonal_winner:
    winner=diagonal_winner
    #there was a win
  else:
    #there was no winner
    winner= None
  return

def check_rows():
  #set glabal variable
  global game_still_going
  #checking all rows
  row_1= board[0]==board[1]==board[2] != "-"
  row_2= board[3]==board[4]==board[5] != "-"
  row_3= board[6]==board[7]==board[8] != "-"

  if row_1 or row_2 or row_3:
    game_still_going= False
  #return the winner(X or O)

  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_columns():

   #set glabal variable
  global game_still_going
  #checking all rows
  column_1= board[0]==board[3]==board[6] != "-"
  column_2= board[1]==board[4]==board[7] != "-"
  column_3= board[2]==board[5]==board[8] != "-"

  if column_1 or column_2 or column_3:
    game_still_going= False
  #return the winner(X or O)

  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonals():

   #set glabal variable
  global game_still_going
  #checking all rows
  diagonal_1= board[0]==board[4]==board[8] != "-"
  diagonal_2= board[6]==board[4]==board[2] != "-"
   
  #checking if any diagonasl are true   
  if diagonal_1 or diagonal_2 :
    game_still_going= False
  #return the winner(X or O)

  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[6]
   

  return


def check_if_tie():
  return

def flip_player():
  return
play_game()
