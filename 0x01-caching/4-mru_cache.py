#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class:
    - inherits from BaseCaching and is a caching system
    - uses a most-recently-used (MRU) algorithm for cache replacement
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """ Add an item in the cache
        - If key or item is None, this method should not do anything.
        - If the number of items in
          self.cache_data is higher than BaseCaching.MAX_ITEMS,
          discard the most recently used item.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key in self.key_order:
            self.key_order.remove(key)
        self.key_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.key_order[-2]
            self.cache_data.pop(mru_key)
            self.key_order.remove(mru_key)
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """ Get an item by key
        - If key is None or if the key doesn’t exist in
          self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.key_order.remove(key)
        self.key_order.append(key)
        return self.cache_data[key]
