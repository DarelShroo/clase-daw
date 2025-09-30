class Ingrediente:
    def __init__(self, nombre, unidad, precio_unidad):
        self.nombre = nombre
        self.unidad = unidad
        self.precio_unidad = precio_unidad

    def __str__(self):
        return f"{self.nombre} ({self.unidad}, {self.precio_unidad}/u"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.nombre, self.unidad, self.precio_unidad))

    def __eq__(self, other):
        if not isinstance(other, Ingrediente):
            return False
        return (self.nombre == other.nombre and
                self.unidad == other.unidad and
                self.precio_unidad == other.precio_unidad)
