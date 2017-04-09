class Classifier:
	def __init__(self, tokenizer, store):
		self.tokenizer = tokenizer
		self.store = store
		self.fc = {}
		self.cc = {}
		self.fw = {}
		self.thresholds = {}
		self.tokens = []

	def setfeaturesweights(self, weights):
		self.fw = weights

	def setthreshold(self, cat, t):
		self.thresholds[cat] = t

	def getthreshold(self, cat):
		if cat not in self.thresholds:
			return 1.0

		return self.thresholds[cat]

	def train(self, item, cat):
		features = self.tokenizer.getfeatures(item)

		for f in features:
			self.store.incf(f, cat)

		self.store.incc(cat)

	def fprob(self, f, cat):
		if self.store.catcount(cat) == 0:
			return 0

		return self.store.fcount(f, cat) / self.store.catcount(cat)

	def weightedprob(self, f, cat, prf, weight=1.0, ap=0.5):
		basicprob = prf(f, cat)
		totals = sum([self.store.fcount(f, c) for c in self.store.categories()])

		for key in self.fw:
			if f.find(key) >= 0:
				weight = self.fw[key]

		bp = ((weight * ap) + (totals * basicprob)) / (weight + totals)
		return bp

	def flush(self):
		self.store.flush()
		return True
