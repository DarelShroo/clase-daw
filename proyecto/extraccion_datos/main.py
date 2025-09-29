import pandas as pd
import networkx as nx
from rapidfuzz import fuzz
from itertools import combinations
import unicodedata
import re

# Original product list
productos = [
    "tomate frito","Tomate frito","tomáte frito","tomat frito","tomate fritó",
    "tomatefrito","tomate frit","tomat fríto","tomate fríto","tomato frito",
    "tomate frito","Tomate frito","tomáte frito","tomat frito","tomate fritó",
    "tomatefrito","tomate frit","tomat fríto","tomate fríto","tomato frito",
    "lechuga","Lechuga","lecuga","lechuja","lechúga",
    "lechuga fresca","lechuga verde","lechhuga","lechgua","lechugaa",
    "lechuga","Lechuga","lecuga","lechuja","lechúga",
    "lechuga fresca","lechuga verde","lechhuga","lechgua","lechugaa",
    "papa","Papa","patata","papá","papa fresca",
    "ppa","papa cruda","papaa","papas","papá",
    "papa","Papa","patata","papá","papa fresca",
    "ppa","papa cruda","papaa","papas","papá",
    "zanahoria","Zanahoria","zanahória","zanahoria fresca","zanahorria",
    "zanahoria cruda","zanahoria rallada","zanahoriia","zanahoriaa","zanahoriá",
    "zanahoria","Zanahoria","zanahória","zanahoria fresca","zanahorria",
    "zanahoria cruda","zanahoria rallada","zanahoriia","zanahoriaa","zanahoriá",
    "manzana","Manzana","manzána","manzan","manzana roja",
    "manzana verde","manzzana","manzanaa","manzana fresca","manzanaa",
    "manzana","Manzana","manzána","manzan","manzana roja",
    "manzana verde","manzzana","manzanaa","manzana fresca","manzanaa",
    "pan","Pan","pan fresco","paan","pán",
    "pán fresco","pann","panecillo","pan blanco","pan integral",
    "pan","Pan","pan fresco","paan","pán",
    "pán fresco","pann","panecillo","pan blanco","pan integral",
    "leche","Leche","leché","leche fresca","lehe",
    "leche entera","lech","lecche","lechea","lechéa",
    "leche","Leche","leché","leche fresca","lehe",
    "leche entera","lech","lecche","lechea","lechéa",
    "queso","Queso","queso fresco","quesoo","quesó",
    "queso rallado","queso curado","queso blando","quesa","quesoo",
    "queso","Queso","queso fresco","quesoo","quesó",
    "queso rallado","queso curado","queso blando","quesa","quesoo",
    "arroz","Arroz","arróz","arrozz","aroz",
    "arroz integral","arroz blanco","arroz largo","arroz grano","arrozar",
    "arroz","Arroz","arróz","arrozz","aroz",
    "arroz integral","arroz blanco","arroz largo","arroz grano","arrozar",
    "pollo","Pollo","polló","pollo fresco","pollo crudo",
    "pollo cocido","pollo entero","poyo","poll","pollo",
    "pollo","Pollo","polló","pollo fresco","pollo crudo",
    "pollo cocido","pollo entero","poyo","poll","pollo"
]

# Normalize text: remove extra spaces, normalize accents, fix common typos dynamically
def normalize_text(text):
    text = ' '.join(text.split())  # Remove extra spaces
    # Normalize accents
    text = ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')
    # Fix common typos: remove repeated letters (e.g., "lechhuga" -> "lechuga")
    text = re.sub(r'([a-z])\1+', r'\1', text.lower())
    # Replace common incorrect characters (e.g., 'áa' -> 'á')
    text = re.sub(r'[áàâãä]a', 'á', text)
    text = re.sub(r'[éèêẽë]e', 'é', text)
    text = re.sub(r'[íìîĩï]i', 'í', text)
    text = re.sub(r'[óòôõö]o', 'ó', text)
    text = re.sub(r'[úùûũü]u', 'ú', text)
    # Remove extra vowels at the end (e.g., "lechugaa" -> "lechuga")
    text = re.sub(r'([aeiou])\1+$', r'\1', text)
    return text

# Create a graph with unique nodes, keeping frequency
unique_productos = list(set(productos))
freq = {p: productos.count(p) for p in unique_productos}
G = nx.Graph()
G.add_nodes_from(unique_productos)

# Similarity function
def similitud_final(a, b):
    r1 = fuzz.token_sort_ratio(normalize_text(a), normalize_text(b))
    r2 = fuzz.ratio(normalize_text(a), normalize_text(b))
    return max(r1, r2)

# Similarity threshold to group typos but preserve specific variants
umbral = 80

# Add edges based on similarity
for i, j in combinations(range(len(unique_productos)), 2):
    sim = similitud_final(unique_productos[i], unique_productos[j])
    if sim >= umbral:
        G.add_edge(unique_productos[i], unique_productos[j])

# Find clusters
clusters = list(nx.connected_components(G))

# Canonical name selection
def elegir_canon(cluster):
    # Prioritize: correct spelling (fewer non-standard chars), more words (descriptive),
    # higher frequency, shorter length
    return max(
        cluster,
        key=lambda s: (
            -sum(1 for c in s.lower() if c not in 'abcdefghijklmnopqrstuvwxyzáéíóúüñ '),  # Fewer non-standard chars
            s.count(' '),  # More words (prefer "lechuga fresca" over "lechuga")
            freq[s],  # Higher frequency
            -len(s)  # Shorter length as tiebreaker
        )
    )

# Map each product to its canonical name
canon_map = {}
for cluster in clusters:
    canon = elegir_canon(cluster)
    for nombre in cluster:
        canon_map[nombre] = canon

# Create cleaned product list (unique canonical names)
productos_limpios = sorted(set(canon_map[p] for p in unique_productos))

# Print results
print(f"Total de productos únicos: {len(productos_limpios)}\n")
print("Lista de productos únicos:")
for i, producto in enumerate(productos_limpios, 1):
    print(f"{i}. {producto}")

# Optional: Print clusters for debugging
print("\nClusters para depuración:")
for i, cluster in enumerate(clusters, 1):
    canon = canon_map[next(iter(cluster))]
    print(f"Cluster {i}: {canon} ({len(cluster)} variantes)")
    print(f"  Variantes: {sorted(cluster)}")
