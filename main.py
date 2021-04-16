import sys
import time

from Graph import Graph
from State import State, Direction, TERMINAL_STATE
from Constants import CONST

CON_IN = sys.stdin
CON_OUT = sys.stdout

# Generate All possible next moves for each state to reduce number of iterations on each node
def Generate_All_Possible_Moves(CAP_BOAT):
	moves = []
	for m in range(CAP_BOAT + 1):
		for c in range(CAP_BOAT + 1):
			if 0 < m < c:
				continue
			if 1 <= m + c <= CAP_BOAT:
				moves.append((m, c))
	return moves


def RUN_BreathFirst(g, INITIAL_STATE):
	sys.stdout = open("BFS_OUTPUT.txt", "w")
	print("\n\nBreath First Search :: \n")
	start_time = time.time()
	p = g.Breath_First_Search(INITIAL_STATE)
	end_time = time.time()
	# print("Printing Solution...")
	if len(p):
		g.Print_PATH(p, TERMINAL_STATE)
	else:
		print("No Solution")
	print("\n Elapsed time in BFS: %.2fms" % ((end_time - start_time)*1000))

def main():
	sys.stdin = open("Inputs.txt", "r")

	m = int(input("m="))
	print(m, end="\n")
	c = int(input("c="))
	print(c, end="\n")
	k = int(input("k="))
	print(k, end="\n")
	t = int(input("TIME_LIMIT_s="))
	print(t, end="\n")
	n = int(input("NODE_LIMIT="))
	print(n, end="\n")

	CNST = CONST(m, c, k, t, n)

	moves = Generate_All_Possible_Moves(CNST.CAP_BOAT)
	print(str(moves.__len__())+" iterations per Node.")

	INITIAL_STATE = State(CNST.MAX_M, CNST.MAX_C, Direction.OLD_TO_NEW, 0, 0, 0, CNST, moves)
	# TERMINAL_STATE = State(-1, -1, Direction.NEW_TO_OLD, -1, -1, 0)

	g = Graph()
	sys.stdout = CON_OUT
	print("\nRunning Breath First Search >>")
	RUN_BreathFirst(g, INITIAL_STATE)
	sys.stdout = CON_OUT
	print("Executed Breath First in BFS_OUTPUT.txt >>")

if __name__ == '__main__':
	main()
