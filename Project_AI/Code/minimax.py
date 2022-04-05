
from typing import List, Tuple, Union
import math

AI = 0
PLAYER = 1
BOARD_SIZE = 3
MINION_SIZE = 3

LEVEL_LG = 2
LEVEL_MD = 1
LEVEL_SM = 0

DEPTH = 5
DEF_ALPHA = -math.inf
DEF_BETA = math.inf

class Minion:
	owner: int
	level: int

	def __init__(self, owner, level):
		self.level = level
		self.owner = owner

BoardPosition = List[List[Union[None, Minion]]]

# 0: AI Win
# 1: Player Win
# 2: Tie
# 3: Continue
def is_game_over(position: BoardPosition) -> int:
	TIE = 2
	CONTINUE = 3
	# Diagonal check
	cur = None
	d_count = 0
	# Left Top to Right Btm diagonal
	for i in range(BOARD_SIZE):
		if cur is None and position[i][i] is not None:
			cur = position[i][i]
			d_count += 1
		elif cur is not None and position[i][i] is not None:
			if cur.owner == position[i][i].owner:
				d_count += 1
	
	if d_count == 3:
		return cur.owner

	cur = None
	d_count = 0
	for i in range(BOARD_SIZE):
		j = BOARD_SIZE - 1 - i
		if cur is None and position[i][j] is not None:
			cur = position[i][j]
			d_count += 1
		elif cur is not None and position[i][j] is not None:
			if cur.owner == position[i][j].owner:
				d_count += 1

	if d_count == 3:
		return cur.owner
		
	# Horizontal and vertical check
	for i in range(BOARD_SIZE):
		count_x = 0
		count_y = 0
		start_point_x = position[i][0]
		start_point_y = position[0][i]

		for j in range(1, BOARD_SIZE):

			if position[i][j] is not None:
				if start_point_x is not None and start_point_x.owner == position[i][j].owner:
					count_x += 1

			if position[j][i] is not None:
				if start_point_y is not None and start_point_y.owner == position[j][i].owner:
					count_y += 1

		if count_x == BOARD_SIZE - 1:
			return start_point_x.owner
		
		if count_y == BOARD_SIZE - 1:
			return start_point_y.owner

	# Full Check
	for i in range(BOARD_SIZE):
		for j in range(BOARD_SIZE):
			if position[i][j] is None:
				return CONTINUE
	return TIE

def is_eatable(minion, level, owner) -> bool:
	return (minion is None) or \
			(minion is not None and minion.level < level and owner != minion.owner)

class BoardState:
	value: int

	alpha: int
	beta: int

	player:List[int] = [MINION_SIZE for _ in range(0, 3)]
	ai: List[int] = [MINION_SIZE for _ in range(0, 3)]
	
	position: BoardPosition

	children: List['BoardState']

	def __init__(self, alpha = 999, beta = -999):
		self.position = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
		self.alpha = alpha
		self.beta = beta
		self.children = []

	def evaluate(self):
		pass

	def __repr__(self) -> str:
		rep = "\n"
		for i in self.position:
			for j in i:
				if j is not None:
					rep += "[{}{}]".format(j.owner, j.level)
				else: 
					rep += "[__]"
			rep += "\n"
		return rep

def copy_boardstate(board: BoardState) -> BoardState:
	b = BoardState(board.alpha, board.beta)
	b.player = board.player.copy()
	b.ai = board.ai.copy()

	for i in range(BOARD_SIZE):
		for j in range(BOARD_SIZE):
			if board.position[i][j] is not None:
				b.position[i][j] = Minion(board.position[i][j].owner, board.position[i][j].level)
			else:
				b.position[i][j] = None
	return b

def add_combination(combinations: List[BoardState], board: BoardState, user: int, level: int, row: int, col: int) -> None:
	if board.player[level] > 0 and is_eatable(board.position[row][col], level, user):
		b = copy_boardstate(board)
		b.position[row][col] = Minion(user, level)
		b.player[level] -= 1
		combinations.append(b)

def generate_moves(board: BoardState, player_turn) -> Union[List[BoardState], None]:
	if is_game_over(board.position) != 3:
		return None

	combinations: List[BoardState] = []
	for i in range(BOARD_SIZE):
		for j in range(BOARD_SIZE):
			if player_turn:
				user = PLAYER
				add_combination(combinations, board, user, LEVEL_LG, i, j)
				add_combination(combinations, board, user, LEVEL_MD, i, j)
				add_combination(combinations, board, user, LEVEL_SM, i, j)
			else:
				user = AI
				add_combination(combinations, board, user, LEVEL_LG, i, j)
				add_combination(combinations, board, user, LEVEL_MD, i, j)
				add_combination(combinations, board, user, LEVEL_SM, i, j)

	return combinations

def check_win(board):
	r = is_game_over(board.position)
	if r == 0: # AI WIN
		return 1
	elif r == 1: # PLAYER WIN
		return -1
	elif r == 2: # TIE 
		return 0
	else: # CONTINUE
		return r

def minimax(board, maximize, depth, max_depth, alpha, beta):
	# Return on max depth
	if depth == max_depth:
		return check_win(board) * (1/(depth + 1))

	# Return on win
	result = check_win(board)
	if result != 3:
		return result * (1/(depth + 1))

	# Generate all possible moves for the current board state
	x = generate_moves(board, maximize)

	# If no moves are generated, done (tie)
	if x == None or x == []:
		return 0
	
	board.children = x
	print(depth, board.children)

	new_depth = depth + 1
	if maximize:
		# Generate children for each child moves
		max_value = -math.inf
		for i in board.children:
			val = minimax(i, not maximize, new_depth, max_depth, alpha, beta)
			max_value = max(max_value, val)
			alpha = max(max_value, alpha)
			if beta <= alpha:
				break
		return max_value * (1/(depth + 1))
	else:
		# Generate children for each child moves
		min_value = math.inf
		for i in board.children:
			val = minimax(i, not maximize, new_depth, max_depth, alpha, beta)
			min_value = min(min_value, val)
			beta = min(min_value, alpha)
			if beta <= alpha:
				break
		return min_value * (1/(depth + 1))

	# # Generate children for each child moves
	# 	for i in board.children:
	# 		minimax(i, not maximize, new_depth, max_depth)

def find_best_move(board):
	AI = 0
	max_val = -math.inf
	best_move: Tuple[int, int, int] = (-1, -1, -1)

	if check_win(board) != 3:
		return None

	for i in range(BOARD_SIZE):
		for j in range(BOARD_SIZE):
			for k in range(3):
				if is_eatable(board.position[i][j], k, 0):
					# Assume move
					board.position[i][j] = Minion(0, k)
					val = minimax(board, True, 0, DEPTH, DEF_ALPHA, DEF_BETA)
					# Undo move
					board.position[i][j] = None

					if val > max_val:
						best_move = (i, j, k)
						max_val = val
	
	if best_move == None:
		raise ValueError("What??")

	return best_move

# b = BoardState()
# b.position = [
# 	[Minion(0,2), None, Minion(1, 2)],
# 	[None, Minion(1,0), None],
# 	[None, None, Minion(0,2)]
# ]

# # print(is_game_over(b.position))

# print(find_best_move(b))