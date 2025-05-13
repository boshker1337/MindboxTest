from geometry import Circle, Triangle, calculate_square, Shape

# Создаем круг и вычисляем его площадь
circle = Circle(10)
print(f"Площадь круга: {circle.square()}")
print(f"Через общую функцию: {calculate_square(circle)}")

# Создаем треугольник и проверяем его свойства
triangle = Triangle(3, 4, 5)
print(f"Площадь треугольника: {triangle.square()}")
print(f"Прямоугольный: {triangle.is_right_angled()}")
print(f"Площадь через общую функцию: {calculate_square(triangle)}")

# Пример добавления новой фигуры (прямоугольник)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def square(self):
        return self.width * self.height
    
rect = Rectangle(4, 5)
print(f"Площадь прямоугольника: {calculate_square(rect)}")