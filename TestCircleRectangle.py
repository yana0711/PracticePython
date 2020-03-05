from CircleFromGeometricObject import Circle
from RectangleFromGeometricObject import Rectangle

def main():
    circle = Circle(1.5)
    print("Circle: ", circle)
    print("Area of the Circle is: ", circle.getArea(), ".")
    print("Diameter of the Circle is : ", circle.getDiameter(), ".")
    
    rectangle = Rectangle(2, 4)
    print("\nRectangle: ", rectangle)
    print("Area of the Rectangle is: ", rectangle.getArea(), ".")
    print("Perimeter of the Rectangle is: ", rectangle.getPerimeter(), ".")
    
main()
