"""
	Grafo para Trabalho de AA: Coloração de Vértices

	pair(u, v): edge between "u" and "v"
		*	u: vertex "u"
		*	v: vertex "v"

	https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/?ref=ghm
"""

#	A class to represent the adjacency list of the node
from typing import Collection


class AdjNode:

	def __init__(self, data):
		self.vertex = data
		self.next = None

#	A class to represent a graph.
class Graph:
	VColor: list = []
	color = ["red", "green", "blue", "cyan", "magenta", "yellow", "black"]

	def __init__(self, vertices):
		self.V = vertices

		#	Initializing default None color
		i = 0
		while(i < vertices):
			self.VColor.append("")
			i += 1
			
		self.graph = [None] * self.V
		return

	#	Function to add an edge in an undirected graph
	def addEdge(self, src, dest):
		#	Adding the node to the source node
		node = AdjNode(dest)
		node.next = self.graph[src]
		# node.value = color
		self.graph[src] = node


		#	Adding the source node to the destination as it is the undirected graph
		node = AdjNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node
		return

	#	Function to print the graph
	def printGraph(self):
		for i in range(self.V):
			print("Adjacency list of vertex {}\nHeader".format(i), end="")
			temp = self.graph[i]
			while(temp):
				print(" -> {}".format(temp.vertex), end="")
				temp = temp.next
			print("\n")
		return
	
	#	Function to print the graph colorized
	def printColorGraph(self):
		i = 0
		while(i < self.V):
			print("Adjacency Colorized list of vertex {}\n{}:".format(i, self.VColor[i]), end="")
			temp = self.graph[i]
			while(temp):
				print(" -> {}".format(temp.vertex), end="")
				temp = temp.next
			
			print("\n")
			i += 1
		return

	def colorizeGraph(self):
		
		return
	


if(__name__ == "__main__"):
	V = 5
	graph = Graph(V)
	graph.addEdge(0, 1)
	graph.addEdge(0, 2)
	graph.addEdge(0, 3)

	graph.addEdge(1, 4)
	graph.addEdge(1, 5)

	graph.addEdge(4, 6)
	graph.addEdge(4, 9)

	graph.addEdge(6, 2)
	graph.addEdge(6, 8)

	graph.addEdge(2, 7)

	graph.addEdge(7, 5)
	graph.addEdge(7, 9)

	graph.addEdge(5, 8)

	graph.addEdge(8, 3)

	graph.addEdge(3, 9)

	graph.printGraph()

	graph.colorizeGraph()
	graph.printColorGraph()


"""
(0,1)
(0,2)
(0,3)

(1,4)
(1,5)

(4,6)
(4,9)

(6,2)
(6,8)

(2,7)

(7,5)
(7,9)

(5,8)

(8,3)

(3,9)
"""