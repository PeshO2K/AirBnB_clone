#!/usr/bin/python3
"""
Unittest class for base_model
"""

import os
import unittest
import models
from models import base_model
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
from io import StringIO
import json
import sys

"""
class TestFileStorage(unittest.TestCase):
    \"""All test cases of BaseModel class""\"
    @classmethod
    def setUpClass(cls):
        \"""removing file.json to start from empty""\"
        # reload(base_model)
        stor_path = "file.json"
        with open(stor_path, "w") as f:
            f.write("{}")
        storage.reload()
        if os.path.exists(stor_path):
            os.remove(stor_path)

    @classmethod
    def tearDownClass(cls):
        \"""removing file.json that has been created
        and manipulated in these tests""\"
        stor_path = "file.json"
        if os.path.exists(stor_path):
            os.remove(stor_path)

    def setUp(self):
        \"""creating a BaseModel before each test case""\"
        self.obj = BaseModel()

    def tearDown(self):
        \"""Instructions to do after each test""\"
        stor_path = "file.json"
        with open(stor_path, "w") as f:
            f.write("{}")
        storage.reload()
        if os.path.exists(stor_path):
            os.remove(stor_path)

    def test_attr_types(self):
        \"""testing the type of Filestorage private attributes""\"
        all_objs = storage.all()
        self.assertIsNotNone(all_objs)
        my_dict = {
            f'{self.obj.__class__.__name__}.{self.obj.id}': self.obj}
        self.maxDiff = None
        self.assertEqual(my_dict, all_objs)

    def test_storage_new(self):
        \"""testing addition of a new object to the storage""\"
        obj2 = BaseModel()
        all_objs = storage.all()
        key = f"BaseModel.{obj2.id}"
        self.assertTrue(key in all_objs)

    def test_storage_save_reload(self):
        \"""testing save and reload methods""\"
        storage.save()
        self.assertTrue(os.path.isfile("file.json"))
        all_objs = storage.all()
        expected = {k: v.to_dict() for k, v in all_objs.items()}
        with open("file.json") as f:
            output = json.load(f)
        self.maxDiff = None
        self.assertEqual(output, expected)

    def test_reload_empty_json(self):
        \"""test for trying to reload storage when no json file""\"
        self.assertIsNone(storage.reload())"""
    
class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
    
    """
    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))
    

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)"""
    
    def test_new(self):
        """Yes"""            
        bm = BaseModel()
        us = User()
        """
       st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()"""
        models.storage.new(bm)
        models.storage.new(us)
        """models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)"""
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        """self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())"""
    """
    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)
            """

    def test_save(self):
        bm = BaseModel()
        us = User()
        """st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()"""
        models.storage.new(bm)
        """models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)"""
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            """self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)"""
    
if __name__ == '__main__':
    unittest.main()
