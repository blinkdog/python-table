# flexi.py
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


class Flexi:
    @classmethod
    def fromkeys(self, sequence, value=None):
        f = Flexi()
        for name in sequence:
            f[name] = value
        return f

    def __contains__(self, item):
        return self.__dict__.__contains__(item)

    def __delitem__(self, key):
        return self.__dict__.__delitem__(key)

    def __getitem__(self, key):
        return self.__dict__.__getitem__(key)

    def __iter__(self):
        return self.__dict__.__iter__()

    def __len__(self):
        return self.__dict__.__len__()

    def __setitem__(self, key, value):
        return self.__dict__.__setitem__(key, value)

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def get(self, key, value=None):
        return self.__dict__.get(key, value)

    def items(self):
        return self.__dict__.items()

    def keys(self):
        return self.__dict__.keys()

    def pop(self, key, value=None):
        return self.__dict__.pop(key, value)

    def popitem(self):
        return self.__dict__.popitem()

    def setdefault(self, key, value):
        return self.__dict__.setdefault(key, value)

    def update(self, obj):
        return self.__dict__.update(obj)

    def values(self):
        return self.__dict__.values()

# ----------------------------------------------------------------------------
# flexi.py
