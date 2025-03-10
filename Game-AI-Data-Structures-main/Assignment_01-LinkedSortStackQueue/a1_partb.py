#    Main Author(s): Hyeri Jang
#    Main Reviewer(s): Christine Ang, Shu-Ting Hsu




class SortedList:

	class Node:
		def __init__(self, data, next = None, prev = None):
			self.data = data
			self.next = next
			self.prev = prev

		def get_data(self):
			return self.data

		def get_next(self):
			return self.next

		def get_previous(self):
			return self.prev

	def __init__(self):
		self.front = self.Node(None)
		self.back = self.Node(None)
		self.front.next = self.back
		self.back.prev = self.front

	def get_front(self):
		if self.is_empty():
			return None
		else:
			return self.front.next

	def get_back(self):
		if self.is_empty():
			return None
		else:
			return self.back.prev

	def is_empty(self):
		return self.front.next == self.back

	def __len__(self):
		count = 0
		curr = self.front.next
		
		while curr != self.back:
			count += 1
			curr = curr.next

		return count

	def insert(self, data):
		curr = self.front.next

		while curr != self.back:
			if data <= curr.data:
				prev_node = curr.prev            
				next_node = curr

				new_node = self.Node(data, next_node, prev_node)
				prev_node.next = new_node
				next_node.prev = new_node

				return new_node	
			curr = curr.next

		prev_node = self.back.prev
		next_node = self.back

		new_node = self.Node(data, next_node, prev_node)
		prev_node.next = new_node
		next_node.prev = new_node

		return new_node

	def erase(self, node):
		if node == None:
			raise ValueError('Cannot erase node referred to by None')
		
		curr = self.front.next
		while curr != self.back:
			if curr == node:
				curr.prev.next = curr.next
				curr.next.prev = curr.prev
				del curr
				return 			
			curr = curr.next

	def search(self, data):
		target = None
		curr = self.front.next

		while curr != self.back:
			if curr.data == data:
				target = curr
				break
			curr = curr.next

		return target

