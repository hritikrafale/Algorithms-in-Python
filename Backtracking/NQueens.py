#check is Safe

def isSafe(chess_board,i,j,N):

	#checking row

	for k in range(0,i):
		if(chess_board[k][j]==1):
			return -1

	#checking column 
	for k in range(0,j):
		if(chess_board[i][j]==1):
			return -1

	#checking left diagonal
	temp,temp1=i,j
	while((temp>=0)and(temp1>=0)):
		if(chess_board[temp][temp1]==1):
			return -1
		temp=temp-1
		temp1=temp1-1	

	#checking right diagonal
	
	while((i<=N-1)and(j<=N-1)):
		if(chess_board[i][j]==1):
			return -1
		i=i-1
		j=j+1
	return 1		



#NQueens Problem

def NQueen(chess_board,i,N):
	#recursive step
	if(N==i):
		return 1
	else:
		for j in range(0,N):
			if(isSafe(chess_board,i,j,N)==1):
				chess_board[i][j]=1
				check=NQueen(chess_board,i+1,N)
				if(check==1):
					return 1
			chess_board[i][j]=0
		return -1		



# main function

N=4

chess_board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

NQueen(chess_board,0,4)
for i in range(0,N):
	print("\n")
	for j in range(0,N):
		print(chess_board[i][j],end=" "),