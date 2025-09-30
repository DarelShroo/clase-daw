import pandas as pd
import networkx as nx
from rapidfuzz import fuzz, process
from itertools import combinations
import unicodedata
import re
from collections import defaultdict
import json
from ingrediente import Ingrediente

# ========== CONFIGURACIÓN MEJORADA ==========
CORRECCIONES = {
    "abdejo": "abadejo",
    "aceitr": "aceite",
    "acido": "ácido",
    "actimel": "actimel",
    "agar agar": "agar agar",
    "agualts": "agua lts",
    "aji": "ají",
    "ajon joli": "ajonjolí",
    "albaricoque": "albaricoque",
    "alcegas": "acelgas",
    "alcochofa": "alcachofa",
    "alemja": "almeja",
    "alginato sodico": "alginato sódico",
    "aljaginato": "alginato",
    "almendra crudasp": "almendra cruda s/p",
    "almendra palillo": "almendra palito",
    "ambrosias": "ambrosías",
    "amapola azul": "amapola azul",
    "anis": "anís",
    "anojo": "añojo",
    "apollinares": "apollinaris",
    "arandanos": "arándanos",
    "arboero": "arbóreo",
    "aroz": "arroz",
    "arrpz": "arroz",
    "articulos": "artículos",
    "atun": "atún",
    "avellana": "avellana",
    "azafran": "azafrán",
    "azucar": "azúcar",
    "glaass": "glasé",
    "babilla": "babilla",
    "bacon": "bacon",
    "banderillas": "banderillas",
    "barritas": "barritas",
    "berberecho": "berberecho",
    "berros": "berros",
    "beterrada": "remolacha",
    "bienex": "bienex",
    "bienmesabe": "bienmesabe",
    "bolleria": "bollería",
    "boqueron": "boquerón",
    "brecol": "brócoli",
    "brocoli": "brócoli",
    "bubango": "bubango",
    "busgado": "búsgado",
    "caballa ahum": "caballa ahumada",
    "caballa cons": "caballa conserva",
    "cabrito": "cabrito",
    "cacahuete": "cacahuete",
    "cafe": "café",
    "calabacin": "calabacín",
    "camaron": "camarón",
    "canonigos": "canónigos",
    "canutillo": "canutillo",
    "carret": "carré",
    "castana": "castaña",
    "cayena": "cayena",
    "cebolletas": "cebolletas",
    "cereeales": "cereales",
    "chalotas": "chalotas",
    "champinon": "champiñón",
    "chistorra": "chistorra",
    "chocolatinas": "chocolatinas",
    "choco": "choco",
    "chopitos": "chopitos",
    "chupito": "chupito",
    "churros": "churros",
    "cilanttro": "cilantro",
    "cloruro calcico": "cloruro cálcico",
    "cochinillo": "cochinillo",
    "coctel": "cóctel",
    "cogollo": "cogollo",
    "coliflor": "coliflor",
    "comino": "comino",
    "conejo": "conejo",
    "congrio": "congrio",
    "cuajada": "cuajada",
    "cuajo": "cuajo",
    "curado curado": "curado",
    "curcuma": "cúrcuma",
    "datiles": "dátiles",
    "decorcrem": "decorcrem",
    "descafeinado": "descafeinado",
    "dextrosa": "dextrosa",
    "dulce": "dulce",
    "edulcorante": "edulcorante",
    "embutido": "embutido",
    "enebro": "enebro",
    "eneldo": "eneldo",
    "escarola": "escarola",
    "esencia": "esencia",
    "esparrago": "espárrago",
    "estragon": "estragón",
    "fettuccini": "fettuccini",
    "fideos": "fideos",
    "filigrana de azucar": "filigrana de azúcar",
    "flores decoracion": "flores decoración",
    "foie gras canapes": "foie gras canapés",
    "frambuesa": "frambuesa",
    "frangollo": "frangollo",
    "fresas": "fresas",
    "fructosa": "fructosa",
    "fuet": "fuet",
    "gamba": "gamba",
    "galletas ecologicas": "galletas ecológicas",
    "garron": "garrón",
    "gel de silice": "gel de sílice",
    "gelatina en laminas": "gelatina en láminas",
    "gelatina fria": "gelatina fría",
    "germinado": "germinado",
    "glucosa": "glucosa",
    "gofio": "gofio",
    "grasa vegetañ¡l": "grasa vegetal",
    "guayabo": "guayabo",
    "guindilla": "guindilla",
    "habas fritas": "habas fritas",
    "harina de maiz": "harina de maíz",
    "hierbas aromaticas": "hierbas aromáticas",
    "higado": "hígado",
    "higos": "higos",
    "hinojos": "hinojos",
    "hojas de azucar": "hojas de azúcar",
    "huesos de jamon": "huesos de jamón",
    "jabali": "jabalí",
    "jamon": "jamón",
    "jareas": "jareas",
    "jengibre": "jengibre",
    "jengobre": "jengibre",
    "judia": "judía",
    "kiwi": "kiwi",
    "laurel": "laurel",
    "lavanda": "lavanda",
    "lechiga": "lechuga",
    "lecitina": "lecitina",
    "lenteja peqeuña": "lenteja pequeña",
    "limon": "limón",
    "lychee": "lychee",
    "macarron": "macarrón",
    "mago": "mango",
    "maiz": "maíz",
    "maltosa": "maltosa",
    "manzana": "manzana",
    "manzanilla sobre": "manzanilla sobre",
    "marron glase": "marrón glacé",
    "mazapan": "mazapán",
    "mejillon": "mejillón",
    "melisa": "melisa",
    "melocoton": "melocotón",
    "menta poleo": "menta poleo",
    "mermel/gelat": "mermelada",
    "mermelada arandano": "mermelada arándano",
    "mermelada dietetica": "mermelada dietética",
    "mermelada hotel porcion": "mermelada hotel porción",
    "mermelada personal porcion": "mermelada personal porción",
    "mezclum": "mezclum",
    "minimazorcas": "mini mazorcas",
    "mojo rojo": "mojo rojo",
    "morilla": "morilla",
    "mostazafuerte": "mostaza fuerte",
    "mozataza": "mostaza",
    "moztaza": "mostaza",
    "nacho": "nacho",
    "names": "names",
    "neranja": "naranja",
    "niños comunion": "niños comunión",
    "niscalo": "níscalo",
    "nisperos": "nísperos",
    "nuez moscada": "nuez moscada",
    "ñoras": "ñoras",
    "oregano": "orégano",
    "orejones de albaricoque": "orejones de albaricoque",
    "paleta ib": "paleta ibérica",
    "pan artezano": "pan artesano",
    "pan bacadillo": "pan baguette",
    "pan chapata": "pan ciabatta",
    "pan grisini": "pan grissini",
    "pan perrp caliente": "pan perro caliente",
    "papa parisien": "papa parisienne",
    "parchita": "parchita",
    "pate": "paté",
    "pavo jamon": "pavo jamón",
    "pepino": "pepino",
    "perejil desidratado": "perejil deshidratado",
    "perlas oro (pasteleria)": "perlas oro (pastelería)",
    "perlas plata (pasteleria)": "perlas plata (pastelería)",
    "picanton": "picantón",
    "pichon": "pichón",
    "pimenton": "pimentón",
    "pimienta mlida": "pimienta molida",
    "pimienta sonbre": "pimienta sobre",
    "pimiento de padron": "pimiento de padrón",
    "pimiento morron": "pimiento morrón",
    "pimiento piquillo": "pimiento piquillo",
    "piña en almibar": "piña en almíbar",
    "piñones": "piñones",
    "piramide chocolate": "pirámide de chocolate",
    "platano": "plátano",
    "polvorones": "polvorones",
    "pota": "pota",
    "praline": "praliné",
    "pularda": "pularda",
    "pure": "puré",
    "queso bri": "queso brie",
    "queso cabre": "queso cabra",
    "queso camberbert": "queso camembert",
    "queso cheedar": "queso cheddar",
    "queso cuarado": "queso curado",
    "queso gorgonsola": "queso gorgonzola",
    "queso gruyere": "queso gruyère",
    "queso idiazabal": "queso idiazábal",
    "queso majorero semi pim": "queso majorero semi pimentón",
    "queso pimenton": "queso pimentón",
    "queso torta casar": "queso torta del casar",
    "rabanito": "rabanito",
    "rabano": "rábano",
    "ravioli": "ravioli",
    "regaliz": "regaliz",
    "requeson": "requesón",
    "riñones-corazon": "riñones-corazón",
    "romero": "romero",
    "rucola": "rúcula",
    "ruibardo": "ruibarbo",
    "sacarina": "sacarina",
    "sake": "sake",
    "salchicha bratwurts": "salchicha bratwurst",
    "salchicha coctel": "salchicha cóctel",
    "salchicha frank": "salchicha frankfurt",
    "salchichon": "salchichón",
    "salmon": "salmón",
    "salsa agrisulce": "salsa agridulce",
    "salsa perryns": "salsa perrins",
    "sama cong": "sama congelado",
    "sandia": "sandía",
    "semola": "sémola",
    "sesamo": "sésamo",
    "solomillo jabali": "solomillo jabalí",
    "sorbete": "sorbete",
    "sumfill": "sumfill",
    "tagliatele": "tagliatelle",
    "tartaleta dulce 39mm": "tartaleta dulce 39 mm",
    "te rojo": "té rojo",
    "te sobre": "té sobre",
    "te verde": "té verde",
    "tempura": "tempura",
    "tila sobre": "tila sobre",
    "tofu": "tofu",
    "tomate ensalda": "tomate ensalada",
    "tomete": "tomate",
    "tomillo": "tomillo",
    "torillas": "tortillas",
    "toronjil": "toronjil",
    "trompeta muerte": "trompeta de la muerte",
    "trufa": "trufa",
    "turron": "turrón",
    "ventresca de atun": "ventresca de atún",
    "vieja fresco": "vieja fresco",
    "vinagre balsamico": "vinagre balsámico",
    "vinagre estragon": "vinagre estragón",
    "vinagre finas hiervas": "vinagre finas hierbas",
    "vinagre miniatura 20 mml": "vinagre miniatura 20 ml",
    "vinagre tinto": "vinagre tinto",
    "viruta lamina": "viruta lámina",
    "wasabi": "wasabi",
    "yogour": "yogur",
    "yuca": "yuca",
    "zanahoriia": "zanahoria",
    "zanahoriaa": "zanahoria",
    "zanahoriá": "zanahoria",
    "refrig.": "refrigerado",
    "congelado.": "congelado",

}

