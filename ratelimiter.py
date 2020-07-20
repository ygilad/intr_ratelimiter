from hashlib import md5


class RateLimiter:
    def __init__(self, threshold, ttl):
        self._threshold = threshold
        self._ttl = ttl
        self._limiter_map = {}

    def get_params(self):
        return {'threshold': self._threshold, 'ttl': self._ttl}


class RateLimitKey:
    def __init__(self, url):
        self._url = url

    def _stringify_key(self):
        return self._url

    def hashed_key(self):
        hash_object = md5(self._stringify_key().encode())
        return hash_object.hexdigest()
