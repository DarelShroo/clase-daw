# Guía Rápida de Manipulación del DOM en JavaScript

Esta guía proporciona un resumen conciso pero completo de los métodos y conceptos para manipular el **Document Object Model (DOM)** en JavaScript. Incluye métodos para seleccionar, modificar e interactuar con elementos HTML, junto con conceptos clave como `NodeList` vs. `HTMLCollection`, manejo de eventos y navegación por el DOM.

---

## 1. Introducción al DOM
El **DOM (Document Object Model)** es una interfaz de programación que representa la estructura de un documento HTML como un árbol de nodos. Cada elemento HTML, atributo, texto y comentario es un nodo en este árbol, lo que permite a JavaScript interactuar dinámicamente con la página web.

- **`document`**: El objeto raíz que representa el documento HTML.
  - `console.log(document)`: Muestra el documento como un árbol HTML.
  - `console.dir(document)`: Muestra las propiedades del objeto `document` como un objeto JavaScript.

---

## 2. Métodos para Seleccionar Elementos

### `getElementById()`
- **Descripción**: Selecciona un elemento por su atributo `id`.
- **Uso**: `document.getElementById("id")`
- **Retorno**: 
  - Un objeto `HTMLElement` si se encuentra el elemento.
  - `null` si no se encuentra.
- **Ejemplo**:
  ```javascript
  const principalTitle = document.getElementById("principal-title");
  console.dir(principalTitle); // Muestra las propiedades del elemento
  principalTitle.textContent = "Título Actualizado";
  ```

### `getElementsByClassName()`
- **Descripción**: Selecciona elementos por su clase CSS.
- **Uso**: `document.getElementsByClassName("clase")`
- **Retorno**: 
  - Una `HTMLCollection` (colección viva, se actualiza automáticamente).
  - Una `HTMLCollection` vacía `[]` si no hay coincidencias.
- **Nota**: No es directamente iterable con `forEach`. Convertir a array si es necesario.
- **Ejemplo**:
  ```javascript
  const buttons = document.getElementsByClassName("btn");
  Array.from(buttons).forEach((element, index) => {
    element.textContent = `Botón ${index + 1}`;
    element.style.padding = "10px";
  });
  ```

### `getElementsByName()`
- **Descripción**: Selecciona elementos por el valor de su atributo `name`.
- **Uso**: `document.getElementsByName("nombre")`
- **Retorno**: 
  - Una `NodeList` (estática, no se actualiza automáticamente).
  - Una `NodeList` vacía `[]` si no hay coincidencias.
- **Ejemplo**:
  ```javascript
  const inputs = document.getElementsByName("username");
  console.log(inputs); // NodeList con los elementos <input name="username">
  ```

### `getElementsByTagName()`
- **Descripción**: Selecciona elementos por su nombre de etiqueta (e.g., `div`, `p`, `h1`).
- **Uso**: `document.getElementsByTagName("etiqueta")`
- **Retorno**: 
  - Una `HTMLCollection` (viva).
  - Una `HTMLCollection` vacía `[]` si no hay coincidencias.
- **Ejemplo**:
  ```javascript
  const paragraphs = document.getElementsByTagName("p");
  console.log(paragraphs); // HTMLCollection de todos los <p>
  ```

### `querySelector()`
- **Descripción**: Selecciona el **primer elemento** que coincide con un selector CSS.
- **Uso**: `document.querySelector("selectorCSS")`
- **Retorno**: 
  - Un objeto `HTMLElement` si se encuentra.
  - `null` si no hay coincidencias.
- **Ejemplo**:
  ```javascript
  const firstButton = document.querySelector(".container .btn");
  console.log(firstButton); // Primer elemento con clase .btn dentro de .container
  ```

### `querySelectorAll()`
- **Descripción**: Selecciona **todos los elementos** que coinciden con un selector CSS.
- **Uso**: `document.querySelectorAll("selectorCSS")`
- **Retorno**: 
  - Una `NodeList` (estática).
  - Una `NodeList` vacía `[]` si no hay coincidencias.
- **Ejemplo**:
  ```javascript
  const allButtons = document.querySelectorAll(".container .btn");
  allButtons.forEach((btn, index) => {
    btn.textContent = `Botón ${index + 1}`;
  });
  ```

---

## 3. `NodeList` vs. `HTMLCollection`

| **Característica**         | **NodeList**                              | **HTMLCollection**                       |
|----------------------------|-------------------------------------------|------------------------------------------|
| **Definición**             | Colección de nodos del DOM (elementos, texto, comentarios, etc.). | Colección de elementos HTML únicamente. |
| **Métodos de obtención**   | `document.querySelectorAll()`, `.childNodes` | `document.getElementsByTagName()`, `document.getElementsByClassName()` |
| **Tipos de nodos**         | Elementos HTML, nodos de texto, comentarios, etc. | Solo elementos HTML. |
| **Métodos disponibles**    | `item()`, `forEach()`, `entries()`, `keys()`, `values()` | `item()`, `namedItem()` |
| **Acceso por índice**      | Sí                                        | Sí                                       |
| **Iterabilidad**           | Sí (`forEach` nativo)                     | No (requiere conversión a array)         |
| **Actualización en vivo**  | No (estática)                             | Sí (dinámica, refleja cambios en el DOM) |

- **Conversión a Array**:
  - Desestructuración: `[...coleccion]`
  - Usando `Array.from`: `Array.from(coleccion)`
