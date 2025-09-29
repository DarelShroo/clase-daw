# Referencia Rápida de las Relaciones del Diagrama ER

Este documento proporciona una referencia rápida de las relaciones en el diagrama Entidad-Relación (ER) mejorado para el sistema "Smart Economart". Cada relación se lista con sus entidades, etiqueta, tipo de cardinalidad (e.g., 1:1, 1:N, N:M), una breve descripción, el porqué de su existencia (justificación basada en los requisitos originales, como RF-01 para requisitos funcionales) y el sentido lógico que tiene en el contexto del sistema (gestión de inventario, pedidos y control de calidad en un entorno educativo de cocina). Las relaciones aseguran integridad de datos, trazabilidad y soporte a características clave.

## 1. PROVEEDORES -> ALBARANES (etiqueta: "pertenece a")
- **Tipo de relación**: 1:N (un proveedor puede tener muchos albaranes, pero cada albarán pertenece a un solo proveedor).
- **Descripción**: Un proveedor está asociado con uno o más albaranes de entrega, indicando que cada albarán pertenece a un proveedor específico.
- **Por qué existe**: Para rastrear el origen de los productos recibidos y gestionar la responsabilidad de los proveedores. Basado en RF-02 de "Requisitos de Aplicativo de Recepción de Productos" (base de datos de proveedores para seguimiento y control).
- **Sentido lógico**: Permite auditar entregas por proveedor, facilitando evaluaciones de rendimiento y optimización de compras en un entorno con presupuesto limitado.

## 2. ALBARANES -> DETALLES_ALBARANES (etiqueta: "contiene")
- **Tipo de relación**: 1:N (un albarán contiene muchos detalles, pero cada detalle pertenece a un solo albarán).
- **Descripción**: Cada albarán contiene múltiples líneas de detalle, representando los ítems en una entrega.
- **Por qué existe**: Para normalizar datos en entregas con múltiples ítems, permitiendo el registro detallado de cantidades y costos. Soporta RF-01 y RF-04 de "Requisitos de Aplicativo de Recepción de Productos" (registrar recepción y costos).
- **Sentido lógico**: Evita redundancia al separar la cabecera general del albarán de los ítems específicos, facilitando cálculos precisos y actualizaciones de inventario.

## 3. DETALLES_ALBARANES -> PRODUCTOS (etiqueta: "detalla")
- **Tipo de relación**: N:1 (muchos detalles pueden referenciar un producto, pero cada detalle se refiere a un solo producto).
- **Descripción**: Cada línea de detalle en un albarán se refiere a un producto específico.
- **Por qué existe**: Para vincular ítems recibidos al catálogo de productos, asegurando consistencia y actualizaciones de inventario. Esencial para autocompletado y reducción de errores (RF-03 de "Requisitos de Aplicativo de Recepción de Productos").
- **Sentido lógico**: Conecta las recepciones reales con el catálogo maestro, permitiendo trazabilidad de lotes y alertas de stock.

## 4. DETALLES_ALBARANES -> IMPUESTOS (etiqueta: "aplica")
- **Tipo de relación**: N:1 (muchos detalles pueden aplicar un impuesto, pero cada detalle aplica un solo impuesto).
- **Descripción**: Cada línea de detalle aplica un tipo específico de impuesto.
- **Por qué existe**: Para calcular costos precisos incluyendo impuestos por ítem. Implícito en los requisitos de control financiero (RF-04 de "Requisitos de Aplicativo de Recepción de Productos").
- **Sentido lógico**: Permite flexibilidad en la aplicación de impuestos variables por producto, mejorando la precisión en reportes financieros.

## 5. USUARIOS -> PEDIDOS_INTERNO (etiqueta: "genera (profesores)")
- **Tipo de relación**: 1:N (un usuario/profesor puede generar muchos pedidos, pero cada pedido es generado por un solo usuario).
- **Descripción**: Usuarios (específicamente con rol 'profesor') generan pedidos internos.
- **Por qué existe**: Para atribuir pedidos a profesores por responsabilidad en un entorno educativo. Basado en RF-01 de "Requisitos del Sistema de Pedidos para Profesores" (profesores seleccionan ingredientes).
- **Sentido lógico**: Asegura accountability y facilita notificaciones o aprobaciones, alineado con la colaboración entre profesores y administración.

