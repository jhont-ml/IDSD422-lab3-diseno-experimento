# Plantilla de protocolo — Experimento de ubicación de producto

**Equipo:** ___ · **Integrantes:** Jhon Jairo Tiupul Irua · **Fecha:** 19/11/2026

## 1. Pregunta e hipótesis

**Pregunta:** ¿Las ventas semanales del producto estrella son mayores cuando está en el pasillo principal que cuando está en su ubicación habitual, comparando la misma tienda en las dos condiciones durante 4 semanas?

La sospecha de la gerencia es que el pasillo principal le da más visibilidad al producto, porque es la zona por la que circula casi todo cliente, y eso debería traducirse en más compras. Para poder confirmarlo o refutarlo con datos, la hipótesis se escribe como una comparación dentro de cada tienda: la diferencia entre sus ventas promedio con el producto en el pasillo y sus ventas promedio con el producto en la ubicación habitual.

- **H₀:** La diferencia promedio de ventas semanales (pasillo principal − ubicación habitual) en una misma tienda es cero o negativa. (μ_d ≤ 0)
- **H₁:** La diferencia promedio de ventas semanales (pasillo principal − ubicación habitual) en una misma tienda es positiva. (μ_d > 0)

La respuesta son las ventas semanales del producto en USD, el período son 4 semanas consecutivas, y la decisión se toma con una prueba t pareada sobre las diferencias de las 10 tiendas, con un nivel de significancia de 0,05.

## 2. Unidad experimental

- **Unidad:** la tienda en una semana (tienda-semana). Cada semana se decide en qué lugar va el producto dentro de esa tienda, y eso es lo que recibe el tratamiento. La tienda completa funciona como un bloque, porque pasa por las dos condiciones.
- **Número de unidades y justificación:** 10 tiendas × 4 semanas = 40 unidades tienda-semana. Cada tienda tiene 2 semanas en pasillo principal y 2 semanas en ubicación habitual.

Se escogió este diseño (cada tienda es su propio control) porque las tiendas de RetailAndina son muy distintas entre sí: no vende lo mismo un local grande de Guayaquil que uno de Loja. Si se comparara un grupo de tiendas contra otro, esas diferencias podrían tapar el efecto del pasillo. Comparando a cada tienda consigo misma, el tamaño, la ciudad y el tipo de clientes se cancelan. Diez tiendas permiten cubrir la Costa y la Sierra sin tener que mover el producto en toda la cadena, y cuatro semanas alcanzan para que cada tienda pase dos veces por cada condición.

Hay que aclarar que las 40 observaciones no son 40 datos independientes: son mediciones repetidas de las mismas 10 tiendas. Por eso el análisis final se hace con una diferencia por tienda (n = 10), no con las 40 filas sueltas.

## 3. Factor, niveles y tratamiento

- **Factor** (variable manipulada): la ubicación física del producto estrella dentro de la tienda.
- **Niveles** (valores del factor): pasillo principal y ubicación habitual.
- **Tratamiento** (combinación asignada): cada tienda recibe una secuencia de niveles en el tiempo. Hay dos secuencias posibles: **A** = pasillo, habitual, pasillo, habitual (semanas 1 a 4), y **B** = habitual, pasillo, habitual, pasillo. El sorteo decide qué secuencia le toca a cada tienda.

El pasillo principal es un **nivel** del factor, no el tratamiento. El tratamiento es lo que se le asigna a cada unidad: en una semana de pasillo, el producto se coloca en una exhibición del pasillo principal con el mismo número de frentes que tiene normalmente y sin carteles adicionales. En una semana habitual, el producto queda en su percha de siempre. Así lo único que cambia entre una semana y otra es el lugar, que es justo lo que pregunta la hipótesis.

## 4. Grupo de control

La referencia sin tratamiento son las semanas en las que el producto se queda en su ubicación habitual. En este diseño no hay un grupo de tiendas aparte que sea el control: **cada tienda es su propio control**, porque se observa con y sin el producto en el pasillo.

El papel del control es responder qué hubiera vendido esa misma tienda si no se movía el producto. Sin esa referencia, un aumento en ventas podría deberse a cualquier cosa (fin de mes, más afluencia, una campaña de la marca) y no habría forma de atribuirlo al pasillo. Al tener la misma tienda en las dos condiciones, todo lo que es propio del local (tamaño, ubicación, clientes fieles, cómo atiende el personal) queda igual en el control y en el tratamiento, y la resta pasillo − habitual aísla mejor el efecto de la ubicación.

Además, como unas tiendas empiezan con el control y otras con el tratamiento, el control también ayuda a separar el efecto del pasillo del paso de las semanas.

## 5. Aleatorización

**Método:** sorteo de la secuencia con semilla fija. A cada una de las 10 tiendas se le sortea, de forma independiente, con qué ubicación empieza (semanas 1 y 3); en las semanas 2 y 4 pasa a la ubicación contraria. Así todas las tiendas terminan con 2 semanas en cada condición.

**¿Por qué es necesaria?** Si el gerente decidiera qué tiendas empiezan en el
