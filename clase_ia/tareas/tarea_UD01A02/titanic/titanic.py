import pandas as pd

# Leer los archivos CSV
try:
    gender_submission = pd.read_csv('gender_submission.csv')
    test = pd.read_csv('test.csv')
    train = pd.read_csv('train.csv')
except FileNotFoundError:
    print("Error: Uno o más archivos CSV no se encuentran en el directorio actual. Verifica las rutas.")
    exit()

# Función para analizar problemas en un DataFrame
def analyze_problems(df, name):
    print(f"\nAnálisis de problemas en {name}:")
    print("\n1. Información general:")
    print(df.info())  # Tipos de datos y nulos
    print("\n2. Valores nulos:")
    print(df.isnull().sum())  # Conteo de nulos por columna
    print("\n3. Duplicados:")
    print(f"Filas duplicadas: {df.duplicated().sum()}")
    print("\n4. Estadísticas descriptivas (numéricas):")
    print(df.describe())  # Para detectar outliers
    print("\n5. Valores únicos en categóricas:")
    for col in df.select_dtypes(include='object').columns:
        print(f"{col}: {df[col].nunique()} valores únicos, ejemplos: {df[col].head(3).tolist()}")

# Analizar cada dataset
analyze_problems(gender_submission, "gender_submission.csv")
analyze_problems(test, "test.csv")
analyze_problems(train, "train.csv")
