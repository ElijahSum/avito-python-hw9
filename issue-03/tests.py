from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_equal(self):
        actual = fit_transform('hello', 'world')
        expected = [
            ('hello', [0, 1]),
            ('world', [1, 0])
        ]
        self.assertEqual(actual, expected)

    def test_not_equal(self):
        actual = fit_transform('world', 'hello')
        expected = [
            ('hello', [0, 1]),
            ('world', [1, 0])
        ]
        self.assertNotEqual(actual, expected)

    def test_not_iterable(self):
        wrong_input = 330
        with self.assertRaises(TypeError):
            fit_transform(wrong_input)

    def test_a_in_b(self):
        a = ('moscow', [0, 1])
        b = fit_transform('moscow', 'new-york')
        self.assertIn(a, b)
