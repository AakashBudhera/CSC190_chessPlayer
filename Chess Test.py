from Chess import *

b=genBoard()

#b[34]=12
#b[18]=b[1]
#b[1]=0
#b[2]=0
#b[27]=b[63]
#b[63]=0

x=chessPlayer(b, 10)
print()
#x=getBestMove(b, 20)
print()
print(x[0], x[1], x[2])
print()

#print(chessPlayer(b, 20))	
#print(PawnEval(12, getplayer(b,12)))
#evalTree=[]
#print(minimax(b, 3, 10, evalTree,-999999999,999999999))
#print()
print(b)
#print(minimax(b, 34, 3, False, evalTree))

#_________________________________________________________________________________________________________________________
"""
def minimax(board, position, depth, maxplayer, tree):
	board=list(board)
	if depth==0 or (checkcheck(board, getplayer(board,position))==True and GetPieceLegalMoves(board,position)==[]):
		return [staticEval(board)]
	i=None

	if maxplayer==True:
		maxEval=(-999999999)
		for i in GetPieceLegalMoves(board, position):
			board[i]=board[position]
			board[position]=0
			tree=tree+[board]
			Eval=minimax(board, position, depth -1, False, tree)
			maxEval=max(maxEval, Eval[0])
			print("maxeval")
			print(maxEval)
			print()
		return [maxEval, tree, position, i] #i=endpos, position=startpos

	else:
		minEval=999999999
		for i in GetPieceLegalMoves(board, position):
			board[i]=board[position]
			board[position]=0
			tree=tree+[board]
			Eval=minimax(board, position, depth -1, True, tree)
			minEval=min(minEval, Eval[0])
			print("mineval")
			print(minEval)
			print()
		return [minEval, tree, position, i]




def chessPlayer(board, player):
	store=[0, None, None]
	evalTree=[]
	eval_out=[]
	startpos=[]
	endpos=[]
	candidateMoves=[]
	if player==10:
		maxplayer=True #white
		for i in GetPlayerPositions(board,player):
			x=minimax(board, i, 3, maxplayer, evalTree)
			eval_out=eval_out+[x[0]]
			startpos=startpos+[x[2]]
			endpos=endpos+[x[3]]
		for i in range(0, len(eval_out),1):	
			candidateMoves=candidateMoves+[[endpos[i],startpos[i]], eval_out[i]]
		max_index=eval_out.index(max(eval_out))
		start=startpos[max_index]
		end=endpos[max_index]
		return [True, [end ,start], candidateMoves, x[1]]

	if player==20:
		maxplayer=False #black
		for i in GetPlayerPositions(board,player):
			x=minimax(board, i, 3, maxplayer, evalTree)
			eval_out=eval_out+[x[0]]
			startpos=startpos+[x[2]]
			endpos=endpos+[x[3]]
		for i in range(0, len(eval_out),1):	
			candidateMoves=candidateMoves+[[endpos[i],startpos[i]], eval_out[i]]
		min_index=eval_out.index(min(eval_out))
		start=startpos[min_index]
		end=endpos[min_index]
		return [True, [end ,start], candidateMoves, x[1]]

	else:
		return [False, False, False, False]
"""
