from linked_lists.node import Node


class LinkedList:
	def __init__(self) -> None:
		self.head = None

	def insert_at_end(self, data):
		new_node = Node(data)
		cur_node = self.head
		if cur_node is None:
			self.head = new_node
			return
		while cur_node.get_next() is not None:
			cur_node = cur_node.get_next()
		cur_node.set_next(new_node)

	def insert_at_head(self, data):
		new_node = Node(data)
		cur_node = self.head
		new_node.set_next(cur_node)
		self.head = new_node

	def is_empty(self) -> bool:
		return not self.head

	def delete_at_head(self):
		cur_node = self.head
		self.head = cur_node.get_next()

	def search(self, data):
		cur_node = self.head
		search_node = Node(data)
		counter = 0
		while cur_node is not None:
			if cur_node.get_data() == search_node.get_data():
				counter += 1
			cur_node = cur_node.get_next()
		return print(counter > 0)

	def delete(self, data):
		cur_node = self.head
		search_node = Node(data)
		while cur_node is not None:
			if cur_node.get_data() == search_node.get_data():
				cur_node = cur_node.get_next()
			if cur_node is not None:
				cur_node = cur_node.get_next()

	def show(self):
		cur_node = self.head
		output = ""
		while cur_node is not None:
			output += str(cur_node.get_data()) + " -> "
			cur_node = cur_node.get_next()
		print(output)