## 6. PEDIDOS_INTERNO -> DETALLES_PEDIDOS_INTERNO (etiqueta: "contiene")
- **Tipo de relación**: 1:N (un pedido contiene muchos detalles, pero cada detalle pertenece a un solo pedido).
- **Descripción**: Cada pedido interno contiene múltiples líneas de detalle para ítems solicitados.
- **Por qué existe**: Para manejar pedidos con múltiples ítems de manera eficiente. Soporta listas consolidadas (RF-04 de "Requisitos del Sistema de Pedidos para Profesores").
- **Sentido lógico**: Normaliza la estructura para pedidos complejos, permitiendo escalabilidad y cálculos de costos totales dinámicos.

## 7. DETALLES_PEDIDOS_INTERNO -> PRODUCTOS (etiqueta: "detalla")
- **Tipo de relación**: N:1 (muchos detalles de pedidos pueden referenciar un producto, pero cada detalle se refiere a un solo producto).
- **Descripción**: Cada detalle de pedido se refiere a un producto específico.
- **Por qué existe**: Para especificar qué se solicita, habilitando cálculos de costos y verificaciones de stock. Vinculado a RF-03 de "Requisitos del Sistema de Pedidos para Profesores" (mostrar costo total antes de confirmar).
- **Sentido lógico**: Integra pedidos con inventario, previniendo solicitudes de productos no disponibles.

## 8. PEDIDOS_INTERNO -> USOS_SOBRANTES (etiqueta: "registra")
- **Tipo de relación**: 1:N (un pedido registra muchos usos/sobrantes, pero cada uso pertenece a un solo pedido).
- **Descripción**: Cada pedido registra el uso y sobrantes.
- **Por qué existe**: Para rastrear utilización de recursos y minimizar desperdicios. De RF-02 y RF-03 de "Requisitos de Gestión de Almacén de Cocina" (registrar uso y asignar sobrantes).
- **Sentido lógico**: Cierra el ciclo de un pedido, permitiendo redistribución de sobrantes y análisis de eficiencia por clase.

## 9. USOS_SOBRANTES -> PRODUCTOS (etiqueta: "detalla")
- **Tipo de relación**: N:1 (muchos usos pueden detallar un producto, pero cada uso detalla un solo producto).
- **Descripción**: Los usos/sobrantes detallan un producto específico.
- **Por qué existe**: Para rastrear consumo granular por producto. Soporta optimización de recursos en cocinas educativas.
- **Sentido lógico**: Actualiza stock en tiempo real y genera insights sobre patrones de desperdicio.

## 10. PRODUCTOS -> BAJAS (etiqueta: "registra")
- **Tipo de relación**: 1:N (un producto puede registrar muchas bajas, pero cada baja es de un solo producto).
- **Descripción**: Los productos registran descartes (bajas).
- **Por qué existe**: Para registrar pérdidas y mantener precisión de inventario. Implícito en la reducción de desperdicios (RF-05 de "Requisitos de Gestión de Almacén de Cocina").
- **Sentido lógico**: Permite análisis de causas de pérdidas (e.g., caducidad) y ajustes en compras futuras.

## 11. PRODUCTOS -> INVENTARIO (etiqueta: "tiene")
- **Tipo de relación**: 1:N (un producto tiene muchos registros de inventario, e.g., lotes, pero cada registro es de un solo producto).
- **Descripción**: Cada producto tiene uno o más registros de inventario (e.g., lotes).
- **Por qué existe**: Para gestionar niveles de stock y trazabilidad. Núcleo de RF-01 de "Requisitos de Gestión de Almacén de Cocina" (sistema de inventario).
- **Sentido lógico**: Soporta FIFO y alertas de caducidad, esencial para seguridad alimentaria.

## 12. INVENTARIO -> LOG_TEMPERATURAS (etiqueta: "registra")
- **Tipo de relación**: 1:N (un registro de inventario registra muchos logs de temperatura, pero cada log es de un solo registro de inventario).
- **Descripción**: Los registros de inventario registran logs de temperatura.
- **Por qué existe**: Para monitorear calidad de alimentos. Directamente de RF-02 de "Smart Economart" (registro de temperaturas).
- **Sentido lógico**: Asegura cumplimiento normativo (HACCP) y previene uso de productos en mal estado.

