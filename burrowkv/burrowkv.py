"""Burrowkv key value store implementation in python
"""
import threading
import json
from collections import defaultdict
from contextlib import contextmanager
from typing import Optional, List, Tuple


class Burrowkv:
    """
    A simple key-value store implemented using a dictionary.
    """

    def __init__(self):
        """
        Initialize an empty key-value store.
        """
        self.__store = defaultdict(lambda: None)
        self.__lock = threading.Lock()

    def set(self, key: str, value: str) -> None:
        """
        Set a value for the given key.

        Args:
            key (str): The key to set.
            value (str): The value to associate with the key.

        Example:
            >>> store = KeyValueStore()
            >>> store.set('name', 'John')
        """
        with self.__lock:
            self.__store[key] = value

    def get(self, key: str) -> Optional[str]:
        """
        Retrieve the value associated with the given key.

        Args:
            key (str): The key to retrieve.

        Returns:
            The value associated with the key, or None
            if the key does not exist.

        Example:
            >>> store = KeyValueStore()
            >>> store.set('name', 'John')
            >>> store.get('name')
            'John'
            >>> store.get('age')
        """
        with self.__lock:
            return self.__store[key]

    def delete(self, key: str) -> None:
        """
        Delete the key-value pair for the given key.

        Args:
            key (str): The key to delete.
        """
        with self.__lock:
            del self.__store[key]

    def contains(self, key: str) -> bool:
        """
        Check if the key exists in the store.

        Args:
            key (str): The key to check.

        Returns:
            bool: True if the key exists, False otherwise.

        Example:
            >>> store = KeyValueStore()
            >>> store.set('name', 'John')
            >>> store.contains('name')
            True
            >>> store.contains('age')
            False
        """
        return key in self.__store

    def keys(self) -> List[str]:
        """
        Get a list of all keys in the store.

        Returns:
            list: A list of keys.

        Example:
            >>> store = KeyValueStore()
            >>> store.set('name', 'John')
            >>> store.keys()
            ['name']
        """
        return list(self.__store.keys())

    def values(self) -> List[str]:
        """
        Get a list of all values in the store.

        Returns:
            list: A list of values.

        Example:
            >>> store = KeyValueStore()
            >>> store.set('name', 'John')
            >>> store.values()
            ['John']
        """
        return list(self.__store.values())

    def items(self) -> List[Tuple[str, str]]:
        """
        Get a list of all key-value pairs in the store.

        Returns:
            list: A list of (key, value) tuples.

        Example:
            >>> store = KeyValueStore()
            >>> store.set('name', 'John')
            >>> store.items()
            [('name', 'John')]
        """
        return list(self.__store.items())

    def to_json(self) -> str:
        """
        Serialize the key-value store to JSON.

        Returns:
            str: The JSON representation of the key-value store.
        """
        json_data = json.dumps(dict(self.__store))
        return json_data

    def from_json(self, json_data: str) -> None:
        """
        Populate the key-value store from a JSON string.

        Args:
            json_str: The JSON string representing the key-value store.

        Returns:
            None
        """
        with self.__lock:
            self.__store = defaultdict(lambda: None, json.loads(json_data))

    @contextmanager
    def transaction(self):
        """
        Create a transaction context for
        performing multiple operations on the store.

        Example:
        >>> store = KeyValueStore()
        >>> with store.transaction():
        ...     store.set('name', 'John')
        ...     store.set('age', 30)
        >>> store.get('name')
        >>> store.get('age')
        """
        try:
            yield
        finally:
            self.__store.clear()

    def clear(self):
        """
        Clear the data store

        Returns:
            None
        """
        with self.__lock:
            self.__store.clear()

    def __len__(self) -> int:
        """
        Return the number of key-value pairs in the store.

        Returns:
            int: The number of key-value pairs.
        """
        return len(self.__store)
