import unittest
from isTriangle import Triangle

class TriangleTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(1, 1, 1)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def testInvalidSide(self):
        actual = Triangle.classify(10, 0, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testInvalidSide2(self):
        actual = Triangle.classify(1, 2, 5)
        expected = Triangle.Type.INVALID    
        self.assertEqual(actual, expected)

    def testScalene(self):
        actual = Triangle.classify(4, 3, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def testIsosceles(self):
        actual = Triangle.classify(3, 3, 5)
        expected = Triangle.Type.ISOSCELES  
        self.assertEqual(actual, expected)

    def testIsosceles2(self):
        actual = Triangle.classify(3, 5, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testIsosceles3(self):
        actual = Triangle.classify(5, 3, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testInvalidLastSide(self):
        actual = Triangle.classify(4, 4, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