# Sufijos a normalizar
SUFIJOS_NORMALIZAR = {
    "cong": "congelado",
    "frescoc": "fresco",
    "frescoco": "fresco",
    "frescoca": "fresco",
    "congeladoado": "congelado",
    "congeladoada": "congelado",
    "desidratado": "deshidratado",
    "molidoa": "molido",
    "ahumadoa": "ahumado",
    "unid.": "unidad",
    "lts.": "lt",
    "lts" : "lt",
    "manj": "manojo",
    "paq." : "paq",
    "unid": "unidad",
    "und" : "unidad",
    "fresc.": "fresco",
    "congelado.": "congelado",
    "refrig.": "refrigerado",
    "s/h": "sin hueso",
    "s/p": "sin piel",
    "c/p": "con piel",
    "c/h": "con hueso",
    "v gama": "5ª gama",
    "d.o.": "denominación de origen",
    "lt": "lt",
    "cl": "cl",
    "mm": "mm",
    "g": "g",
    "kg": "kg",
    "refrig.": "refrigerado"
}

# Normalización de unidades
NORMALIZACION_UNIDADES = {
    # Peso
    "kg": "kg", "kilo": "kg", "kilogramo": "kg", "kilogramos": "kg",
    "gr": "g", "gramo": "g", "gramos": "g", "g.": "g",
    "mg": "mg", "miligramo": "mg", "miligramos": "mg",

    # Volumen
    "l": "l", "lt": "l", "lts": "l", "litro": "l", "litros": "l", "l.": "l",
    "ml": "ml", "mililitro": "ml", "mililitros": "ml", "ml.": "ml",
    "cl": "cl", "centilitro": "cl", "centilitros": "cl",

    # Unidades
    "unidad": "unidad", "unidades": "unidad", "ud": "unidad", "uds": "unidad",
    "unid": "unidad", "un": "unidad", "u": "unidad", "u.": "unidad",
    "pza": "unidad", "pieza": "unidad", "piezas": "unidad",

    # Paquetes
    "paq": "paquete", "paquete": "paquete", "paquetes": "paquete", "pqt": "paquete",
    "pack": "paquete", "packs": "paquete",

    # Latas
    "lata": "lata", "latas": "lata", "bote": "lata", "botes": "lata",

    # Botellas
    "botella": "botella", "botellas": "botella", "bot": "botella",

    # Sobre
    "sobre": "sobre", "sobres": "sobre", "sob": "sobre",

    # Bolsa
    "bolsa": "bolsa", "bolsas": "bolsa", "bol": "bolsa",

    # Docena
    "docena": "docena", "docenas": "docena", "doc": "docena",

    # Manojo
    "manojo": "manojo", "manojos": "manojo", "mazo": "manojo", "mazos": "manojo",

    # Racimo
    "racimo": "racimo", "racimos": "racimo",

    # Atado
    "atado": "atado", "atados": "atado",

    # Bandera
    "bandeja": "bandeja", "bandejas": "bandeja",

    # Caja
    "caja": "caja", "cajas": "caja", "cj": "caja", "caj": "caja"
}

