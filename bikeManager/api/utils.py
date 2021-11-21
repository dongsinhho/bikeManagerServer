import redis
import json

rds = redis.StrictRedis(port=6379, db=0)

class Red:
    def getAllKey():
        data = []
        for item in rds.keys():
            item = item.decode()
            data.append(item)
        return data

    def set(cache_key,data):
        data = json.dumps(data)
        rds.set(cache_key,data)

    def get(cache_key):
        cache_data = rds.get(cache_key)
        if not cache_data:
            return None
        cache_data = cache_data.decode()
        #cache_data = json.loads(cache_data)
        return cache_data