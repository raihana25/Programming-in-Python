'''Repeatedly ask the user to enter a team name and how many games a team has won or lost. Store this info in a dictionary, with team name as keys and values as a list of the form [wins,losses).Use the dictionary to do the following.
• Print names of all teams.
• Print name of team with highest wins
• Print name of team with highest losses
• Allow user to enter the team name and print the teams win percentage'''
print("************Match Leaderboard************\n\n")
board={}

while(True):
    name=input("Enter team name: ")
    result=input("Enter result(w/l): ")
    if (name not in board):
        if(result=="w"):
            board[name]=[1,0]
        else:
            board[name]=[0,1]
    else:
        if (result=="w"):
            board[name][0]+=1
        else:
            board[name][1]+=1
    
    c=input("Add another match? (y/n): ")
    if (c=="n"):
        break

print("Team\tWin|Lose")
for i,j in board.items():
    print(i,"\t",j)
#board={1:[10,1],2:[99,0]}
#print (max(board))
#print (min(board))
'''res=[key for key in board if all(board[tmp]<=board[key] for tmp in board)]
#print(str(res))'''

name=input("Enter team name to check win percentage ")
print(board[name][0]*100/(board[name][0]+board[name][1]))