class Ingrediente:

  def __init__(self, nombre: str, unidad: str, precio_unidad: int, rendimiento: str):
    self.nombre = nombre
    self.unidad = unidad
    self.precio_unidad = precio_unidad
    self.rendimiento = rendimiento

  def __str__(self):
    return f"{self.nombre} ({self.unidad}, {self.precio_unidad}€/u, rendimiento: {self.rendimiento}%)"

  def __repr__(self):
    return f"Ingrediente(nombre={self.nombre!r}, unidad={self.unidad!r}, precio_unidad={self.precio_unidad!r}, rendimiento={self.rendimiento!r})"
