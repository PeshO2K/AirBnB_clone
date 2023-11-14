#!/usr/bin/python3
"""
Unittest class for base_model
"""

import os
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
import json


class TestFileStorage(unittest.TestCase):
    """All test cases of BaseModel class"""
    @classmethod
    def setUpClass(self):
        stor_path = "file.json"
        """Preserve existing test file.json
        if any"""
        try:
            os.rename(stor_path, "your_json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(self):
        """Delete unit test json and restore previous
        Reset __objects"""
        stor_path = "file.json"
        if os.path.exists(stor_path):
            os.remove(stor_path)

    def setUp(self):
        """creating a BaseModel before each test case"""
        self.obj = BaseModel()

    def tearDown(self):
        """Instructions to do after each test"""
        stor_path = "file.json"
        with open(stor_path, "w") as f:
            f.write("{}")
        storage.reload()
        if os.path.exists(stor_path):
            os.remove(stor_path)

    def test_attr_types(self):
        """testing the type of Filestorage private attributes"""
        all_objs = storage.all()
        self.assertIsNotNone(all_objs)
        my_dict = {
            f'{self.obj.__class__.__name__}.{self.obj.id}': self.obj}
        self.maxDiff = None
        self.assertEqual(my_dict, all_objs)

    def test_storage_new(self):
        """testing addition of a new object to the storage
        In parent and subclass"""
        obj2 = BaseModel()
        obj3 = User()
        # storage.new(obj3)
        all_objs = storage.all()
        # print(all_objs)
        key2 = f"BaseModel.{obj2.id}"
        key3 = f"User.{obj3.id}"
        with self.subTest():
            self.assertTrue(key2 in all_objs)
            # print(key3 in all_objs)
        with self.subTest():
            self.assertIn(key2, all_objs)
            # print(key3 in all_objs)

    def test_storage_save_reload(self):
        """testing save and reload methods
        in parent and subclass"""
        obj2 = User()
        storage.save()
        self.assertTrue(os.path.isfile("file.json"))
        all_objs = storage.all()
        expected = {k: v.to_dict() for k, v in all_objs.items()}
        with open("file.json") as f:
            output = json.load(f)
        self.maxDiff = None
        self.assertEqual(output, expected)

    def test_reload_empty_json(self):
        """test for trying to reload storage when no json file"""
        self.assertIsNone(storage.reload())


if __name__ == '__main__':
    unittest.main()
