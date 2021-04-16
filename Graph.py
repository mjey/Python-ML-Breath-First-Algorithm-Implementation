from State import TERMINAL_STATE

import time
class Graph:
	def __init__(self):
		self.bfs_parent = {}
		self.dfs_parent = {}
		self.expandedBFS = 0

	def Breath_First_Search(self, s):
		self.expandedBFS = 0
		self.bfs_parent[s] = None
		visited = {(s.missionaries, s.cannibals, s.dir): True}
		s.level = 0
		start_time = time.time()
		queue = [s]
		while queue:
			self.expandedBFS += 1
			u = queue.pop(0)
			if u.IS_Goal_State():
				print("No of Expanded Nodes: " + str(self.expandedBFS))
				print("No of Explored Nodes: " + str(visited.__len__()))
				queue.clear()
				self.bfs_parent[TERMINAL_STATE] = u
				return self.bfs_parent
			# Stops searching after a certain time/node limit 
			t = time.time() - start_time
			if t > u.CONSTANTS.MAX_TIME or self.expandedBFS > u.CONSTANTS.MAX_NODES:
				if t > u.CONSTANTS.MAX_TIME:
					print("%.2fs EXCEEDED TIME LIMIT of %.2fs" % (t, u.CONSTANTS.MAX_TIME))
				else:
					print("EXCEEDED NODE LIMIT of %d" % u.CONSTANTS.MAX_NODES)
				print("No of Expanded Nodes: " + str(self.expandedBFS))
				print("No of Explored Nodes: " + str(visited.__len__()))
				queue.clear()
				return {}

			for v in reversed(u.SUCCESSORS()):
				if (v.missionaries, v.cannibals, v.dir) not in visited.keys():
					self.bfs_parent[v] = u
					v.level = u.level + 1
					queue.append(v)
					visited[(v.missionaries, v.cannibals, v.dir)] = True
		return {}

	# Prints the path returned by BFS/DFS
	def Print_PATH(self, parentList, tail):
		if tail is None:
			return
		if parentList == {} or parentList is None:  # tail not in parentList.keys():
			return
		if tail == TERMINAL_STATE: tail = parentList[tail]
		stack = []
		while tail is not None:
			stack.append(tail)
			tail = parentList[tail]

		while stack:
			print(stack.pop())
