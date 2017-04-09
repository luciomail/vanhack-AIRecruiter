import redis


class RedisStoreBayes:
	def __init__(self, host, port, db, p=''):
		self.con = redis.Redis(host=host, port=port, db=db, decode_responses=True)
		self.prefix = p

		if self.con is None:
			raise Exception('Redis error')

	def flush(self):
		self.con.flushdb()

	def incf(self, f, cat):
		self.con.hincrby(self.prefix + '_featureCategoryCount', cat + '__%--%__' + f, 1)

	def fcount(self, f, cat):
		count = self.con.hget(self.prefix + '_featureCategoryCount', cat + '__%--%__' + f)

		if count is None:
			return 0

		return float(count)

	def incc(self, cat):
		self.con.hincrby(self.prefix + '_categoryCount', cat, 1)

	def catcount(self, cat):
		count = self.con.hget(self.prefix + '_categoryCount', cat)

		if count is None:
			return 0

		return float(count)

	def categories(self):
		return self.con.hkeys(self.prefix + '_categoryCount')

	def totalcount(self):
		count = 0
		for catCount in self.con.hvals(self.prefix + '_categoryCount'):
			count += float(catCount)
		return count
