from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Cargar dataset y dividir datos (si no lo hiciste antes)
iris = datasets.load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Entrenar clasificador SVC con kernel lineal
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = svm.predict(X_test)

# Calcular métricas
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=target_names)

# Imprimir resultados
print("Accuracy del modelo SVM (kernel lineal):", accuracy)
print("\nMatriz de confusión:")
print(cm)
print("\nClassification Report:")
print(report)

# Visualizar matriz de confusión
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
disp.plot(values_format="d")
plt.title("Matriz de confusión - SVM (kernel lineal)")
plt.show()
