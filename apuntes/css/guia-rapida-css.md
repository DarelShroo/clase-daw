# Guía Rápida de CSS - Basada en el código proporcionado

Esta es una guía de referencia rápida que resume las propiedades CSS utilizadas en el código proporcionado, con explicaciones claras de cada propiedad y sus valores posibles, incluyendo todos los valores de propiedades como `display`, en español.

## 1. **Propiedades de Color**

### `color`
- **Descripción**: Define el color del texto (color de primer plano) de un elemento.
- **Valores utilizados**:
  - Colores nombrados: `blue`, `red`, `white`, `pink`, `purple`, `whitesmoke`, `yellow`.
  - Hexadecimal: `#09f` (abreviatura de `#0099ff`).
  - OKLCH: `oklch(10% 0.148 238.24)` (espacio de color moderno, perceptivamente uniforme).
- **Valores posibles**:
  - Colores nombrados: Cualquier nombre de color válido (ej., `black`, `green`).
  - Hexadecimal: `#RRGGBB` o `#RGB` (ej., `#ffffff`, `#000`).
  - RGB: `rgb(0, 0, 0)` (valores de rojo, verde, azul de 0-255).
  - RGBA: `rgba(0, 0, 0, 0.5)` (RGB con opacidad; formato antiguo).
  - RGB moderno: `rgb(0 0 0 / 50%)` (recomendado).
  - HSL: `hsl(matiz, saturación%, luminosidad%)` (matiz en grados, saturación/luminosidad en %).
  - OKLCH: `oklch(luminosidad% croma matiz)` (luminosidad y croma en %, matiz en grados).
  - `transparent`: Color completamente transparente.
  - `currentColor`: Usa el valor de `color` del elemento o su padre.
  - `inherit`: Hereda el color del elemento padre.
  - `initial`: Restablece al valor predeterminado (generalmente negro).
  - `unset`: Restablece al valor heredado o inicial.
  - `revert`: Revierte al valor del navegador o de la cascada.
- **Ejemplo**:
```css
h1 { color: blue; }
.link { color: red; }
article + p { color: oklch(10% 0.148 238.24); }
```

### `background-color`
- **Descripción**: Establece el color de fondo de un elemento.
- **Valores utilizados**:
  - Hexadecimal: `#774561`, `#09f`, `#000`.
  - Colores nombrados: `wheat`, `red`, `yellow`, `blue`.
- **Valores posibles**: Igual que `color` (nombres, hexadecimal, RGB, RGBA, HSL, OKLCH, `transparent`, etc.).
- **Ejemplo**:
```css
body { background-color: #774561; }
#show { background-color: #09f; }
.container { background-color: red; }
```

## 2. **Tipografía**

### `font-family`
- **Descripción**: Especifica la pila de fuentes para el texto.
- **Valores utilizados**:
  - Fuentes del sistema: `system-ui`, `-apple-system`, `BlinkMacSystemFont`.
  - Fuentes específicas: `Segoe UI`, `Roboto`, `Oxygen`, `Ubuntu`, `Cantarell`, `Open Sans`, `Helvetica Neue`.
  - Familia genérica: `sans-serif`.
- **Valores posibles**:
  - Nombres de fuentes: Fuentes específicas (ej., `Arial`, `Times New Roman`).
  - Familias genéricas: `sans-serif`, `serif`, `monospace`, `cursive`, `fantasy`.
  - Fuentes del sistema: Para usar fuentes nativas del sistema operativo.
  - Lista separada por comas: Fuentes de respaldo en orden de preferencia.
- **Ejemplo**:
```css
body { font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; }
```

### `font-size`
- **Descripción**: Define el tamaño de la fuente del texto.
- **Valores utilizados**: `100px`.
- **Valores posibles**:
  - Longitud: `px`, `rem`, `em`, `%`, etc.
  - Palabras clave: `small`, `medium`, `large`, `larger`, `smaller`.
  - `inherit`: Hereda del padre.
  - `initial`: Restablece al valor predeterminado (generalmente `16px`).
  - `unset`: Restablece al valor heredado o inicial.
  - `revert`: Revierte al valor del navegador o de la cascada.
- **Ejemplo**:
```css
.block { font-size: 100px; }
```

## 3. **Modelo de Caja**

### `border`
- **Descripción**: Propiedad abreviada para `border-width`, `border-style` y `border-color`.
- **Valores utilizados**:
  - `border-width`: `0`, `1px`, `4px`, `5px`.
  - `border-style`: `solid`.
  - `border-color`: `red`, `yellow`, `#000`.