- **Verificar tipo**:
  ```javascript
  const elementos = document.getElementsByClassName("btn");
  console.log(elementos instanceof HTMLCollection); // true
  console.log(elementos.constructor.name); // "HTMLCollection"
  ```

---

## 4. Manipulación de Elementos

### Cambiar Contenido
- **`textContent`**: Cambia el texto de un elemento (ignora etiquetas HTML).
  ```javascript
  const title = document.getElementById("title");
  title.textContent = "Nuevo Título";
  ```
- **`innerHTML`**: Cambia el contenido HTML de un elemento (interpreta etiquetas HTML).
  ```javascript
  title.innerHTML = "<strong>Nuevo Título</strong>";
  ```

### Modificar Atributos
- **`getAttribute("atributo")`**: Obtiene el valor de un atributo.
  ```javascript
  const img = document.querySelector("img");
  console.log(img.getAttribute("src")); // Ruta de la imagen
  ```
- **`setAttribute("atributo", "valor")`**: Establece el valor de un atributo.
  ```javascript
  img.setAttribute("alt", "Descripción de la imagen");
  ```
- **`removeAttribute("atributo")`**: Elimina un atributo.
  ```javascript
  img.removeAttribute("alt");
  ```

### Modificar Estilos
- **`style.propiedad`**: Modifica una propiedad CSS específica.
  ```javascript
  const div = document.querySelector(".box");
  div.style.backgroundColor = "blue";
  div.style.padding = "10px";
  ```
- **`classList`**: Manipula clases CSS.
  - `add("clase")`: Añade una clase.
  - `remove("clase")`: Elimina una clase.
  - `toggle("clase")`: Alterna una clase.
  - `contains("clase")`: Verifica si tiene una clase.
  ```javascript
  div.classList.add("active");
  console.log(div.classList.contains("active")); // true
  ```

### Crear y Añadir Elementos
- **`document.createElement("etiqueta")`**: Crea un nuevo elemento.
- **`appendChild(nodo)`**: Añade un nodo como hijo.
- **`prepend(nodo)`**: Añade un nodo como primer hijo.
- **`removeChild(nodo)`**: Elimina un nodo hijo.
- **Ejemplo**:
  ```javascript
  const newDiv = document.createElement("div");
  newDiv.textContent = "Nuevo elemento";
  document.body.appendChild(newDiv);
  ```

---

## 5. Manejo de Eventos
- **`addEventListener("evento", funcion)`**: Asocia una función a un evento.
- **Eventos comunes**: `click`, `mouseover`, `input`, `submit`, etc.
- **Ejemplo**:
  ```javascript
  const button = document.querySelector(".btn");
  button.addEventListener("click", () => {
    alert("¡Botón clicado!");
  });
  ```
- **`removeEventListener("evento", funcion)`**: Elimina un manejador de eventos.
- **Objeto Event**:
  - `event.target`: Elemento que disparó el evento.
  - `event.preventDefault()`: Evita el comportamiento predeterminado (e.g., envío de formulario).
  ```javascript
  const form = document.querySelector("form");
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    console.log("Formulario enviado");
  });
  ```

---

## 6. Navegación por el DOM
- **Nodos padres e hijos**:
  - `parentElement`: Elemento padre.
  - `children`: `HTMLCollection` de hijos elementos.
  - `childNodes`: `NodeList` de todos los nodos hijos (incluye texto, comentarios).
- **Hermanos**:
  - `nextElementSibling`: Siguiente elemento hermano.
  - `previousElementSibling`: Elemento hermano anterior.
- **Ejemplo**:
  ```javascript
  const element = document.querySelector(".child");
  console.log(element.parentElement); // Padre del elemento
  console.log(element.nextElementSibling); // Siguiente hermano
  ```

---

## 7. Consejos Prácticos
- **Evitar el uso excesivo de `innerHTML`**: Puede ser inseguro con contenido no confiable (riesgo de XSS).
- **Usar `querySelector`/`querySelectorAll` para selectores complejos**: Más flexible que otros métodos.
- **Convertir colecciones a arrays** para usar métodos como `map`, `filter`, etc.
  ```javascript
  const items = document.getElementsByClassName("item");
  const texts = Array.from(items).map(item => item.textContent);
  ```
- **Depuración**:
  - Usa `console.dir(elemento)` para inspeccionar propiedades.
  - Usa `elemento instanceof Tipo` para verificar el tipo de elemento.

---

## 8. Ejemplo Completo
```javascript
// Seleccionar y modificar elementos
const container = document.querySelector(".container");
const buttons = document.querySelectorAll(".btn");

// Cambiar texto y estilos
buttons.forEach((btn, index) => {
  btn.textContent = `Botón ${index + 1}`;
  btn.style.backgroundColor = index % 2 === 0 ? "blue" : "green";
});

// Añadir un nuevo elemento
const newButton = document.createElement("button");
newButton.textContent = "Nuevo Botón";
newButton.classList.add("btn");
container.appendChild(newButton);

// Añadir un evento
newButton.addEventListener("click", () => {
  alert("¡Nuevo botón clicado!");
});
```

---

## 9. Recursos Adicionales
- **Documentación oficial**: [MDN Web Docs - DOM](https://developer.mozilla.org/es/docs/Web/API/Document_Object_Model)
- **Práctica**: Experimenta en la consola de desarrolladores del navegador (F12).
- **Herramientas**: Usa `console.log` y `console.dir` para explorar el DOM.

---

*Última actualización: 21 de septiembre de 2025*