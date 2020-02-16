#Tic Tac Toe game


def draw_board():
    print(" --- --- --- ")
    print("| {} | {} | {} | ".format(game[0][0], game[0][1], game[0][2]))
    print(" --- --- --- ")
    print("| {} | {} | {} | ".format(game[1][0], game[1][1], game[1][2]))
    print(" --- --- --- ")
    print("| {} | {} | {} | ".format(game[2][0], game[2][1], game[2][2]))
    print(" --- --- --- ")
    
    
    




#Define the game

game = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

playing_game = True

token = "x"

while playing_game :
    
    
    draw_board()
    
    making_move = True
    while making_move :
        try:
            #Take a coodirnate
            move = input("Please enter the codinate of you move x,y: ")
            
            #Remove any whitespace
            move = move.strip()
            
            move_y = int(move[0])
            move_x = int(move[2])
            
            #Check if place is taken
            if game[move_x][move_y] == " ":
                
                game[move_x][move_y] = token
                making_move = False
                
            else:
                print("ERROR: THe square is taken")
        
        
        except:
            print("ERROR: Please enter a valid value")
            
        
        
      
    #Check for win
    
    
    row_complete = (game[move_x][0] == game[move_x][1] == game[move_x][2])
    column_complete = (game[0][move_y] == game[1][move_y] == game[2][move_y])
    diagonal_rl_complete = (game[0][0] == game[1][1] == game[2][2] and game[0][0] != " "  and game[1][1] != " "  and game[2][2] != " " )
    diagonal_lr_complete = (game[2][0] == game[1][1] == game[0][2] and game[2][0] != " "  and game[1][1] != " "  and game[0][2] != " " )
    
    if row_complete or column_complete or diagonal_rl_complete or diagonal_lr_complete:
        
        draw_board()
        
        if token == "x":
            print("Player one wins")
        else:
            print("Player two wins")
        
        
        cont = input("Press any key to continue")
        
        game = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]

        
    if game[0][0] != " "  and game[0][1] != " "  and game[0][2] != " " and game[1][0] != " "  and game[1][1] != " "  and game[1][2] != " " and game[2][0] != " "  and game[2][1] != " "  and game[2][2] != " " :
    
        print("Game drawn")
        cont = input("Press any key to continue")
        

        game = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]
         
    
        
    if token == "x":
        token = "o"
    elif token == "o":
        token = "x"
        
        
  
        



#Remove the comma from the move and split them into two seperate vars