# Palabras clave para categorización
PALABRAS_CLAVE_CATEGORIAS = {
    "pescado": ["pescado", "salmón", "atún", "merluza", "bacalao", "lubina", "dorada",
                "rape", "rodaballo", "sargo", "pargo", "cherne", "pescadilla", "boquerón",
                "sardina", "caballa", "corvina", "emperador", "pez espada", "trucha",
                "gamba", "langostino", "langosta", "bogavante", "centollo", "nécora",
                "mejillón", "almeja", "ostra", "vieira", "pulpo", "calamar", "sepia",
                "choco", "navaja", "bígaro", "erizo", "cigala", "carabinero", "abadejo",
                "congrio", "merlucilla", "pampano", "morena", "tollos", "alfonsinos",
                "medregal", "vieja", "cabrilla", "lapas", "peto", "bonito", "chicharro"],
    "carne": ["pollo", "ternera", "cerdo", "cordero", "conejo", "pavo", "codorniz",
              "pichón", "faisán", "perdiz", "jabalí", "ciervo", "corzo", "buey",
              "solomillo", "lomo", "chuleta", "costilla", "falda", "cadera", "aguja",
              "entrecot", "filete", "hígado", "riñón", "molleja", "seso", "lengua",
              "rabo", "carne", "muslo", "pechuga", "ala", "pata", "jamón", "panceta",
              "chorizo", "salchicha", "butifarra", "morcilla", "salchichón", "fuet",
              "lacón", "tocino", "beicon", "chopped", "mortadela", "cochinillo",
              "picantón", "gallina", "pularda", "cabrito", "cabra", "añojo", "magret",
              "carrillera", "presa", "secreto", "pluma", "lagrimas", "chuletero"],
    "verdura": ["zanahoria", "cebolla", "pimiento", "tomate", "lechuga", "espinaca",
                "acelga", "col", "coliflor", "brócoli", "alcachofa", "berenjena",
                "calabacín", "calabaza", "pepino", "puerro", "ajo", "cebolleta",
                "espárrago", "judía", "guisante", "haba", "maíz", "patata", "papa",
                "boniato", "batata", "remolacha", "rábano", "nabo", "apio", "endibia",
                "escarola", "canónigo", "rúcula", "berro", "hinojo", "cardo", "rabanito",
                "chalota", "bubango", "col china", "brotes", "germinado", "palmito"],
    "fruta": ["manzana", "pera", "naranja", "mandarina", "limón", "pomelo", "lima",
              "plátano", "fresa", "frambuesa", "mora", "arándano", "grosella",
              "cereza", "uva", "melón", "sandía", "piña", "mango", "papaya",
              "aguacate", "coco", "kiwi", "higo", "dátil", "ciruela", "albaricoque",
              "melocotón", "néctarina", "paraguayo", "breva", "granada",
              "parchita", "guayaba", "lichi", "caqui", "níspero", "parchita"],
    "lacteo": ["queso", "leche", "yogur", "nata", "mantequilla", "margarina",
               "cuajada", "requesón", "quark", "yogur", "actimel", "activvia"],
    "pan": ["pan", "bollo", "baguette", "chapata", "integral", "tostado", "molde",
            "pita", "brioche", "croissant", "galleta", "bizcocho", "magdalena",
            "ciabatta", "pulga", "grissini", "tortilla", "barquillo", "churro"],
    "especia": ["sal", "pimienta", "pimentón", "comino", "canela", "clavo", "nuez moscada",
                "vainilla", "azafrán", "cúrcuma", "curry", "orégano", "tomillo", "romero",
                "albahaca", "perejil", "cilantro", "eneldo", "estragón", "laurel", "menta",
                "hierbabuena", "mostaza", "wasabi", "jengibre", "ajo", "cebolla", "cardamomo",
                "anís", "cilantro", "hierba buena", "melisa", "reina luisa", "toronjil",
                "lavanda", "salvia", "cayena", "guindilla", "ají"]
}

