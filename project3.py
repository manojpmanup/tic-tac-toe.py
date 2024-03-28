def tik_tac_toe():#dictionary for storing the data 
    tiktac={1:" ",2:" ",3:" ",
            4:" ",5:" ",6:" ",
            7:" ",8:" ",9:" "}
    def display_ticktoactoe(board):#displays  the tic-tac--toe board 
        print(board[1]+"|"+board[2]+"|"+board[3])
        print("____")
        print(board[4]+"|"+board[5]+"|"+board[6])
        print("____")
        print(board[7]+"|"+board[8]+"|"+board[9])
        print("____")
    display_ticktoactoe(tiktac)#calling of the display function
    def start_game():#defining the game function for starting the game
        turn="X"# ensures the turns 
        for i in range(1,10):
            print("in the"+str(i)+" round "+turn+" its ur turn")
            move=int(input("which place u what to place the"+turn+":"))
            if tiktac[move]=="X"or tiktac[move]=="O":#checking the slot is already filled or not
                move=int(input((turn+"enter a valid place: ")))#if slot already filled reentering the value
            tiktac[move]=turn #assigning the place to the player  
            display_ticktoactoe(tiktac)
            if tiktac[1]==tiktac[4]==tiktac[7]==turn or tiktac[2]==tiktac[5]==tiktac[8]==turn or tiktac[3]==tiktac[6]==tiktac[9]==turn or tiktac[1]==tiktac[2]==tiktac[3]==turn or tiktac[4]==tiktac[5]==tiktac[6]==turn or tiktac[7]==tiktac[8]==tiktac[9]==turn or tiktac[1]==tiktac[5]==tiktac[9]==turn or tiktac[3]==tiktac[5]==tiktac[7]==turn:
                    print("u won ",turn)
                    return
            elif turn=="X":
                turn="O"
            else:
                turn="X"
        print("all the posssible moves got over match draw")
    start_game()
tik_tac_toe()