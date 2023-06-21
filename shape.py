class Shape(object):
    @classmethod
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @classmethod
    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @classmethod
    def merge_conflict(self):
        return """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis accumsan, erat sit amet maximus sagittis, 
                turpis odio placerat velit, in lobortis dui dolor non nibh."""
