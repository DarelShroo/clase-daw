import json
from ingrediente import Ingrediente


def extract_all(atribute = "nombre", path = "./ingredientes_unicos.json"):
  arr_data = []
  with open(path, "r", encoding="utf-8") as f:
      data = json.load(f)
      for product in data:
          ingredient = Ingrediente(**product)
          if atribute == "nombre":
            arr_data.append(ingredient.nombre)
          elif atribute=="unidad":
             arr_data.append(ingredient.unidad)
  return set(arr_data)


print(extract_all())
