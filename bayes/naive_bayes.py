from bayes.classifier import Classifier


class NaiveBayes(Classifier):
	def __init__(self, tokenizer, store):
		Classifier.__init__(self, tokenizer, store)

	def docprob(self, cat):
		p = 1

		for f in self.tokens:
			p *= self.weightedprob(f, cat, self.fprob)

		return p

	def prob(self, cat):
		docprob = self.docprob(cat)
		catprob = self.store.catcount(cat) / self.store.totalcount()
		return docprob * catprob

	def classify(self, item, default=None):
		probs = {}
		maximum = 0.0
		self.tokens = self.tokenizer.getfeatures(item)

		for cat in self.store.categories():
			probs[cat] = self.prob(cat)

			if probs[cat] > maximum:
				maximum = probs[cat]
				best = cat

		for cat in probs:
			if cat == best:
				continue

			if probs[cat] * self.getthreshold(best) > probs[best]:
				return default

		return best
