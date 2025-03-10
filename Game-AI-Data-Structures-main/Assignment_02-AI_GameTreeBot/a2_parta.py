#    Main Author(s): Hyeri Jang
#    Main Reviewer(s): Christine Ang, Shu-Ting Hsu


class HashTable:

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice as long as it is a hash table

	def __init__(self, cap=32):
		self.cap = cap
		self.table = [None] * cap
		self.size = 0

	def insert(self,key, value):
		index = hash(key) % self.cap
		while self.table[index] is not None:
			if self.table[index][0] == key:
				return False
			index = (index + 1) % self.cap
		
		self.table[index] = (key, value)
		self.size += 1

		if self.size > 0.7 * self.cap:
			new_capacity = self.cap * 2
			new_table = [None] * new_capacity

			for entry in self.table:
				if entry is not None:
					rehash_key, rehash_value = entry
					new_index = hash(rehash_key) % new_capacity
					while new_table[new_index] is not None:
						new_index = (new_index + 1) % new_capacity
					new_table[new_index] = (rehash_key, rehash_value)

			self.cap = new_capacity
			self.table = new_table
		
		return True

	def modify(self, key, value):
		index = hash(key) % self.cap
		for count in range(self.cap):
			if self.table[index] is None:
				return False
			if self.table[index][0] == key:
				self.table[index] = (key, value)
				return True
			index = (index + 1) % self.cap
		return False

	def remove(self, key):
		index = hash(key) % self.cap
		for count in range(self.cap):
			if self.table[index] is None:
				return False
			if self.table[index][0] == key:
				self.table[index] = (None, None)
				self.size -= 1
				return True
			index = (index + 1) % self.cap
		return False

	def search(self, key):
		index = hash(key) % self.cap
		for count in range(self.cap):
			if self.table[index] is None:
				return None
			if self.table[index][0] == key:
				return self.table[index][1]
			index = (index + 1) % self.cap
		return None

	def capacity(self):
		return self.cap

	def __len__(self):
		return self.size

