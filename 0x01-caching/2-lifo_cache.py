#!/usr/bin/env python3
""" Create a class FIFOCache that inherits from BaseCaching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Implements a Last-In-First-Out (LIFO) caching strategy.
    """

    def __init__(self):
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Put an item into the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= self.MAX_ITEMS:
                print("DISCARD:", self.last_key)
                del self.cache_data[self.last_key]
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Get an item from the cache by key.
        """
        return self.cache_data.get(key, None)