# ========== FUNCIONES MEJORADAS ==========
def normalizar_texto_mejorado(texto):
    """Normalización mejorada del texto con categorización"""
    original = texto.lower().strip()
    texto = original
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto)
                    if unicodedata.category(c) != 'Mn')

    # Paso 1: Correcciones ortográficas
    for error, correccion in CORRECCIONES.items():
        texto = re.sub(r'\b' + re.escape(error) + r'\b', correccion, texto)
        if texto != original and error != texto:
            print(f"Corrección ortográfica: '{original}' -> '{texto}' (reemplazo: {error} -> {correccion})")

    # Paso 2: Normalizar sufijos usando expresiones regulares - CORREGIDO
    for sufijo, normalizado in SUFIJOS_NORMALIZAR.items():
        # Reemplazar sufijo al final de una palabra (delimitado por espacio o fin de cadena)
        pattern = r'\b(\w*?)' + re.escape(sufijo) + r'\b'
        # Usar re.escape en el reemplazo para evitar problemas con números
        nuevo_texto = re.sub(pattern, lambda m: m.group(1) + re.escape(normalizado), texto)
        if nuevo_texto != texto:
            print(f"Normalización de sufijo: '{texto}' -> '{nuevo_texto}' (sufijo: {sufijo} -> {normalizado})")
            texto = nuevo_texto

    # Paso 3: Limpieza final
    texto = re.sub(r'\s+', ' ', texto).strip()
    if texto != original:
        print(f"Normalización final: '{original}' -> '{texto}'")
    return texto

