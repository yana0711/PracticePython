from GeometricObject import GeometricObject

class Rectangle(GeometricObject):
    def __init__(self, width=1, height= 1):
        super().__init__()
        self.__width = width
        self.__height = height
        
    def getWidth(self):
        return self.__width
        
    def setWidth(self, width):
        self.__width = width
        
    def getHeight(self):
        return self.__height
        
    def setHeigh(self, height):
        self.__height = height
        
    def getArea(self):
        return self.__height * self.__width
        
    def getPerimeter(self):
        return 2*(self.__height+self.__width)
        
    def __str__(self):
        return super().__str__() + "Width: " + str(self.__width) + \
        "Height: " + str(self.__height)
