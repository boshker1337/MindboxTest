import unittest
import math
from geometry import Circle, Triangle, calculate_square

class TestGeometry(unittest.TestCase):
    #Класс для тестирования геометрических фигур.
    
    def test_circle_square(self):
        #Тест вычисления площади круга
        r = 5
        circle = Circle(r)
        self.assertAlmostEqual(circle.square(), math.pi * r**2)
        self.assertAlmostEqual(calculate_square(circle), math.pi * r**2)
    
    def test_circle_invalid_radius(self):
        #Тест обработки недопустимого радиуса круга.
        with self.assertRaises(ValueError):
            Circle(-1)  # Отрицательный радиус
        with self.assertRaises(ValueError):
            Circle(0)  # Нулевой радиус
    
    def test_triangle_square(self):
        #Тест вычисления площади треугольника.
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.square(), 6.0)
        self.assertAlmostEqual(calculate_square(triangle), 6.0)
    
    def test_triangle_invalid_sides(self):
        #Тест обработки недопустимых сторон треугольника.
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)  # Невыполнение неравенства треугольника
        with self.assertRaises(ValueError):
            Triangle(0, 1, 1)  # Нулевая сторона
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 2)  # Отрицательная сторона
    
    def test_right_angled_triangle(self):
        #Тест проверки прямоугольного треугольника.
        self.assertTrue(Triangle(3, 4, 5).is_right_angled())
        self.assertFalse(Triangle(3, 4, 6).is_right_angled())

if __name__ == '__main__':
    unittest.main()