- **Valores posibles**:
  - `border-width`: Longitud (ej., `1px`, `3px`) o palabras clave (`thin`, `medium`, `thick`).
  - `border-style`: `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`, `inset`, `outset`, `none`, `hidden`.
  - `border-color`: Igual que `color`.
  - `initial`: Restablece al valor predeterminado (sin borde).
  - `inherit`: Hereda del elemento padre.
  - `unset`: Restablece al valor heredado o inicial.
  - `revert`: Revierte al valor del navegador o de la cascada.
- **Ejemplo**:
```css
.description { border: 1px solid red; }
#show { border: 0; }
.section-container-2 { border: 5px solid #000; }
```

### `outline`
- **Descripción**: Similar a `border`, pero no afecta el diseño (se dibuja fuera del elemento).
- **Valores utilizados**:
  - `outline-width`: `10px`.
  - `outline-style`: `solid`.
  - `outline-color`: `red`, `blue`.
- **Valores posibles**: Igual que `border` (ancho, estilo, color).
- **Ejemplo**:
```css
.link:hover { outline: 10px solid red; }
.link:active { outline: 10px solid blue; }
```

### `margin`
- **Descripción**: Define el espaciado exterior alrededor de un elemento.
- **Valores utilizados**:
  - `0` (para eliminar márgenes predeterminados).
  - `10px`.
  - `auto` (para centrar elementos horizontalmente).
- **Valores posibles**:
  - Longitud: `px`, `rem`, `em`, `%`, etc.
  - Abreviatura: `margin: arriba derecha abajo izquierda;` o `margin: arriba/abajo derecha/izquierda;`.
  - `auto`: Centra elementos horizontalmente (en bloques con ancho definido).
- **Ejemplo**:
```css
body { margin: 0; }
.container { margin: 10px; }
.container-2 { margin: auto; }
```

### `padding`
- **Descripción**: Define el espaciado interior dentro de un elemento.
- **Valores utilizados**: `10px`.
- **Valores posibles**:
  - Longitud: `px`, `rem`, `em`, `%`, etc.
  - Abreviatura: `padding: arriba derecha abajo izquierda;` o `padding: arriba/abajo derecha/izquierda;`.
- **Ejemplo**:
```css
.container { padding: 10px; }
```

### `box-sizing`
- **Descripción**: Define cómo se calculan `width` y `height`.
- **Valores utilizados**: `border-box`.
- **Valores posibles**:
  - `content-box`: El ancho/alto incluye solo el contenido (predeterminado).
  - `border-box`: El ancho/alto incluye contenido, relleno y borde.
  - `inherit`: Hereda del padre.
- **Ejemplo**:
```css
.container { box-sizing: border-box; }
.section-container-2 { box-sizing: border-box; }
```

### `box-shadow`
- **Descripción**: Añade una sombra al elemento.
- **Valores utilizados**: `0 0 5px #000` (desplazamiento horizontal, vertical, desenfoque, color).
- **Valores posibles**:
  - Formato: `desplazamiento-x desplazamiento-y desenfoque extensión color`.
  - `inset`: Sombra interior (no utilizada aquí).
  - Colores: Igual que `color`.
  - `none`: Sin sombra.
- **Ejemplo**:
```css
.container-2 { box-shadow: 0 0 5px #000; }
```

### `opacity`
- **Descripción**: Define la transparencia de un elemento.
- **Valores utilizados**: `0.9` (90% de opacidad).
- **Valores posibles**:
  - Número entre `0` (transparente) y `1` (opaco).
  - `inherit`: Hereda del padre.
  - `initial`: Restablece al valor predeterminado (`1`).
  - `unset`: Restablece al valor heredado o inicial.
- **Ejemplo**:
```css
.item { opacity: 0.9; }
```

## 4. **Diseño**

### `width` y `height`
- **Descripción**: Establece las dimensiones de un elemento.
- **Valores utilizados**:
  - `width`: `250px`, `100px`, `50px`.
  - `height`: `250px`, `100px`, `50px`, `25px`, `100vh` (altura de la ventana gráfica).
- **Valores posibles**:
  - Longitud: `px`, `rem`, `em`, `%`, etc.
  - Unidades de ventana gráfica: `vh`, `vw`, `vmin`, `vmax`.
  - `auto`: Determinado por el contenido o el diseño.
  - Nota: `height` en porcentaje requiere un padre con altura explícita.
- **Ejemplo**:
```css
body { height: 100vh; }
.container { width: 250px; height: 250px; }
.box { width: 100px; height: 50px; }
```

