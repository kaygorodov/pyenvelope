import unittest
from pyenvelope import get_minimum_bounding_rectangle


class TestMinimumBoundingRectangle(unittest.TestCase):

    def test(self):
        points = (
            (1, 2),
            (2, 6),
            (3, 7),
            (2, 2)
        )
        mbr = get_minimum_bounding_rectangle(points)

        self.assertEqual(mbr,
                         [
                             (1.9411764705882355, 1.7647058823529418),
                             (3.2352941176470584, 6.9411764705882355),
                             (2.2941176470588234, 7.176470588235294),
                             (1.0000000000000009, 2.0000000000000004),
                             (1.9411764705882355, 1.7647058823529418)
                         ])

if __name__ == '__main__':
    unittest.main()
