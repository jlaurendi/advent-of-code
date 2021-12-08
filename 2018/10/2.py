import sys, copy

num_p = 448
last_marble = 7162800

# num_p = 9
# last_marble = 25
class Node:
	def __init__(self, value, prevNode=None, nextNode=None):
		self.value = value
		self.prevNode = prevNode
		self.nextNode = nextNode

	def __str__(self):
		return str(self.value)


class LinkedList:
	def __init__(self):
		self.curr_node = None

	def append(self, value):
		node = Node(value)
		if self.curr_node == None:
			node.prevNode = node
			node.nextNode = node
		else:
			node.prevNode = self.curr_node
			node.nextNode = self.curr_node.nextNode
			self.curr_node.nextNode.prevNode = node
			self.curr_node.nextNode = node
		self.curr_node = node

	def moveLeft(self, n):
		for i in xrange(n):
			self.curr_node = self.curr_node.prevNode

	def moveRight(self, n):
		for i in xrange(n):
			self.curr_node = self.curr_node.nextNode

	def removeCurrentNode(self):
		self.curr_node.prevNode.nextNode = self.curr_node.nextNode
		self.curr_node.nextNode.prevNode = self.curr_node.prevNode
		self.curr_node = self.curr_node.nextNode


	def __str__(self):
		out_string = "["
		curr = self.curr_node
		while True:
			out_string += str(curr.value) + ', '
			curr = curr.nextNode

			if curr == self.curr_node.prevNode:
				break

		return out_string[0:-2] + "]"


marbles = LinkedList()
marbles.append(0)
curr_p = 1
scores = {}
for i in xrange(1, last_marble):
	# print marbles.curr_node, marbles
	if i % 23 == 0:
		if curr_p not in scores:
			scores[curr_p] = 0
		scores[curr_p] += i
		# print marbles.curr_node

		marbles.moveLeft(7)
		# print marbles.curr_node
		scores[curr_p] += marbles.curr_node.value
		marbles.removeCurrentNode()
	else:
		marbles.moveRight(1)
		marbles.append(i)

	curr_p = (curr_p+1) % num_p


print max(scores.values())
