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

game = [["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]

playing_game = True

token = "x"

while playing_game :
    
    
    draw_board()
    
    #Take a coodirnate
    move = input("Please enter the codinate of you move x,y: ")
    
    #Remove any whitespace
    move = move.strip()
    
    move_y = int(move[0])
    move_x = int(move[1])
    
    game[move_x][move_y] = token
    
    if token == "x":
        token = "o"
    elif token == "o":
        token = "x"
        
        



#Remove the comma from the move and split them into two seperate vars