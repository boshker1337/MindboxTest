import math
from abc import ABC, abstractmethod

class Shape(ABC):
    #Абстрактный базовый класс для всех геометрических фигур.
    
    #Определяет обязательные методы, которые должны быть реализованы в дочерних классах конкретных фигур.
    
    @abstractmethod
    def square(self) -> float:
        #Вычисляет площадь фигуры.
        
        #Returns: float: Площадь фигуры
        pass

class Circle(Shape):
    #Класс, представляющий круг.
    
    #Attributes: radius (float): Радиус круга
    
    def __init__(self, radius: float):
        #Инициализирует круг с заданным радиусом.
        
        #Args: radius (float): Радиус круга (должен быть положительным)
            
        #Raises: ValueError: Если радиус не положительный
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius
    
    def square(self) -> float:
        #Вычисляет площадь круга по формуле πr².
        
        #Returns: float: Площадь круга
        return math.pi * self.radius ** 2

class Triangle(Shape):
    #Класс, представляющий треугольник.
    
    #Attributes: a (float): Длина первой стороны 
    #            b (float): Длина второй стороны
    #            c (float): Длина третьей стороны
    
    def __init__(self, a: float, b: float, c: float):
        #Инициализирует треугольник с заданными сторонами.
        
        #Args: a (float): Длина первой стороны
        #      b (float): Длина второй стороны
        #      c (float): Длина третьей стороны
            
        #Raises: ValueError: Если стороны не положительные или не могут образовать треугольник
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("Все стороны должны быть положительными")
        if not self._is_valid_triangle(a, b, c):
            raise ValueError("Невозможно создать треугольник с такими сторонами")
        self.a = a
        self.b = b
        self.c = c
    
    def _is_valid_triangle(self, a: float, b: float, c: float) -> bool:
        #Проверяет, могут ли стороны образовать треугольник (неравенство треугольника).
        
        #Args: a (float): Длина первой стороны
        #      b (float): Длина второй стороны
        #      c (float): Длина третьей стороны
            
        #Returns: bool: True, если стороны могут образовать треугольник, иначе False
        return (a + b > c) and (a + c > b) and (b + c > a)
    
    def square(self) -> float:
        #Вычисляет площадь треугольника по формуле Герона.
        
        #Returns: float: Площадь треугольника
        # Полупериметр
        s = (self.a + self.b + self.c) / 2
        # Формула Герона
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def is_right_angled(self) -> bool:
        #Проверяет, является ли треугольник прямоугольным по теореме Пифагора.
        
        #Returns: bool: True, если треугольник прямоугольный, иначе False
        # Сортируем стороны для нахождения гипотенузы (самой длинной стороны)
        sides = sorted([self.a, self.b, self.c])
        # Проверяем теорему Пифагора с учетом погрешности вычислений
        #a^2 + b^2 = c^2
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

def calculate_square(shape: Shape) -> float:
    #Вычисляет площадь фигуры.
    
    #Args: shape (Shape): Объект геометрической фигуры
        
    #Returns: float: Площадь фигуры
    return shape.square()
