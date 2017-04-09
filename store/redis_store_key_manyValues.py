import redis

class RedisStoreKeyManyValues:
	def __init__(self, host, port, db, p=''):
		self.con = redis.Redis(host=host, port=port, db=db, decode_responses=True)
		self.prefix = p

		if self.con is None:
			raise Exception('Redis error')

	def flush(self):
		self.con.flushdb()

	def set(self, key, value):
		self.con.hset(self.prefix + '_key_' + key, value, '1')

	def values(self, key):
		return self.con.hkeys(self.prefix + '_key_' + key)