### `display`
- **Descripción**: Controla cómo se representa un elemento en el diseño.
- **Valores utilizados**:
  - `block`: Ocupa todo el ancho, comienza en una nueva línea.
  - `flex`: Habilita el diseño Flexbox para los hijos.
- **Valores posibles**:
  - `block`: Ocupa todo el ancho, nueva línea (ej., `div`, `p`).
  - `inline`: Ocupa solo el ancho del contenido, permanece en la línea (ej., `span`, `a`).
  - `inline-block`: Inline, pero respeta `width` y `height`.
  - `none`: Oculta el elemento (no reserva espacio).
  - `flex`: Habilita Flexbox.
  - `grid`: Habilita CSS Grid.
  - `inline-flex`: Contenedor Flexbox en línea.
  - `inline-grid`: Contenedor Grid en línea.
  - `table`: Simula un diseño de tabla.
  - `inline-table`: Diseño de tabla en línea.
  - `list-item`: Se comporta como un elemento de lista (ej., `li`).
  - `contents`: El elemento desaparece, pero sus hijos permanecen.
  - `inherit`: Hereda del padre.
  - `initial`: Restablece al valor predeterminado (generalmente `inline`).
  - `unset`: Restablece al valor heredado o inicial.
  - `revert`: Revierte al valor del navegador o de la cascada.
- **Ejemplo**:
```css
.box { display: block; }
.parent { display: flex; }
```

### `position`
- **Descripción**: Define el método de posicionamiento de un elemento.
- **Valores utilizados**: `absolute`.
- **Valores posibles**:
  - `static`: Posición predeterminada (sigue el flujo normal).
  - `relative`: Relativo a su posición normal, permite ajustes con `top`, `right`, etc.
  - `absolute`: Relativo al ancestro posicionado más cercano o al documento.
  - `fixed`: Relativo a la ventana gráfica, permanece fijo al hacer scroll.
  - `sticky`: Alterna entre `relative` y `fixed` según el scroll.
  - `inherit`: Hereda del padre.
  - `initial`: Restablece a `static`.
  - `unset`: Restablece al valor heredado o inicial.
- **Ejemplo**:
```css
.container-2 { position: absolute; }
```

### `inset`
- **Descripción**: Propiedad abreviada para `top`, `right`, `bottom`, `left`.
- **Valores utilizados**: `0` (coloca el elemento en todas las esquinas del contenedor padre).
- **Valores posibles**:
  - Longitud: `px`, `rem`, `em`, `%`, etc.
  - `auto`: Valor predeterminado.
  - Abreviatura: `inset: top right bottom left;` o `inset: top/bottom right/left;`.
- **Ejemplo**:
```css
.container-2 { inset: 0; }
```

### `overflow`
- **Descripción**: Controla qué sucede con el contenido que desborda el contenedor.
- **Valores utilizados**: `auto` (agrega barras de desplazamiento si es necesario).
- **Valores posibles**:
  - `visible`: Contenido desbordado es visible (predeterminado).
  - `hidden`: Contenido desbordado se oculta.
  - `scroll`: Siempre muestra barras de desplazamiento.
  - `auto`: Muestra barras de desplazamiento solo si es necesario.
  - `inherit`: Hereda del padre.
  - `initial`: Restablece a `visible`.
  - `unset`: Restablece al valor heredado o inicial.
- **Ejemplo**:
```css
.container { overflow: auto; }
```

### `text-overflow`
- **Descripción**: Define cómo se muestra el texto desbordado.
- **Valores utilizados**: `'>'` (cadena personalizada para indicar desbordamiento).
- **Valores posibles**:
  - `clip`: Corta el texto desbordado.
  - `ellipsis`: Muestra puntos suspensivos (`…`) para texto desbordado.
  - Cadena: Una cadena personalizada (como `>`).
  - `inherit`: Hereda del padre.
  - `initial`: Restablece a `clip`.
  - `unset`: Restablece al valor heredado o inicial.
- **Ejemplo**:
```css
.container { text-overflow: '>'; }
```

## 5. **Flexbox**

### `flex-flow`
- **Descripción**: Propiedad abreviada para `flex-direction` y `flex-wrap`.
- **Valores utilizados**: `row wrap` (elementos en fila, permite envoltura).
- **Valores posibles**:
  - Combinación de `flex-direction` y `flex-wrap`.
  - `inherit`, `initial`, `unset`, `revert`.
- **Ejemplo**:
```css
.parent { flex-flow: row wrap; }
```