def normalizar_unidad(unidad):
    """Normaliza las unidades de medida"""
    if not unidad:
        return "unidad"

    original = unidad.lower().strip()
    unidad_norm = original

    # Buscar la unidad en el diccionario de normalización
    for unidad_variante, unidad_normalizada in NORMALIZACION_UNIDADES.items():
        if re.search(r'\b' + re.escape(unidad_variante) + r'\b', unidad_norm):
            unidad_norm = unidad_normalizada
            break

    # Si no se encuentra una unidad específica, usar "unidad" por defecto
    if unidad_norm == original and unidad_norm not in NORMALIZACION_UNIDADES.values():
        unidad_norm = "unidad"

    if unidad_norm != original:
        print(f"Normalización de unidad: '{original}' -> '{unidad_norm}'")

    return unidad_norm

def categorizar_ingrediente(nombre):
    """Categoriza un ingrediente basado en palabras clave"""
    nombre_lower = nombre.lower()
    for categoria, palabras_clave in PALABRAS_CLAVE_CATEGORIAS.items():
        for palabra in palabras_clave:
            if palabra in nombre_lower:
                return categoria
    return "otros"

def extraer_raiz_producto(nombre):
    """Extrae la raíz del producto (elimina estados, preparaciones, etc.)"""
    terminos_eliminar = [
        "congelado", "fresco", "fresca", "en conserva", "en almíbar", "en escabeche",
        "deshidratado", "molido", "laminado", "en polvo", "en grano", "entero",
        "filete", "lomo", "entrecot", "chuleta", "muslo", "pechuga", "ala",
        "pelado", "sin piel", "con piel", "limpio", "sin limpiar", "salado",
        "ahumado", "marinado", "adobado", "en aceite", "en vinagre"
    ]
    raiz = nombre.lower()
    for termino in terminos_eliminar:
        raiz = re.sub(r'\s*' + re.escape(termino) + r'\s*', ' ', raiz)
    return re.sub(r'\s+', ' ', raiz).strip()

