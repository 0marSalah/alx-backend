#!/usr/bin/env python3
""" Create a class FIFOCache that inherits from BaseCaching
"""

from collections import deque
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Implements a First-In-First-Out (FIFO) caching strategy.
    # Use a deque to maintain the order of keys
    # Add the new key to the end of the queue
    # Remove the oldest key from the queue
    # Remove the corresponding item from the cache
    """

    def __init__(self):
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ Put an item into the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                oldest_key = self.queue.popleft()
                del self.cache_data[oldest_key]
                print("DISCARD: {}".format(oldest_key))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item from the cache by key.
        """
        return self.cache_data.get(key, None)
