"""
  This module provides a wrapper for dict and list items
  that exposes dict entries as it's attributes

  - Example::
    # import
    from obj import to_obj

    # initialize
    object = to_obj({ 'foo': 'bar' })
    array = to_obj([{ 'baz': 'qux' }])

    # provides accessors
    object.foo

    # provdes deep
    array[0].baz

    # in the iterator
    item.baz for item in array
"""

__version__ = "1.0.0"
__docformat__ = "reStructuredText"


class Obj(dict):
    """
        Wrap `dict` to `Obj`
        Overwrite accessor methods to provide wrapped value
    """

    def __getitem__(self, name):
        return to_obj(super().__getitem__(name))

    def __getattr__(self, name):
        return to_obj(super().__getitem__(name))

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def copy(self):
        return Obj(super().copy())

    def fromkeys(self, value):
        """
            Overwrite built-in `fromkeys` to return a wrapped value
        """
        return Obj(super().fromkeys(value))

    def get(self, value, default=None):
        return to_obj(super().get(value, default))

    def pop(self, value):
        return to_obj(super().pop(value))

    def popitem(self):
        value = super().popitem()
        return (value[0], to_obj(value[1]))


class Arr(list):
    """
        Wrap `list` to `Arr`
        Overwrite accessor methods to provide wrapped value
    """

    def __getitem__(self, index):
        # if isinstance(index, slice):
        #   for item in super().__getitem__(index):
        #     return to_obj(item)
        # else:
        return to_obj(super().__getitem__(index))

    def __iter__(self):
        for value in list.__iter__(self):
            yield to_obj(value)

    def copy(self):
        return to_obj(super().copy())

    def pop(self, value=0):
        return to_obj(super().pop(value))


def to_obj(value):
    """
        Wrap `dict` to `Obj`
        Wrap `list` to `Arr`
        otherwise return original value
    """
    if isinstance(value, dict):
        return Obj(value)
    if isinstance(value, list):
        return Arr(value)
    return value
