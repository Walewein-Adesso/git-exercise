class Shape(object):
    @classmethod
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @classmethod
    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

