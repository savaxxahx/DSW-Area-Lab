import math #import math module to use pi
import unittest

def circleArea(radius): # no return types and no parameter types
    """ Returns  the area of the circle"""
    return radius*radius*math.pi;

def rectArea(base, height):
    """ Returns the area of the rectangle"""
    return base*height;

def trapArea(base1, base2, height):
    """ Returns the area of the trapezoid"""
    return height * (base1 + base2) / 2;

def triArea(base,height):
    """ Returns the area of the triangle"""
    return base * height / 2;
    
def squareArea(base):
    """Returns the area of the squarew"""
    return base*base;
    
	
class MyTest(unittest.TestCase): # inheriting from unittest.Testcase
    def testCircleArea(self):
        self.assertEqual(circleArea(5),25*math.pi)
    
    def testRectArea(self):
        self.assertEqual(rectArea(2,3),6)
    
    def testTrapArea(self):
        self.assertEqual(trapArea(4,3,2), 7)
    
    def testTriArea(self):
        self.assertEqual(triArea(3,3),4.5)
        self.assertAlmostEqual(triArea(4.2,6.4), 13.44)
       
    def testSquareArea(self):
        self.assertEqual(squareArea(6),36) 