def calcular_similitud_mejorada(a, b):
    """Calcula similitud mejorada considerando categorías, raíces y precios"""
    raiz_a = extraer_raiz_producto(a.nombre)
    raiz_b = extraer_raiz_producto(b.nombre)
    cat_a = categorizar_ingrediente(a.nombre)
    cat_b = categorizar_ingrediente(b.nombre)

    # Si categorías son diferentes y no son "otros", similitud baja
    if cat_a != cat_b and cat_a != "otros" and cat_b != "otros":
        return 0

    # Normalizar nombres para similitud
    sim_raiz = fuzz.token_sort_ratio(raiz_a, raiz_b)
    sim_completa = fuzz.token_sort_ratio(a.nombre, b.nombre)
    similitud = max(sim_raiz, sim_completa)

    # Penalizar si las unidades son diferentes
    if a.unidad != b.unidad and "unidad" not in a.unidad.lower() and "unidad" not in b.unidad.lower():
        similitud *= 0.8

    # Penalizar si los precios son diferentes
    try:
        precio_a = float(a.precio_unidad.replace('€', '').replace(',', '.').strip())
        precio_b = float(b.precio_unidad.replace('€', '').replace(',', '.').strip())
        if precio_a != precio_b:
            similitud *= 0.5  # Reducir significativamente la similitud si los precios difieren
    except (ValueError, AttributeError):
        pass  # Si no se pueden comparar los precios, no penalizar

    if similitud > 70:
        print(f"Similitud: '{a.nombre}' vs '{b.nombre}'")
        print(f" Raíces: '{raiz_a}' vs '{raiz_b}' -> {sim_raiz}")
        print(f" Categorías: {cat_a} vs {cat_b}")
        print(f" Similitud final: {similitud}")
    return similitud

def elegir_canonico_mejorado(cluster):
    """Elige el nombre canónico más representativo"""
    if not cluster:
        return None
    puntuaciones = []
    for producto in cluster:
        puntuacion = 0
        puntuacion -= len(producto.nombre) * 0.1
        if any(error in producto.nombre.lower() for error in CORRECCIONES.keys()):
            puntuacion -= 50
        if "kg" in producto.unidad.lower() or "unidad" in producto.unidad.lower():
            puntuacion += 10
        categoria = categorizar_ingrediente(producto.nombre)
        if categoria != "otros":
            puntuacion += 20
        puntuaciones.append((puntuacion, producto))
    canon = max(puntuaciones, key=lambda x: x[0])[1]
    print(f"Canónico elegido: '{canon.nombre}'")
    return canon

def verificar_precios_cluster(cluster):
    """Verifica coherencia de precios en un cluster"""
    if len(cluster) <= 1:
        return True
    precios = []
    for producto in cluster:
        try:
            precio_str = producto.precio_unidad.replace('€', '').replace(',', '.').strip()
            if precio_str and precio_str != '/u':
                precio = float(precio_str)
                precios.append(precio)
        except (ValueError, AttributeError):
            continue
    if len(precios) < 2:
        return True
    precio_medio = sum(precios) / len(precios)
    desviaciones = [abs(p - precio_medio) / precio_medio for p in precios]
    if max(desviaciones) > 2.0:
        print(f"⚠️ Posible cluster incorrecto - Precios muy diferentes: {precios}")
        return False
    return True

