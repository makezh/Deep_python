class LRUCache:
    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}
        self.order_dict = {}
        self.order = 0

    def get(self, key):
        if key in self.cache:
            self.order_dict[key] = self.order
            self.order += 1
            return self.cache[key]
        return None

    def set(self, key, value):
        if len(self.cache) >= self.limit:
            early_key = min(self.order_dict.keys(),
                            key=lambda k: self.order_dict[k])
            self.order_dict.pop(early_key)
            self.cache.pop(early_key)
        self.order_dict[key] = self.order
        self.order += 1
        self.cache[key] = value


def main():
    if __name__ == "__main__":
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        print(cache.get("k3"))  # None
        print(cache.get("k2"))  # "val2"
        print(cache.get("k1"))  # "val1"

        cache.set("k3", "val3")

        print(cache.get("k3"))  # "val3"
        print(cache.get("k2"))  # None
        print(cache.get("k1"))  # "val1"
        return "alright, this is main"
    return "just end"


main()
