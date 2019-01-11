import unittest
import unittest.mock
import students

def last_name_search():
    with students.patch.object(__builtin__, 'input', lambda: 'S: CORONADO'):
        assert students.function() == "CORONADO, DIMPLE, 6, 102, KERBS, BENITO"

def last_name_search_bus():
    with students.patch.object(__builtin__, 'input', lambda: 'S: CORONADO B'):
        assert students.function() == "CORONADO, DIMPLE, 52"
