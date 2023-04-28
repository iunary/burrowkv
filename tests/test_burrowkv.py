import unittest
from burrowkv import Burrowkv


class TestBurrow(unittest.TestCase):
    def setUp(self):
        self.store = Burrowkv()

    def test_set_get(self):
        self.store.set("name", "John")
        self.assertEqual(self.store.get("name"), "John")

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.store.get("age"))

    def test_delete(self):
        self.store.set("name", "John")
        self.store.delete("name")
        self.assertIsNone(self.store.get("name"))

    def test_contains(self):
        self.store.set("name", "John")
        self.assertTrue(self.store.contains("name"))
        self.assertFalse(self.store.contains("age"))

    def test_keys(self):
        self.store.set("name", "John")
        self.store.set("age", "30")
        self.assertEqual(self.store.keys(), ["name", "age"])

    def test_values(self):
        self.store.set("name", "John")
        self.store.set("age", "30")
        self.assertEqual(self.store.values(), ["John", "30"])

    def test_items(self):
        self.store.set("name", "John")
        self.store.set("age", "30")
        self.assertEqual(self.store.items(), [("name", "John"), ("age", "30")])

    def test_to_from_json(self):
        self.store.set("name", "John")
        self.store.set("age", "30")

        json_data = self.store.to_json()

        new_store = Burrowkv()
        new_store.from_json(json_data)

        self.assertEqual(new_store.get("name"), "John")
        self.assertEqual(new_store.get("age"), "30")

    def test_clear(self):
        self.store.set("name", "John")
        self.store.clear()

        self.assertEqual(len(self.store), 0)


if __name__ == "__main__":
    unittest.main()
