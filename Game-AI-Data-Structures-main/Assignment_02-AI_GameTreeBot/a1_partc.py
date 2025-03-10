#    Main Author(s): Casey Hsu
#    Main Reviewer(s): Christine Ang and Hyeri Jang

class Stack:
	# A Stack is a data structure that follows the FILO (First In Last Out) rule

	# Initializes the Stack 
	# Default capacity is 10
        # cap: The initial capacity of the Stack
	def __init__(self, cap=10):
		self.size_limit = cap
		self.stack = [None] * self.size_limit
		self.size = 0

	
	# Returns the current capacity of the Stack
	# return: The total capacity of the Stack
	def capacity(self):
		return self.size_limit

	
	# Adds an element to the top of the Stack
	# If the Stack is full, the capacity is doubled
	# data: The element to add to the Stack
	def push(self, data):
		# Resize the stack when capacity is exceeded
		if self.size >= self.size_limit:
			self.size_limit *=2
			new_stack = [None] * self.size_limit
			for i in range(self.size):
				new_stack[i] = self.stack[i]
			self.stack = new_stack

		# adds data to the "top" of the Stack
		self.stack[self.size]= data
		self.size += 1


	# Removes and returns the element from the top of the Stack
	# Raises IndexError if the Stack is empty
	# return: The top element of the Stack
	def pop(self):
		if self.size == 0:
			raise IndexError('pop() used on empty stack')
		
		top_value = self.stack[self.size - 1]

		# remove the top of item
		self.stack[self.size - 1] = None

		self.size -= 1

		return top_value

	# Returns the element at the top of the Stack without removing it
	# return: The top element, or None if the Stack is empty
	def get_top(self):
		if self.size == 0:
			return None
		# returns the the newest value  
		return self.stack[self.size - 1] 


	# Checks if the Stack is empty
	# return: True if empty, otherwise False
	def is_empty(self):
		if self.size == 0:
			return True
		else:
			return False

	# Returns the current number of elements in the Stack
	# return: The number of elements in the Stack
	def __len__(self):
		return self.size


class Queue:

	#This function initialises the Queue class members
	#It is passed a value assigned to the queue's capacity (default value is 10)
	def __init__(self, cap=10):
		self.queue = [None] * cap
		self.cap = cap
		self.used = 0
		self.front = 0
		self.back = 0

	#This function returns the queue's capacity
	def capacity(self):
		return self.cap

	#This function adds data to the back of the queue
	#If queue's used value is equal to the queue's capacity then resizing occurs, resizing doubles the capacity and copies the data to the new queue
	#This function uses a method of circular indexing via the use of the % operator
	#After insertion or resizing the data members are assigned new values
	#This function does not return anything
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

	#This function removes the oldest data from the value
	#Since it is a queue, the oldest data is the data at the "front" of the queue
	#After removal, data members: front & used are assigned new values
	#This function returns the value that is removed, and if the queue is empty it will raise the IndexError
	def dequeue(self):
		if self.is_empty():
			raise IndexError('dequeue() used on empty queue')
		else:
			front_value = self.queue[self.front]
			self.front = (self.front + 1) % self.cap
			self.used -= 1
		return front_value

	#This function returns the oldest value at the "front" of the queue, returns None if queue is empty
	def get_front(self):
		if self.is_empty():
			return None
		else:
			return self.queue[self.front]

	#This function returns a bool representing whether the queue is empty or not
	#If the queue's value is 0, it will return True. Otherwise, will return False. 
	def is_empty(self):
		if self.used == 0:
			return True
		else:
			return False

	#This function returns the queue's used value representing the length of the queue 
	def __len__(self):
		return self.used



class Deque:
	# A Deque is a data structure where elements can be added or removed from both ends (front and back).
	# It is implemented using a list with dynamic resizing when capacity is exceeded.
	
	# Initializes the Deque
	# Default capacity is 10
	# cap: The initial capacity of the Deque
	def __init__(self, cap=10):
		self.size_limit = cap
		self.deque = [None] * self.size_limit
		self.front = 0
		self.back = -1
		self.size = 0 

	
	# Returns the current capacity of the Deque
	# return: The total capacity of the Deque
	def capacity(self):
		return self.size_limit

	
	# Adds an element to the front of the Deque
	# If the Deque is full, the capacity is doubled
	# data: The element to add to the front
	def push_front(self, data):
		# size * 2
		if self.size >= self.size_limit:
			new_size_limit = self.size_limit * 2
			new_deque = [None] * new_size_limit
		
			# Rearrange the data into a new list
			for i in range(self.size):
				new_deque[i] = self.deque[(self.front + i) % self.size_limit]
			
			self.deque = new_deque
			self.size_limit = new_size_limit
			self.front = 0
			self.back = self.size - 1

		# Add data to front
		self.front = (self.front - 1) % self.size_limit
		self.deque[self.front] = data
		self.size += 1

	
	# Adds an element to the back of the Deque
	# If the Deque is full, the capacity is doubled
	# data: The element to add to the back
	def push_back(self, data):
		# size * 2
		if self.size >= self.size_limit:
			new_size_limit = self.size_limit * 2
			new_deque = [None] * new_size_limit
		
			# Rearrange the data into a new list
			for i in range(self.size):
				new_deque[i] = self.deque[(self.front + i) % self.size_limit]
			
			self.deque = new_deque
			self.size_limit = new_size_limit
			self.front = 0
			self.back = self.size - 1

		# Add data to backend
		self.back = (self.back + 1) % self.size_limit
		self.deque[self.back] = data
		self.size += 1	

	
	# Removes and returns the element from the front of the Deque
	# Raises IndexError if the Deque is empty
	# return: The front element of the Deque
	def pop_front(self):
		if self.size == 0:
			raise IndexError('pop_front() used on empty deque')
		
		front_value = self.deque[self.front]

		self.deque[self.front] = None

		self.front = (self.front + 1) % self.size_limit

		self.size -= 1

		return front_value

	
	# Removes and returns the element from the back of the Deque
	# Raises IndexError if the Deque is empty
	# return: The back element of the Deque
	def pop_back(self):
		if self.size == 0:
			raise IndexError('pop_back() used on empty deque')
		
		back_value = self.deque[self.back]

		# Remove the back item
		self.deque[self.back] = None 

		self.back = (self.back - 1) % self.size_limit

		self.size -= 1

		return back_value

	
	# Returns the element at the front of the Deque without removing it
	# return: The front element, or None if the Deque is empty
	def get_front(self):
		if self.size == 0:
			return None
		
		return self.deque[self.front]

	
	# Returns the element at the back of the Deque without removing it
	# return: The back element, or None if the Deque is empty
	def get_back(self):
		if self.size == 0:
			return None
		
		return self.deque[self.back]

	
	# Checks if the Deque is empty
	# return: True if empty, otherwise False
	def is_empty(self):
		if self.size == 0:
			return True
		else:
			return False

	
	# Returns the current number of elements in the Deque
	# return: The number of elements in the Deque
	def __len__(self):
		return self.size

	
	# Returns the k element from the front of the Deque without removing it
	# Raises IndexError if the index is out of range
	# k: Index of the element
	# return: The k element of the Deque
	def __getitem__(self, k):
		if k < 0 or k >= self.size:
			raise IndexError('Index out of range')
		
		return self.deque[(self.front + k) % self.size_limit]