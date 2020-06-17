from random import *

def convert2d(board): #1dboard
	for i in range(0,7,1):
		accum[0][i]=board[i]
	for i in range(8,15,1):
		accum[1][i]=board[i]
	for i in range(16,23,1):
		accum[2][i]=board[i]
	for i in range(24,31,1):
		accum[3][i]=board[i]
	for i in range(32,39,1):
		accum[4][i]=board[i]
	for i in range(40,47,1):
		accum[5][i]=board[i]
	for i in range(48,55,1):
		accum[6][i]=board[i]
	for i in range(56,63,1):
		accum[7][i]=board[i]
	return accum

def covertback(board):
	for i in range(0,7,1):
		for j in range(0,7,1):
			accum[i+j]=board[i][j]

def genBoard():
    board = [13,11,12,14,15,12,11,13,10,10,10,10,10,10,10,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,20,20,20,20,20,20,23,21,22,24,25,22,21,23]
    return board

def PseudoLegalMoves(board,position):
	if board[position]==10 or board[position]==20: #Pawn
		accum=Pawn(board,position)
		return accum
		
	if board[position]==11 or board[position]==21: #Knight
		accum=Knight(board,position)
		return accum

	if board[position]==12 or board[position]==22: #Bishop
		accum=Bishop(board,position)
		return accum

	if board[position]==13 or board[position]==23: #Rook
		accum=Rook(board,position)
		return accum

	if board[position]==14 or board[position]==24: #Queen
		accum=Queen(board,position)
		return accum

	if board[position]==15 or board[position]==25: #King
		accum=King(board,position)
		return accum

	return []

def checkcheck(board,player):
	kingLoc=0
	for i in range(0, 63, 1):
		if board[i]==player+5:
			kingLoc=i
			break
	if IsPositionUnderThreat(board,kingLoc,player)==True:
		return True
	else:
		return False

def checkmate(board):
	accum=0
	if checkcheck(board,10)==True:
		for i in GetPlayerPositions(board, 10):
			for j in GetPieceLegalMoves(board,i):
				accum=accum+1
		if accum==0:
			return True
	if checkcheck(board,20)==True:
		for i in GetPlayerPositions(board, 20):
			for j in GetPieceLegalMoves(board,i):
				accum=accum+1
		if accum==0:
			return True
	return False

def getplayer(board,position):
	if position>63 or position<0:
		return False
	if (board[position]==0):
		return 0
	elif (board[position]>=20):
		return 20
	elif (board[position]<20) and (board[position]>=10):
		return 10

#______________________________________________________________________________________________________________________________________
#Assignment fcns
def GetPlayerPositions(board,player):
	accum=[]
	if player==20:
		for i in range(0,len(board),1):
			if (board[i]>=20):
				accum=accum+[i]
	if player==10:
		for i in range(0,len(board),1):
			if (board[i]<20) and (board[i]>=10):
				accum=accum+[i]
	return accum

def GetPieceLegalMoves(board,position):
	moves=[]
	player=getplayer(board,position)
	Pseudo=PseudoLegalMoves(board,position)
	for i in Pseudo:
		temp=list(board)
		temp[i]=temp[position]
		temp[position]=0
		if checkcheck(temp,player)==False:
			moves=moves+[i]
	return moves

def IsPositionUnderThreat(board,position,player):
	enemy=0
	if player==20:
		enemy=10
	if player==10:
		enemy=20
	enemypositions=GetPlayerPositions(board,enemy)
	enemymoves=[]
	for i in enemypositions:
		enemymoves=PseudoLegalMoves(board,i)
		for i in enemymoves:
			if i==position:
				return True
	return False

#_____________________________________________________________________________________________________________________________________
#Actual algorithm here [Assign 4]
def chessPlayer(B, player):
	board=list(B)
	evalTree=[]
	x=getBestMove(board, player)
	if x==False:
		return [False, None, None, None]
	else:
		return [True, x[0], x[2], x[1]]
		
#_____________________________________________________________________________________________________________________________________
#Piecewise helper fcns

