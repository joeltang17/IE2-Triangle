import unittest
from isTriangle import Triangle

class TriangleTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def testInvalidSide(self):
        actual = Triangle.classify(0, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testInvalidSide2(self):
        actual = Triangle.classify(1, 2, 4)
        expected = Triangle.Type.INVALID    
        self.assertEqual(actual, expected)

    def testScalene(self):
        actual = Triangle.classify(3, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def testIsosceles(self):
        actual = Triangle.classify(3, 3, 4)
        expected = Triangle.Type.ISOSCELES  
        self.assertEqual(actual, expected)

    def testIsosceles2(self):
        actual = Triangle.classify(3, 4, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testIsosceles3(self):
        actual = Triangle.classify(4, 3, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testInvalidLastSide(self):
        actual = Triangle.classify(3, 3, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
