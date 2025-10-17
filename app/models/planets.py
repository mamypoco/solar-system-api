class Planets:
    def __init__(self, id, name, description, size):
        self.id = id 
        self.name = name 
        self.description = description
        self.size = size


planets = [
    Planets(1, "Mars", "dusty", "medium"),
    Planets(2, "Jupiter", "1000 times the size of earth", "large"),
    Planets(3, "Mercury", "closest to Sun", "large"),
    Planets(4, "Uranus", "cold", "small")
] 