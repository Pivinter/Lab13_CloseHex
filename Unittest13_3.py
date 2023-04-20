import unittest
from Lab13_3_closeTabl import *
class TestNote(unittest.TestCase):
    def test_note_creation(self):
        note = Note("Ivanov", "Ivan", "380123456789", ["01", "01", "1990"])
        self.assertEqual(note.surname, "Ivanov")
        self.assertEqual(note.name, "Ivan")
        self.assertEqual(note.phone_number, "380123456789")
        self.assertEqual(note.birthdate, ["01", "01", "1990"])

class TestClosedHashTable(unittest.TestCase):
    def test_insert_and_search(self):
        hash_table = ClosedHashTable()
        note = Note("Ivanov", "Ivan", "380123456789", ["01", "01", "1990"])
        hash_table.insert(note)
        found_note = hash_table.search("380123456789")
        self.assertIsNotNone(found_note)
        self.assertEqual(found_note.phone_number, "380123456789")

    def test_delete(self):
        hash_table = ClosedHashTable()
        note = Note("Ivanov", "Ivan", "380123456789", ["01", "01", "1990"])
        hash_table.insert(note)
        self.assertTrue(hash_table.delete("380123456789"))
        self.assertIsNone(hash_table.search("380123456789"))

    def test_delete_by_name(self):
        hash_table = ClosedHashTable()
        note = Note("Ivanov", "Ivan", "380123456789", ["01", "01", "1990"])
        hash_table.insert(note)
        self.assertTrue(hash_table.delete_by_name("Ivan"))
        self.assertIsNone(hash_table.search("380123456789"))

    def test_delete_by_birthdate(self):
        hash_table = ClosedHashTable()
        note = Note("Ivanov", "Ivan", "380123456789", ["01", "01", "1990"])
        hash_table.insert(note)
        self.assertTrue(hash_table.delete_by_birthdate(["01", "01", "1990"]))
        self.assertIsNone(hash_table.search("380123456789"))

    def test_search_by_name(self):
        hash_table = ClosedHashTable()
        note1 = Note("Ivanov", "Ivan", "380123456789", ["01", "01", "1990"])
        note2 = Note("Petrov", "Ivan", "380123456788", ["02", "01", "1991"])
        hash_table.insert(note1)
        hash_table.insert(note2)
        found_notes = hash_table.search_by_name("Ivan")
        self.assertEqual(len(found_notes), 2)


if __name__ == "__main__":
    unittest.main()