def Pawn(board,position):
	accum=[]
	di=int(position//8)
	dj=int(position%8)
	pl=getplayer(board, position)
	if pl==False:
		return []

	if getplayer(board,position)==10:
		if (di+1)<8:
			if board[position+8]==0: #empty
				accum=accum+[position+8]
		if (dj+1<8):
			if getplayer(board, position+9)==20: 
				accum=accum+[position+9]
		if (dj-1<=0):
			if getplayer(board, position+7)==20: 
				accum=accum+[position+7]
		return accum

	if getplayer(board,position)==20:
		if (di-1)>=0:
			if board[position-8]==0: #empty
				accum=accum+[position-8]
		if (dj+1<8):
			if getplayer(board, position-7)==20: 
				accum=accum+[position-7]
		if (dj-1<=0):
			if getplayer(board, position-9)==20: 
				accum=accum+[position-9]
		return accum

def Knight(board,position):
	accum=[]
	di=int(position//8)
	dj=int(position%8)
	pl=getplayer(board, position)
	if pl==False:
		return []


	if (di-2>=0) and (dj-1>=0):
		if getplayer(board, position-17)!=pl: 
			accum=accum+[position-17]

	if (di-2>=0) and (dj+1<8):
		if getplayer(board, position-15)!=pl: 
			accum=accum+[position-15]

	if (di+2<8) and (dj+1<8):
		if getplayer(board, position+17)!=pl: 
			accum=accum+[position+17]

	if (di+2<8) and (dj-1>=0):
		if getplayer(board, position+15)!=pl: 
			accum=accum+[position+15]

	if (di-1>=0) and (dj-2>=0):
		if getplayer(board, position-10)!=pl: 
			accum=accum+[position-10]

	if (di-1>=0) and (dj+2<8):
		if getplayer(board, position-6)!=pl: 
			accum=accum+[position-6]

	if (di+1<8) and (dj+2<8):
		if getplayer(board, position+10)!=pl: 
			accum=accum+[position+10]

	if (di+1<8) and (dj-2>=0):
		if getplayer(board, position+6)!=pl: 
			accum=accum+[position+6]
	
	return accum

def Bishop(board,position):
	accum=[]
	
	pl=getplayer(board, position)
	if pl==False:
		return []


	Block=False
	di=int(position//8)
	dj=int(position%8)
	i=1
	while Block==False:		
		if (dj+i>=8) or (di+i>=0):
			Block=True
			break
		if getplayer(board, position+9*i)==pl:
			Block=True
			break
		if (dj+i<8) and (di+i<8):
			if getplayer(board, position+9*i)!=pl: 
				accum=accum+[position+9*i]
		if getplayer(board, position+9*i)!=pl and getplayer(board, position+9*i)!=0:
			Block=True
			break
		i=i+1

	Block=False
	di=int(position//8)
	dj=int(position%8)
	i=1
	while Block==False:		
		if (dj+i>=8) or (di-i<0):
			Block=True
			break
		if getplayer(board, position-7*i)==pl:
			Block=True
			break
		if (dj+i<8) and (di-i>=0):
			if getplayer(board, position-7*i)!=pl: 
				accum=accum+[position-7*i]	
		if getplayer(board, position-7*i)!=pl and getplayer(board, position-7*i)!=0:
			Block=True
			break
		i=i+1



	Block=False
	di=int(position//8)
	dj=int(position%8)
	i=1	
	while Block==False:		
		if (di+i>=8) or (dj-i<0):
			Block=True
			break
		if getplayer(board, position+7*i)==pl:
			Block=True
			break
		if (di+i<8) and (dj-i>=0):
			if getplayer(board, position+7*i)!=pl: 
				accum=accum+[position+7*i]
		if getplayer(board, position+7*i)!=pl and getplayer(board, position+7*i)!=0:
			Block=True
			break
		i=i+1

	Block=False
	di=int(position//8)
	dj=int(position%8)
	i=1
	while Block==False:		
		if (di-i<0) or (dj-i<0):
			Block=True
			break
		if getplayer(board, position-9*i)==pl:
			Block=True
			break
		if (di-i>=0) and (dj-i>=0):
			if getplayer(board, position-9*i)!=pl: 
				accum=accum+[position-9*i]
		if getplayer(board, position-9*i)!=pl and getplayer(board, position-9*i)!=0:
			Block=True
			break
		i=i+1

	return accum

def Rook(board,position):
	accum=[]
	
	pl=getplayer(board, position)
	if pl==False:
		return []
	Block=False
	di=int(position//8)
	dj=int(position%8)
	i=1
	while Block==False:
		if (dj+i>=8):
			Block=True
			break
		if getplayer(board, position+i)==pl:
			Block=True
			break
		if (dj+i<8):
			if getplayer(board, position+i)!=pl: 
				accum=accum+[position+i]
		if getplayer(board, position+i)!=pl and getplayer(board, position+i)!=0:
			Block=True
			break
		i=i+1

	Block=False
	di=int(position//8)
	dj=int(position%8)
	i=1
	while Block==False:
		if (dj-i<0):
			Block=True
			break
		if getplayer(board, position-i)==pl:
			Block=True
			break
		if (dj-i>=0):
			if getplayer(board, position-i)!=pl: 
				accum=accum+[position-i]
		if getplayer(board, position-i)!=pl and getplayer(board, position-i)!=0:
			Block=True
			break
		i=i+1



	Block=False
	di=int(position//8)
	dj=int(position%8)
	i=1	
	while Block==False:
		if (di+i>=8):
			Block=True
			break
		if getplayer(board, position+8*i)==pl:
			Block=True
			break
		if (di+i<8):
			if getplayer(board, position+8*i)!=pl: 
				accum=accum+[position+8*i]
		if getplayer(board, position+8*i)!=pl and getplayer(board, position+8*i)!=0:
			Block=True
			break
		i=i+1

	Block=False
	di=int(position//8)
	dj=int(position%8)
	i=1
	while Block==False:
		if (di-i<0):
			Block=True
			break
		if getplayer(board, position-8*i)==pl:
			Block=True
			break
		if (di-i>=0):
			if getplayer(board, position-8*i)!=pl: 
				accum=accum+[position-8*i]
		if getplayer(board, position-8*i)!=pl and getplayer(board, position-8*i)!=0:
			Block=True
			break
		i=i+1

	return accum

def Queen(board,position):
	accum=[]
	pl=getplayer(board, position)
	if pl==False:
		return []
	accum=accum+Rook(board,position)+Bishop(board,position)
	return accum

def King(board,position):
	accum=[]
	di=int(position//8)
	dj=int(position%8)
	pl=getplayer(board, position)
	if pl==False:
		return []


	if (dj-1>=0):
		if getplayer(board, position-1)!=pl: 
			accum=accum+[position-1]

	if (dj+1<8):
		if getplayer(board, position+1)!=pl: 
			accum=accum+[position+1]



	if (di+1<8) and (dj-1>=0):
		if getplayer(board, position+7)!=pl: 
			accum=accum+[position+7]

	if (di+1<8):
		if getplayer(board, position+8)!=pl: 
			accum=accum+[position+8]

	if (di+1<8) and (dj+1<8):
		if getplayer(board, position+9)!=pl: 
			accum=accum+[position+9]



	if (di-1>=0) and (dj+1<8):
		if getplayer(board, position-7)!=pl: 
			accum=accum+[position-7]

	if (di-1>=0):
		if getplayer(board, position-8)!=pl: 
			accum=accum+[position-8]

	if (di-1>=0) and (dj-1>=0):
		if getplayer(board, position-9)!=pl: 
			accum=accum+[position-9]
	
	return accum

#_____________________________________________________________________________________________________________________________________
#Minimax
def minimax(B, depth, player, tree, alpha, beta): #alpha= -inf beta= +inf
	board=list(B)
	if depth==0 or checkmate(board)==True:
		return [staticEval(board), board]

	if player==10:
		maxEval=(-999999999)
		for position in GetPlayerPositions(board,10):
			for i in GetPieceLegalMoves(board, position):
				board[i]=board[position]
				board[position]=0
				tree=tree+[board]
				Eval=minimax(board, depth -1, 20, tree, alpha, beta)
				maxEval=max(maxEval, Eval[0])
				alpha = max(alpha, Eval[0])
				if beta <= alpha:
					break
		return [maxEval, tree] #i=endpos, position=startpos

	if player==20:
		minEval=99999999
		for position in GetPlayerPositions(board,20):
			for i in GetPieceLegalMoves(board, position):
				board[i]=board[position]
				board[position]=0
				tree=tree+[board]
				Eval=minimax(board, depth -1, 10, tree, alpha, beta)
				minEval=min(minEval, Eval[0])
				beta = min(beta, Eval[0])
				if beta <= alpha:
					break
		return [minEval, tree]
	else:
		return False

def getBestMove(board, player):
	B=list(board)
	startpos=[]
	endpos=[]
	tree=[board]
	acc=[]
	cM=[]
	for i in GetPlayerPositions(board, player):
		for j in GetPieceLegalMoves(board,i):
				B[j]=B[i]
				B[i]=0
				x=minimax(B, 2, player, tree, -999999999, 999999999)
				if x==False:
					return False
				acc=acc+[x[0]]
				startpos=startpos+[i]
				endpos=endpos+[j]
				tree=tree+[x[1]]
				cM=cM+[[[j,i],x[0]]]
	if player==10:
		index=acc.index(max(acc))


	if player==20:
		index=acc.index(min(acc))

	move=[endpos[index], startpos[index]]

	return [move, tree, cM]

#_____________________________________________________________________________________________________________________________________
#Minimax helper fcns
def staticEval(board):
	Eval=0
	for i in range(0,63,1):
		if board[i]==10:
			x=PawnEval(i, getplayer(board,i))
			Eval=Eval+x

		if board[i]==20: #Pawn
			x=PawnEval(i, getplayer(board,i))
			Eval=Eval+x
		
		if board[i]==11:
			x=KnightEval(i, getplayer(board,i))
			Eval=Eval+3*x

		if board[i]==21: #Knight
			x=KnightEval(i, getplayer(board,i))
			Eval=Eval+3*x


		if board[i]==12:
			x=BishopEval(i, getplayer(board,i))
			Eval=Eval+3*x

		if board[i]==22: #Bishop
			x=BishopEval(i, getplayer(board,i))
			Eval=Eval+3*x

		if board[i]==13:
			x=RookEval(i, getplayer(board,i))
			Eval=Eval+5*x

		if board[i]==23: #Rook
			x=RookEval(i, getplayer(board,i))
			Eval=Eval+5*x

		if board[i]==14:
			x=QueenEval(i, getplayer(board,i))
			Eval=Eval+9*x

		if board[i]==24: #Queen
			x=QueenEval(i, getplayer(board,i))
			Eval=Eval+9*x

		if board[i]==15:
			x=KnightEval(i, getplayer(board,i))
			Eval=Eval+90*x

		if board[i]==25: #King
			x=KnightEval(i, getplayer(board,i))
			Eval=Eval+90*x

	return float(Eval)

def PawnEval(position, player):
	Eval=0
	B=[
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
    [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
    [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
    [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
    [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
    [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
    ]

	i=int(position//8)
	j=int(position%8)
	if player==10:
		Eval=B[i][j]
	if player==20:
		Eval=-1*(B[7-i][j])
	return Eval

def KnightEval(position, player):
	Eval=0
	B=[
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
    [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
    [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
    [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
    [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
    [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
    ]
	i=int(position//8)
	j=int(position%8)
	if player==10:
		Eval=B[i][j]
	if player==20:
		Eval=-1*(B[7-i][j])
	return Eval

def BishopEval(position, player):
	Eval=0
	B=[
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
	]
	i=int(position//8)
	j=int(position%8)
	if player==1:
		Eval=float(B[i][j])
	if player==2:
		Eval=-1*(float(B[7-i][j]))
	return float(Eval)

def RookEval(position, player):
	Eval=0
	B=[
    [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
	]
	i=int(position//8)
	j=int(position%8)
	if player==10:
		Eval=float(B[i][j])
	if player==20:
		Eval=-1*(float(B[7-i][j]))
	return float(Eval)

def QueenEval(position,player):
	B=[
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
	]
	i=int(position//8)
	j=int(position%8)
	if player==10:
		Eval=float(B[i][j])
	if player==20:
		Eval=-1*(float(B[7-i][j]))
	return float(Eval)

def KingEval(position,player):
	Eval=0
	B=[
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
    [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]
	]
	i=int(position//8)
	j=int(position%8)
	if player==10:
		Eval=float(B[i][j])
	if player==20:
		Eval=-1*(float(B[7-i][j]))
	return float(Eval)
