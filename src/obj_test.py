import unittest
import obj

class Test(unittest.TestCase):
  def test_obj(self):
    # passthough primitives and unsupported types
    self.assertTrue(obj.to_obj(5) == 5)
    self.assertTrue(obj.to_obj(True) == True)
    self.assertTrue(obj.to_obj("hello") == "hello")
    
    # wrap lists and dics
    self.assertTrue(isinstance(obj.to_obj([]), obj.arr))
    self.assertTrue(isinstance(obj.to_obj({}), obj.obj))

    # wrap nested
    self.assertTrue(isinstance(obj.to_obj({ 'a': {} }).a, obj.obj))
    self.assertTrue(isinstance(obj.to_obj([[]])[0], obj.arr))
    self.assertTrue(isinstance(obj.to_obj({ 'a': {} }).a, obj.obj))
    self.assertTrue(isinstance(obj.to_obj([{}])[0], obj.obj))
    self.assertTrue(isinstance(obj.to_obj({ 'a': []}).a, obj.arr))

    # wrap literal
    self.assertTrue(obj.to_obj({ 'a': 5 })['a'] == 5)
    self.assertTrue(obj.to_obj([{ 'a': 5 }])[0].a == 5)

    # wrap iterators
    [self.assertTrue(isinstance(item, obj.obj)) for item in obj.to_obj([{}, {}, {}])]

    # passthrough assignment
    object = obj.to_obj({ 'a': 1, 'b': 2, 'c': 3 })
    object.d = 4
    self.assertTrue(list(object.values()).pop() == 4)

    # passthrough delete
    del object.d
    self.assertTrue(list(object.values()) == [1,2,3])

    # throw on missing keys
    with self.assertRaises(AttributeError):
      del object.e
    
    # wrap .copy
    array = obj.to_obj([{'x':10}])
    self.assertTrue(isinstance(object.copy(), obj.obj))
    self.assertTrue(isinstance(array.copy(), obj.arr))

    # wrap .fromkeys
    self.assertTrue(isinstance(object.fromkeys(['a', 'b']), obj.obj))

    # wrap .get
    self.assertTrue(isinstance(obj.to_obj({ 'a': {} }).get('a'), obj.obj))

    # wrap .pop
    self.assertTrue(isinstance(obj.to_obj({ 'a': {} }).pop('a'), obj.obj))
    self.assertTrue(isinstance(obj.to_obj([{ 'a': {} }]).pop(), obj.obj))

    # wrap .popitem
    object = obj.to_obj({ 'a': {} })
    (key, value) = object.popitem()
    self.assertTrue(isinstance(value, obj.obj))

unittest.main()