# ========== PROCESO PRINCIPAL MEJORADO ==========
def procesar_ingredientes_mejorado(ingredientes):
    """Proceso principal mejorado de agrupación"""
    print("=== PROCESO DE AGRUPACIÓN MEJORADO ===")
    print("\n1. Normalizando ingredientes...")
    for ingrediente in ingredientes:
        ingrediente.nombre = normalizar_texto_mejorado(ingrediente.nombre)
        ingrediente.unidad = normalizar_unidad(ingrediente.unidad)

    print("\n2. Creando grafo de similitud...")
    productos_unicos = list(set(ingredientes))
    G = nx.Graph()
    G.add_nodes_from(productos_unicos)

    print("\n3. Calculando similitudes...")
    umbral_similitud = 80
    aristas_agregadas = 0
    for i, j in combinations(range(len(productos_unicos)), 2):
        similitud = calcular_similitud_mejorada(productos_unicos[i], productos_unicos[j])
        if similitud >= umbral_similitud:
            # Solo conectar si los nombres normalizados son idénticos y los precios son iguales
            nombre_norm_i = normalizar_texto_mejorado(productos_unicos[i].nombre)
            nombre_norm_j = normalizar_texto_mejorado(productos_unicos[j].nombre)
            precio_i = productos_unicos[i].precio_unidad
            precio_j = productos_unicos[j].precio_unidad
            if nombre_norm_i == nombre_norm_j and precio_i == precio_j:
                G.add_edge(productos_unicos[i], productos_unicos[j])
                aristas_agregadas += 1

    print(f"Se agregaron {aristas_agregadas} aristas")

    print("\n4. Identificando clusters...")
    clusters = list(nx.connected_components(G))

    print("\n5. Procesando clusters...")
    mapa_canonico = {}
    clusters_finales = []
    productos_eliminados = []  # Array para productos eliminados

    for i, cluster in enumerate(clusters, 1):
        if not verificar_precios_cluster(cluster):
            print(f"Cluster {i} dividido por incoherencia de precios")
            for producto in cluster:
                clusters_finales.append({producto})
                mapa_canonico[producto] = producto
        else:
            canonico = elegir_canonico_mejorado(cluster)
            clusters_finales.append(cluster)
            for producto in cluster:
                mapa_canonico[producto] = canonico
                # Agregar a productos eliminados si no es el canónico
                if producto != canonico:
                    productos_eliminados.append({
                        'producto_original': producto,
                        'reemplazado_por': canonico,
                        'razon': 'duplicado_en_cluster'
                    })

    productos_agrupados = set()
    for cluster in clusters_finales:
        productos_agrupados.update(cluster)
    productos_no_agrupados = set(productos_unicos) - productos_agrupados
    for producto in productos_no_agrupados:
        clusters_finales.append({producto})
        mapa_canonico[producto] = producto

    print(f"\n=== RESULTADOS ===")
    print(f"Total clusters: {len(clusters_finales)}")
    print(f"Productos no agrupados: {len(productos_no_agrupados)}")
    print(f"Productos eliminados (duplicados): {len(productos_eliminados)}")

    # Crear lista de ingredientes únicos para el JSON
    ingredientes_unicos = []
    for producto in sorted(set(mapa_canonico.values()), key=lambda x: x.nombre):
        ingredientes_unicos.append({
            "nombre": producto.nombre.lower(),
            "unidad": producto.unidad.lower(),
            "precio_unidad": producto.precio_unidad,
        })

    # Guardar en JSON
    with open("ingredientes_unicos.json", "w", encoding="utf-8") as f:
        json.dump(ingredientes_unicos, f, ensure_ascii=False, indent=2)

    # Guardar productos eliminados en JSON
    productos_eliminados_json = []
    for eliminado in productos_eliminados:
        productos_eliminados_json.append({
            "nombre_original": eliminado['producto_original'].nombre,
            "unidad_original": eliminado['producto_original'].unidad,
            "precio_original": eliminado['producto_original'].precio_unidad,
            "reemplazado_por": eliminado['reemplazado_por'].nombre,
            "razon": eliminado['razon']
        })

    with open("productos_eliminados.json", "w", encoding="utf-8") as f:
        json.dump(productos_eliminados_json, f, ensure_ascii=False, indent=2)

    return clusters_finales, mapa_canonico, productos_eliminados

# ========== EJECUCIÓN ==========
if __name__ == "__main__":
    print("Leyendo archivo ingredientes.csv...")
    ingredientes = []
    with open("./ingredientes.csv") as file:
        for ingredient_data in file:
            arr_ingredient_data = ingredient_data.strip().split(";")
            nombre = arr_ingredient_data[0]
            unidad = arr_ingredient_data[1]
            precio_unidad = arr_ingredient_data[2]
            ingrediente_obj = Ingrediente(nombre, unidad, precio_unidad)
            ingredientes.append(ingrediente_obj)
    print(f"Se leyeron {len(ingredientes)} productos")

    clusters, mapa_canonico, productos_eliminados = procesar_ingredientes_mejorado(ingredientes)

    print("\n=== CLUSTERS FINALES ===")
    for i, cluster in enumerate(clusters, 1):
        canonico = mapa_canonico[next(iter(cluster))]
        print(f"\nCluster {i}: {canonico.nombre} ({len(cluster)} variantes)")
        print("Variantes:")
        for variante in sorted(cluster, key=lambda x: x.nombre):
            if variante != canonico:
                print(f" - {variante}")

    productos_unicos_finales = set(mapa_canonico.values())
    print(f"\n=== PRODUCTOS ÚNICOS FINALES: {len(productos_unicos_finales)} ===")
    for i, producto in enumerate(sorted(productos_unicos_finales, key=lambda x: x.nombre), 1):
        print(f"{i}. {producto}")

    print(f"\n=== PRODUCTOS ELIMINADOS: {len(productos_eliminados)} ===")
    for i, eliminado in enumerate(productos_eliminados, 1):
        print(f"{i}. '{eliminado['producto_original'].nombre}' -> '{eliminado['reemplazado_por'].nombre}'")
