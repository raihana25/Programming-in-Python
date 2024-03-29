'''Repeatedly ask the user to enter a team name and how many games a team has won or lost. Store this info in a dictionary, with team name as keys and values as a list of the form [wins,losses).Use the dictionary to do the following.
• Print names of all teams.
• Print name of team with highest wins
• Print name of team with highest losses
• Allow user to enter the team name and print the teams win percentage'''
print("************Match Leaderboard************\n\n")
board={}

while(True):
    name=input("Enter team name: ")
    result=input("Enter wins and losses\n): ")
    result=[int(input("result: ")) for i in range(0,2) ]
    board[name]=result
    
    c=input("Add another match? (y/n): ")
    if (c=="n"):
        break

print("Team\tWin|Lose")
for i,j in board.items():
    print(i,"\t",j)

w=[]
l=[]
teams=list(board.keys())
winloss=list(board.values())
for  item in winloss:
    w.append(item[0])
    l.append(item[1])
indexw=w.index(max(w))
indexl=l.index(max(l))
print("winner: ",teams[indexw],"\nloser: ", teams[indexl])


name=input("Enter team name to check win percentage ")
print(board[name][0]*100/(board[name][0]+board[name][1]))
