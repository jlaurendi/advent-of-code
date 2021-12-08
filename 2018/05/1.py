import sys
with open('advent-input.txt') as f:
	a = f.readlines()[0]
	# a = 'dabAcCaCBAcCcaDA'
	a = [i for i in a]

class Node:
	def __init__(self, value, prevNode=None, nextNode=None):
		self.value = value
		self.prevNode = prevNode
		self.nextNode = nextNode

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, value):
		node = Node(value)
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			node.prevNode = self.tail
			if self.tail != None:
				self.tail.nextNode = node
			self.tail = node

	def remove(self, node):
		if node.prevNode != None:
			node.prevNode.nextNode = node.nextNode
		if node.nextNode != None:
			node.nextNode.prevNode = node.prevNode

		if self.head == node:
			self.head = node.nextNode

		if self.tail == node:
			self.tail = node.prevNode

	def length(self):
		count = 0
		curr = self.head
		while curr != None:
			count += 1
			curr = curr.nextNode
		return count

	def __str__(self):
		out_string = ""
		curr = self.head
		while curr != None:
			out_string += curr.value
			curr = curr.nextNode
		return out_string

lnk_list = LinkedList()
for i in a:
	lnk_list.append(i)

while True:
	curr_length = lnk_list.length()
	curr = lnk_list.head
	while curr.nextNode != None:
		x = curr.value
		y = curr.nextNode.value
		if x != y and x.lower() == y.lower():
			if curr.prevNode != None:
				tmp = curr.prevNode
			else:
				tmp = curr.nextNode.nextNode
			lnk_list.remove(curr)
			lnk_list.remove(curr.nextNode)
			curr = tmp
		else:
			curr = curr.nextNode

	if curr_length == lnk_list.length():
		print curr_length
		sys.exit()
