#    Main Author(s): 
#    Main Reviewer(s):



class Stack:

	def __init__(self, cap):
		pass

	def capacity(self):
		pass

	def push(self, data):
		pass

	def pop(self):
		pass

	def get_top(self):
		pass

	def is_empty(self):
		pass

	def __len__(self):
		pass


class Queue:

	def __init__(self, cap=10):
		self.queue = [None] * cap
		self.cap = cap
		self.used = 0
		self.front = 0
		self.back = 0

	def capacity(self):
		return self.cap

	def enqueue(self, data):
		if self.used == self.cap:
			new_queue = [None] * (self.cap*2)
			
			for i in range(self.used):
				new_queue[i] = self.queue[(self.front + i) % self.cap]

			self.queue = new_queue
			self.cap *= 2
			self.front = 0
			self.back = self.used
		
		self.queue[self.back] = data
		self.back = (self.back + 1) % self.cap
		self.used += 1

	def dequeue(self):
		if self.is_empty():
			raise IndexError('dequeue() used on empty queue')
		else:
			front_value = self.queue[self.front]
			self.front = (self.front + 1) % self.cap
			self.used -= 1
		return front_value


	def get_front(self):
		if self.is_empty():
			return None
		else:
			return self.queue[self.front]

	def is_empty(self):
		if self.used == 0:
			return True
		else:
			return False

	def __len__(self):
		return self.used



class Deque:

	def __init__(self, cap):
		pass

	def capacity(self):
		pass

	def push_front(self, data):
		pass

	def push_back(self, data):
		pass

	def pop_front(self):
		pass

	def pop_back(self):
		pass

	def get_front(self):
		pass

	def get_back(self):
		pass

	def is_empty(self):
		pass

	def __len__(self):
		pass

	def __getitem__(self, k):
		pass
