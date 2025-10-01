"""Escribe una función suma_enteros()
   que pida dos números enteros al usuario
   (con input) y devuelva su suma."""

def pedir_numeros():
    while True:
        try:
            x, y = input("Escribe dos números separados por espacio: ").split()
            return int(x), int(y)
        except ValueError:
            print("Debes escribir dos números enteros válidos.")
        except Exception:
            print("No has seguido las indicaciones, inténtalo otra vez.")

def suma_enteros():
    x, y = pedir_numeros()
    return x + y

print(suma_enteros())

"""Escribe una función es_par(n)
   que devuelva True si el número
   es par y False en caso contrario."""

def es_par(x: int):
  return  "es par" if (x%2 == 0) else "es impar"

print(es_par(5))

"""Escribe una función tabla_multiplicar(n)
que imprima la tabla de multiplicar de n
del 1 al 10."""

def tabla_multiplicar(x: int):
  return [x*j for j in range(1, 11)]

print(tabla_multiplicar(5))

"""Escribe una función estadisticas(lista)
   que devuelva un diccionario con mínimo,
   máximo y media de una lista numérica."""

def estadisticas(x: list[int]):
  return {
    "minimo": min(x),
    "maximo": max(x),
    "media": sum(x)/len(x)
  }

print(estadisticas([1, 20, 5]))

"""Escribe una función contar_palabras(texto)
   que reciba una cadena y devuelva un diccionario
   con la frecuencia de cada palabra."""

def contar_palabras(x: str):
  words = x.split(" ")
  words_dict = {}
  for word in words:
    words_dict[word] = words_dict.get(word, 0) + 1
  return words_dict


print(contar_palabras("gato pato gallina conejo pato gato"))

"""Escribe una función cuadrados(lista)
   que devuelva una nueva lista con los
   cuadrados de los números de la lista
   original."""

def cuadrados(x: list[int]):
  return [y*y for y in x]

print(cuadrados([2, 3, 5]))

"""Escribe una función es_palindromo(cadena)
   que devuelva True si la cadena es un palíndromo
   (se lee igual al derecho y al revés), ignorando
   espacios y mayúsculas."""

def es_palindromo(cadena: str):
  cadena_formateada = cadena.replace(" ", "").lower()
  return cadena_formateada[::-1] == cadena_formateada

print(es_palindromo("ao A"))

"""Escribe una función pares_hasta(n)
   que devuelva una lista con todos
   los números pares desde 0 hasta n."""

def pares_hasta(n: int):
  return [x for x in range(0, n+1) if x%2 == 0]

print(pares_hasta(5))

"""Escribe una función division_segura(a, b)
   que devuelva el resultado de a / b, pero si b
   es 0, devuelva un mensaje de error en lugar
   de lanzar excepción."""

def division_segura(a: int, b: int):
  try:
    if b == 0:
      raise ValueError("No se puede hacer la división forma segura")
    return a/b
  except ValueError as e:
    return e

print(division_segura(5,2))

"""Escribe una función min_max(lista)
que devuelva el mínimo y el máximo de
la lista como una tupla."""

def min_max(x: list[int]):
  return (min(x), max(x))

print(min_max([2,5,6,8,1,5,8,10]))


"""Crea una clase Rectangulo
   con atributos ancho y alto, y un
   método area() que devuelva el área."""

class Rectangulo:
  def __init__(self, ancho: int, alto: int):
    self.ancho = ancho
    self.alto = alto

  def area(self):
    return self.ancho*self.alto


print(Rectangulo(5, 10).area())
