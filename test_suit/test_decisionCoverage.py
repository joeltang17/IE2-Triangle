import unittest
from isTriangle import Triangle

class TriangleTest(unittest.TestCase):
    def test1(self): #reaches triangle type equilateral
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def testInvalidSide(self): #reaches first invalid statement from side being <= 0
        actual = Triangle.classify(0, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testInvalidSide2(self): #reaches second invalid statement from sum of two sides being less than the third
        actual = Triangle.classify(1, 2, 4)
        expected = Triangle.Type.INVALID    
        self.assertEqual(actual, expected)

    def testScalene(self): #reaches triangle type scalene
        actual = Triangle.classify(3, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def testIsosceles(self): #reaches first isoceles statement (a == b )
        actual = Triangle.classify(3, 3, 4)
        expected = Triangle.Type.ISOSCELES  
        self.assertEqual(actual, expected)

    def testIsosceles2(self): #reaches second isoceles statement (b == c)
        actual = Triangle.classify(3, 4, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testIsosceles3(self): #reaches third isoceles statement (a == c)
        actual = Triangle.classify(4, 3, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testInvalidLastSide(self): #reaches last invalid statement from sum of two equal sides being less than the third
        actual = Triangle.classify(3, 3, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
