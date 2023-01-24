import random

colone=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
def tableau():
    print(" ___________ ")
    print("| %c | %c | %c |" % (colone[1],colone[2],colone[3]))    
    print("|___|___|___|")    
    print("| %c | %c | %c |" % (colone[4],colone[5],colone[6]))    
    print("|___|___|___|")    
    print("| %c | %c | %c |" % (colone[7],colone[8],colone[9]))    
    print("|___|___|___|") 

def game():
    turn='x'
    count=0
    
    for i in range(10):
        tableau()
        
        print("c'est ton toure" , turn)
        deplacer=int(input("fait entrez ta case de choix:"))
        if colone[deplacer]==' ':
            colone[deplacer]=turn
            count+=1
        else:
            print("Ce lieu est déjà occupé.\nDéplacer vers quel lieu ?") 
            continue
        
        if count >= 5 :
            if colone[7] == colone[8] == colone[9] != ' ': # across the top
                tableau()
                print("\nGame Over.\n")                
                print(" gagner " +turn + " won. ****")                
                break
            elif colone[4] == colone[5] == colone[6] != ' ': # across the middle
                tableau()
                print("\nGame Over.\n")                
                print(" gagner " +turn + " won. ****")
                break
            elif colone[1] == colone[2] == colone[3] != ' ': # across the bottom
                tableau()
                print("\nGame Over.\n")                
                print(" gagner " +turn + " won. ****")
                break
                
            elif colone[1] == colone[4] == colone[7] != ' ': # down the left side
                tableau()
                print("\nGame Over.\n")                
                print(" gagner " +turn + " won. ****")
                break
            elif colone[2] == colone[5] == colone[8] != ' ': # down the middle
                tableau()
                print("\nGame Over.\n")                
                print(" gagner " +turn + " won. ****")
                break
            elif colone[3] == colone[6] == colone[9] != ' ': # down the right side
                tableau()
                print("\nGame Over.\n")                
                print(" gagner " +turn + " won. ****")
                break 
            elif colone[7] == colone[5] == colone[3] != ' ': # diagonal
                tableau()
                print("\nGame Over.\n")                
                print(" gagner " +turn + " won. ****")
                break
            elif colone[1] == colone[5] == colone[9   ] != ' ': # diagonal
                tableau()
                print("\nGame Over.\n")                
                print(" gagner " +turn + " won. ****")
                break 
        if count == 9:
            if colone[i]!=' ':
                
                print("\nGame Over.\n")                
                print("Nul!!")
            break

        if turn =='x':
            turn = 'O'
        else :
            turn = 'x'
        
game()
