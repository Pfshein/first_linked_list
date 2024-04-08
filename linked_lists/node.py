class Node(object):
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	# Get методы
	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	# Set методы
	def set_data(self, data=None):
		self.data = data

	def set_next(self, next=None):
		self.next = next