### `flex-direction`
- **Descripción**: Define la dirección de los elementos en un contenedor Flexbox.
- **Valores utilizados**: `row` (elementos en fila, de izquierda a derecha).
- **Valores posibles**:
  - `row`: Fila (de izquierda a derecha).
  - `row-reverse`: Fila inversa (de derecha a izquierda).
  - `column`: Columna (de arriba a abajo).
  - `column-reverse`: Columna inversa (de abajo a arriba).
  - `inherit`, `initial`, `unset`, `revert`.
- **Ejemplo**:
```css
.parent { flex-direction: row; }
```

### `justify-content`
- **Descripción**: Alinea los elementos a lo largo del eje principal del contenedor Flexbox.
- **Valores utilizados**: `center` (centra los elementos).
- **Valores posibles**:
  - `flex-start`: Alinea al inicio.
  - `flex-end`: Alinea al final.
  - `center`: Centra los elementos.
  - `space-between`: Distribuye con espacio entre elementos.
  - `space-around`: Distribuye con espacio alrededor de los elementos.
  - `space-evenly`: Distribuye con espacio igual entre y alrededor de los elementos.
  - `inherit`, `initial`, `unset`, `revert`.
- **Ejemplo**:
```css
.parent { justify-content: center; }
```

### `align-items`
- **Descripción**: Alinea los elementos a lo largo del eje transversal del contenedor Flexbox.
- **Valores utilizados**: `center` (centra los elementos verticalmente).
- **Valores posibles**:
  - `flex-start`: Alinea al inicio.
  - `flex-end`: Alinea al final.
  - `center`: Centra los elementos.
  - `baseline`: Alinea según la línea base del texto.
  - `stretch`: Estira los elementos para llenar el contenedor.
  - `inherit`, `initial`, `unset`, `revert`.
- **Ejemplo**:
```css
.parent { align-items: center; }
```

### `gap`
- **Descripción**: Define el espacio entre los elementos hijos en un contenedor Flexbox o Grid.
- **Valores utilizados**: `10px`.
- **Valores posibles**:
  - Longitud: `px`, `rem`, `em`, etc.
  - `inherit`, `initial`, `unset`, `revert`.
- **Ejemplo**:
```css
.parent { gap: 10px; }
```

## 6. **Pseudo-Clases**

- **Descripción**: Aplica estilos según la interacción del usuario o el estado del elemento.
- **Valores utilizados**:
  - `:hover`: Estilos al pasar el ratón.
  - `:active`: Estilos al hacer clic.
  - `:focus`: Estilos cuando un elemento tiene el foco (ej., input).
  - `:first-child`: Selecciona el primer hijo de un padre.
  - `:last-child`: Selecciona el último hijo de un padre.
  - `:nth-child(2)`: Selecciona el segundo hijo.
- **Ejemplo**:
```css
.link:hover { outline: 10px solid red; }
.link:active { outline: 10px solid blue; }
input:focus { border: 1px solid yellow; }
li:first-child { color: pink; }
li:last-child { color: purple; }
div:nth-child(2) { background-color: #09f; }
```

## 7. **Combinadores**

- **Descripción**: Selecciona elementos según su relación con otros elementos.
- **Tipos utilizados**:
  - Descendiente (` `): Selecciona todos los descendientes (ej., `main p`).
  - Hijo directo (`>`): Selecciona hijos directos (ej., `article > p`).
  - Hermano adyacente (`+`): Selecciona el primer hermano después de un elemento (ej., `article + p`).
  - Hermanos generales (`~`): Selecciona todos los hermanos después de un elemento (ej., `article ~ p`).
- **Ejemplo**:
```css
main p { color: whitesmoke; } /* Descendiente */
article > p { color: yellow; } /* Hijo directo */
article + p { color: #09f; } /* Hermano adyacente */
article ~ p { color: red; } /* Hermanos generales */
```

## 8. **Notas Adicionales**

- **Comentarios en el código**: El archivo incluye comentarios explicativos sobre:
  - Formatos de color (`rgb`, `rgba`, `hsl`, `oklch`).
  - Valores de `border` (`initial`, `inherit`, `unset`, `revert`).
  - Comportamiento de `height` en porcentaje (necesita un padre con altura explícita).
  - Reseteo de márgenes predeterminados en `body`.
  - Diferencia entre `inline` y `block` en `display`.
  - Propiedades de Flexbox (`flex-grow`, `flex-shrink`, `flex-basis`).
- **Uso de unidades**: Se utilizan `px` para medidas fijas y `vh` para medidas relativas a la ventana gráfica.
- **Modernidad**: Uso de `oklch`, `inset` y `rgb(0 0 0 / 50%)` refleja un enfoque moderno.
- **Flexbox**: Uso extensivo para layouts flexibles, con centrado y espaciado controlado.