# test_flexi.py
# Copyright 2019 Patrick Meade
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------

from flexi.flexi import Flexi

DICT_CONTENTS = [
    '__class__',
    '__contains__',
    '__delattr__',
    '__delitem__',
    '__dir__',
    '__doc__',
    '__eq__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__getitem__',
    '__gt__',
    '__hash__',
    '__init__',
    '__init_subclass__',
    '__iter__',
    '__le__',
    '__len__',
    '__lt__',
    '__ne__',
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__setitem__',
    '__sizeof__',
    '__str__',
    '__subclasshook__',
    'clear',
    'copy',
    'fromkeys',
    'get',
    'items',
    'keys',
    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'
]

OBJECT_CONTENTS = [
    '__class__',
    '__delattr__',
    '__dir__',
    '__doc__',
    '__eq__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__gt__',
    '__hash__',
    '__init__',
    '__init_subclass__',
    '__le__',
    '__lt__',
    '__ne__',
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__sizeof__',
    '__str__',
    '__subclasshook__'
]

CLASS_CONTENTS = [
    '__dict__',
    '__module__',
    '__weakref__'
]


def test_dict_dir():
    d = dict()
    assert dir(d) == DICT_CONTENTS


def test_object_dir():
    o = object()
    assert dir(o) == OBJECT_CONTENTS


def test_flexi_dir():
    FLEXI_CONTENTS = list(set().union(DICT_CONTENTS, OBJECT_CONTENTS, CLASS_CONTENTS))
    FLEXI_CONTENTS.sort()
    f = Flexi()
    assert dir(f) == FLEXI_CONTENTS


def test_constructor_empty():
    f = Flexi()
    assert len(f) == 0
    assert len(f.keys()) == 0
    assert len(f.values()) == 0


def test_write_subscript_read_dot():
    f = Flexi()
    f["alice"] = 50
    assert f.alice == 50
    assert len(f) == 1
    assert len(f.keys()) == 1
    assert len(f.values()) == 1


def test_write_dot_read_subscript():
    f = Flexi()
    f.alice = 50
    assert f["alice"] == 50
    assert len(f) == 1
    assert len(f.keys()) == 1
    assert len(f.values()) == 1


def test_in_flexi():
    f = Flexi()
    f["alice"] = 10
    f["bob"] = 20
    f["carol"] = 30
    f["dave"] = 40
    assert ("alice" in f)
    assert not ("eve" in f)


def test_over_flexi():
    f = Flexi()
    f["alice"] = 10
    f["bob"] = 20
    f["carol"] = 30
    f["dave"] = 40
    for name in f:
        assert f[name] > 5


def test_delete_from_flexi():
    f = Flexi()
    f["alice"] = 10
    f["bob"] = 20
    f["carol"] = 30
    f["dave"] = 40
    del f["bob"]
    del f.carol
    assert len(f) == 2
    assert ("alice" in f)
    assert ("dave" in f)
    assert not ("bob" in f)
    assert not ("carol" in f)


def test_clear_flexi():
    f = Flexi()
    f["alice"] = 10
    f["bob"] = 20
    f["carol"] = 30
    f["dave"] = 40
    assert len(f) == 4
    assert len(f.keys()) == 4
    assert len(f.values()) == 4
    f.clear()
    assert len(f) == 0
    assert len(f.keys()) == 0
    assert len(f.values()) == 0


def test_copy_flexi():
    f = Flexi()
    f["alice"] = 10
    f["bob"] = 20
    f["carol"] = 30
    f["dave"] = 40
    assert len(f) == 4
    assert len(f.keys()) == 4
    assert len(f.values()) == 4
    x = f.copy()
    assert len(x) == 4
    assert len(x.keys()) == 4
    assert len(x.values()) == 4


def test_write_subscript_read_get():
    f = Flexi()
    f["alice"] = 50
    assert f.get("alice") == 50
    assert len(f) == 1
    assert len(f.keys()) == 1
    assert len(f.values()) == 1


def test_write_dot_read_get():
    f = Flexi()
    f.alice = 50
    assert f.get("alice") == 50
    assert len(f) == 1
    assert len(f.keys()) == 1
    assert len(f.values()) == 1


def test_flexi_items():
    f = Flexi()
    f["alice"] = 10
    f["bob"] = 20
    f["carol"] = 30
    f["dave"] = 40
    assert len(f.items()) == 4


def test_flexi_pop():
    f = Flexi()
    f["alice"] = 10
    result = f.pop("alice")
    assert result == 10
    assert len(f) == 0


def test_flexi_popitem():
    f = Flexi()
    f["alice"] = 10
    f["bob"] = 20
    f["carol"] = 30
    f["dave"] = 40
    p = f.popitem()
    assert len(f.items()) == 3
    assert p == ("dave", 40)


def test_flexi_class_fromkeys():
    f = Flexi.fromkeys(["alice", "bob", "carol", "dave"], 25)
    assert len(f) == 4
    assert f.alice is 25
    assert f.bob is 25
    assert f.carol is 25
    assert f.dave is 25


def test_flexi_instance_fromkeys():
    f = Flexi()
    x = f.fromkeys(["alice", "bob", "carol", "dave"], 25)
    assert len(f) == 0
    assert len(x) == 4
    assert x.alice is 25
    assert x.bob is 25
    assert x.carol is 25
    assert x.dave is 25


def test_flexi_update():
    f = Flexi()
    f["alice"] = 10
    f["bob"] = 20
    f["carol"] = 30
    f["dave"] = 40
    f.update([("alice", 100), ("bob", 200), ("carol", 300), ("dave", 400)])
    assert len(f) == 4
    assert f.alice is 100
    assert f.bob is 200
    assert f.carol == 300
    assert f.dave == 400


def test_flexi_setdefault():
    f = Flexi()
    f["alice"] = 10
    f["bob"] = 20
    f["carol"] = 30
    f["dave"] = 40
    r1 = f.setdefault("alice", 50)
    assert f.alice is 10
    assert r1 == 10
    r2 = f.setdefault("eve", 50)
    assert f.eve is 50
    assert r2 == 50

# ----------------------------------------------------------------------------
# test_flexi.py
