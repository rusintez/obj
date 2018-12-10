# pylint: disable=C0103,C0111,E1101

import unittest
import obj


class Test(unittest.TestCase):
    def test_obj(self):
        # passthough primitives and unsupported types
        self.assertEqual(obj.to_obj(5), 5)
        self.assertEqual(obj.to_obj(True), True)
        self.assertEqual(obj.to_obj("hello"), "hello")

        # wrap lists and dics
        self.assertTrue(isinstance(obj.to_obj([]), obj.Arr))
        self.assertTrue(isinstance(obj.to_obj({}), obj.Obj))

        # wrap nested
        self.assertTrue(isinstance(obj.to_obj({'a': {}}).a, obj.Obj))
        self.assertTrue(isinstance(obj.to_obj([[]])[0], obj.Arr))
        self.assertTrue(isinstance(obj.to_obj({'a': {}}).a, obj.Obj))
        self.assertTrue(isinstance(obj.to_obj([{}])[0], obj.Obj))
        self.assertTrue(isinstance(obj.to_obj({'a': []}).a, obj.Arr))

        # wrap literal
        self.assertTrue(obj.to_obj({'a': 5})['a'] == 5)
        self.assertTrue(obj.to_obj([{'a': 5}])[0].a == 5)

        # wrap iterators
        for item in obj.to_obj([{}, {}, {}]):
            self.assertTrue(isinstance(item, obj.Obj))

        # passthrough assignment
        o = obj.to_obj({'a': 1, 'b': 2, 'c': 3})
        o.d_field = 4
        self.assertTrue(list(o.values()).pop() == 4)

        # passthrough delete
        del o.d_field
        self.assertTrue(list(o.values()) == [1, 2, 3])

        # throw on missing keys
        with self.assertRaises(AttributeError):
            del o.e

        # wrap .copy
        array = obj.to_obj([{'x': 10}])
        self.assertTrue(isinstance(o.copy(), obj.Obj))
        self.assertTrue(isinstance(array.copy(), obj.Arr))

        # wrap .fromkeys
        self.assertTrue(isinstance(o.fromkeys(['a', 'b']), obj.Obj))

        # wrap .get
        self.assertTrue(isinstance(obj.to_obj({'a': {}}).get('a'), obj.Obj))

        # wrap .pop
        self.assertTrue(isinstance(obj.to_obj({'a': {}}).pop('a'), obj.Obj))
        self.assertTrue(isinstance(obj.to_obj([{'a': {}}]).pop(), obj.Obj))

        # wrap .popitem
        o = obj.to_obj({'a': {}})
        (key, value) = o.popitem()  # pylint: disable=W0612
        self.assertTrue(isinstance(value, obj.Obj))


unittest.main()
