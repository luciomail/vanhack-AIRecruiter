class MemStore:
	def __init__(self):
		# Counts of feature/category combinations
		self.fc = {}
		# Counts of documents in each category
		self.cc = {}

	# Increase the count of a feature/category pair
	def incf(self, f, cat):
		self.fc.setdefault(f, {})
		self.fc[f].setdefault(cat, 0)
		self.fc[f][cat] += 1

	# Increase the count of a category
	def incc(self, cat):
		self.cc.setdefault(cat, 0)
		self.cc[cat] += 1

	# The number of times a feature has appeared in a category
	def fcount(self, f, cat):
		if f in self.fc and cat in self.fc[f]:
			return float(self.fc[f][cat])

		return 0

	# The number of items in a category
	def catcount(self, cat):
		if cat in self.cc:
			return float(self.cc[cat])

		return 0

	# The total number of items
	def totalcount(self):
		return sum(self.cc.values())

	# The list of all categories
	def categories(self):
		return self.cc.keys()

	@staticmethod
	def flush():
		return
