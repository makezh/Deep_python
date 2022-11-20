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
        if len(self.cache) >= self.limit and \
                key not in self.order_dict.keys():
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

        # val1 val2 None
        for i in range(1, 4):
            print(f"k{i} = {cache.get('k' + str(i))}")
        print()

        cache.set("k2", "val22")
        cache.set("k2", "val23")
        cache.set("k2", "val24")
        cache.set("k2", "val25")
        cache.set("k1", "val11")
        cache.set("k1", "val12")
        cache.set("k1", "val123")

        # val123 val25 None
        for i in range(1, 4):
            print(f"k{i} = {cache.get('k' + str(i))}")
        print()

        cache.set("k3", "val321")

        # None val25 321
        for i in range(1, 4):
            print(f"k{i} = {cache.get('k' + str(i))}")
        print()

        return "alright, this is main"
    return "just end"


main()