## 13. LOG_TEMPERATURAS -> USUARIOS (etiqueta: "responsable")
- **Tipo de relación**: N:1 (muchos logs pueden tener un responsable, pero cada log tiene un solo responsable).
- **Descripción**: Los logs de temperatura están asociados a un usuario responsable.
- **Por qué existe**: Para auditabilidad y responsabilidad en contextos educativos/entrenamiento.
- **Sentido lógico**: Facilita entrenamiento de alumnos y resolución de incidencias.

## 14. PRODUCTOS -> RENDIMIENTOS (etiqueta: "mide")
- **Tipo de relación**: 1:N (un producto mide muchos rendimientos, pero cada rendimiento es de un solo producto).
- **Descripción**: Los productos miden rendimientos (yields).
- **Por qué existe**: Para calcular eficiencia y costos reales. De RF-01 y RF-02 de "Requisitos de Gestión de Rendimiento en Cocina".
- **Sentido lógico**: Optimiza procesos educativos, ajustando expectativas de merma en clases.

## 15. RECETAS -> DETALLES_RECETAS (etiqueta: "contiene")
- **Tipo de relación**: 1:N (una receta contiene muchos detalles de ingredientes, pero cada detalle pertenece a una sola receta).
- **Descripción**: Cada receta contiene múltiples detalles de ingredientes.
- **Por qué existe**: Para desglosar recetas en planificación. Soporta RF-05 de "Requisitos de Gestión de Rendimiento en Cocina".
- **Sentido lógico**: Integra recetas con stock para pronósticos de necesidades.

## 16. DETALLES_RECETAS -> PRODUCTOS (etiqueta: "usa")
- **Tipo de relación**: N:1 (muchos detalles de recetas usan un producto, pero cada detalle usa un solo producto).
- **Descripción**: Los detalles de recetas usan productos específicos.
- **Por qué existe**: Para vincular ingredientes a stock en pronósticos de necesidades.
- **Sentido lógico**: Permite escalado de recetas y verificación de disponibilidad.

## 17. DETALLES_RECETAS -> UNIDADES (etiqueta: "mide")
- **Tipo de relación**: N:1 (muchos detalles miden en una unidad, pero cada detalle mide en una sola unidad).
- **Descripción**: Los detalles de recetas se miden en unidades específicas.
- **Por qué existe**: Para estandarización y escalado preciso.
- **Sentido lógico**: Evita errores en conversiones de medidas durante clases prácticas.

## 18. PRODUCTOS -> UNIDADES (etiqueta: "mide")
- **Tipo de relación**: N:1 (muchos productos miden en una unidad, pero cada producto mide en una sola unidad por defecto).
- **Descripción**: Los productos se miden en unidades predeterminadas.
- **Por qué existe**: Para manejo consistente de cantidades en todo el sistema.
- **Sentido lógico**: Centraliza la lógica de medidas, facilitando integraciones con pesajes (RF-03 de "Gestión de Materiales en Cocina").

## 19. PRODUCTOS -> MOVIMIENTOS (etiqueta: "registra")
- **Tipo de relación**: 1:N (un producto registra muchos movimientos, pero cada movimiento es de un solo producto).
- **Descripción**: Los productos registran movimientos (entradas/salidas).
- **Por qué existe**: Para rastro completo de cambios en stock, mejorando trazabilidad.
- **Sentido lógico**: Unifica auditorías de inventario, detectando varianzas.

## 20. USUARIOS -> MOVIMIENTOS (etiqueta: "realiza")
- **Tipo de relación**: 1:N (un usuario realiza muchos movimientos, pero cada movimiento es realizado por un solo usuario).
- **Descripción**: Los usuarios realizan movimientos.
- **Por qué existe**: Para atribuir acciones por seguridad y auditoría en un entorno compartido educativo.
- **Sentido lógico**: Soporta responsabilidad y análisis de patrones de uso por rol (e.g., profesores vs. alumnos).