#!/usr/bin/env python3
""" redis module """
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    """ Class posses methods which operate a caching system """

    def __init__(self):
        """ Instance method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        """
        Method which takes a data argument, returns a string
        """
        self._key = str(uuid4())
        self._redis.set(self._key, data)
        return self._key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> UnionOfTypes:
        """
        Retrieves data
        """
        value = self._redis.get(key)
        return fn(value) if fn else value

    def get_str(self, value: str) -> str:
        """ getter for string """
        return self.get(self._key, str)

    def get_int(self, value: str) -> int:
        """ getter for int"""
        return self.get(self._key, int)
