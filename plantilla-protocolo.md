# Plantilla de protocolo — Experimento de ubicación de producto

**Equipo:** ___ · **Integrantes:** Jhon Jairo Tiupul Irua · **Fecha:** 19/11/2026

## 1. Pregunta e hipótesis

**Pregunta:** ¿Ubicar el producto estrella en el pasillo principal aumenta sus unidades vendidas por semana, frente a mantenerlo en su ubicación habitual, durante un período de 4 semanas?

La idea detrás es que el pasillo principal es por donde pasa casi todo cliente que entra a la tienda, entonces el producto tendría más exposición y más compras por impulso. Para que el experimento pueda confirmar o refutar esto, la hipótesis se plantea comparando el **cambio** en ventas de las tiendas tratadas contra el cambio de las tiendas control, tomando como punto de partida dos semanas de línea base.

- **H₀:** El aumento promedio de unidades vendidas por semana (período de tratamiento menos línea base) es igual o menor en las tiendas con el producto en el pasillo principal que en las tiendas con el producto en su ubicación habitual. (μ_pasillo − μ_habitual ≤ 0)
- **H₁:** El aumento promedio de unidades vendidas por semana es mayor en las tiendas con el producto en el pasillo principal. (μ_pasillo − μ_habitual > 0)

La respuesta se mide en unidades vendidas por semana, durante 4 semanas de tratamiento, y se considera evidencia a favor de H₁ si la prueba t pareada de una cola da un p-valor menor a 0,05.

## 2. Unidad experimental

- **Unidad:** la tienda. Es la que recibe el tratamiento, porque mover el producto de lugar es una decisión que se toma para todo el local y la vive cualquier cliente que entra, no se puede aplicar a un cliente sí y a otro no.
- **Número de unidades y justificación:** N = 12 tiendas, organizadas en 6 pares de tiendas parecidas (misma ciudad o región y volumen de ventas similar). Cada tienda se mide 6 semanas (2 de línea base + 4 de tratamiento), lo que da 72 registros tienda-semana, pero la unidad sigue siendo la tienda: las semanas de una misma tienda no son independientes entre sí.

Se escogió que cada tienda se quede en un solo grupo durante todo el experimento (y no alternar semana a semana) porque si el producto se mueve y se regresa, los clientes ya aprendieron dónde está y eso contamina la semana siguiente (efecto de arrastre). Doce tiendas es un número que la gerencia puede manejar sin mover el inventario de toda la cadena, y con el emparejamiento y la línea base se reduce bastante la variación entre tiendas, que es justo lo que más complica detectar el efecto con pocas unidades.

## 3. Factor, niveles y tratamiento

- **Factor** (variable manipulada): la ubicación del producto estrella dentro de la tienda.
- **Niveles** (valores del factor): (1) pasillo principal y (2) ubicación habitual.
- **Tratamiento** (combinación asignada): cada tienda recibe uno de los dos niveles durante las semanas 3 a 6. Las 6 tiendas del grupo tratamiento ponen el producto en una exhibición del pasillo principal (mismo tipo de estante y mismo espacio, sin carteles extra); las 6 del grupo control lo dejan exactamente donde siempre ha estado.

Hay que diferenciar bien: el pasillo principal es un **nivel** del factor, no el tratamiento en sí. El tratamiento es lo que se le asigna a cada tienda, que en este diseño es un solo nivel por tienda. En las semanas 1 y 2 (línea base) todas las tiendas tienen el producto en su ubicación habitual, así que esas semanas sirven para medir cuánto vende cada tienda "normalmente" antes de intervenir. Esto es coherente con la hipótesis porque lo que se compara es el cambio desde esa línea base.

## 4. Grupo de control

El grupo de control son las 6 tiendas que, por sorteo, mantienen el producto en su ubicación habitual durante las 6 semanas. Es la referencia sin tratamiento.

Su papel es mostrar qué hubiera pasado con las ventas si no se movía el producto. Durante esas semanas pueden cambiar muchas cosas que no tienen nada que ver con el pasillo: quincena, fin de mes, clima, alguna campaña de la marca a nivel nacional, o simplemente que las ventas vengan subiendo. Todo eso afecta a las dos tiendas de cada par por igual, entonces cuando restamos el cambio del control al cambio del tratamiento, lo que queda es (en principio) el efecto de la ubicación. Sin el grupo control solo tendríamos un "antes y después" de las tiendas tratadas y no se podría separar el efecto del pasillo de cualquier cosa que haya pasado en esas semanas.

Además, como cada tienda control está emparejada con una tienda tratamiento de la misma ciudad y tamaño parecido, la comparación es entre tiendas que se parecen, no entre una tienda grande de Guayaquil y una pequeña de la Sierra.

## 5. Aleatorización

**Método:** aleatorización por bloques (pares). Primero se forman 6 pares de tiendas similares según ciudad y ventas históricas del producto. Después, dentro de cada par se sortea cuál tienda va al pasillo principal y cuál se queda en la ubicación habitual. Así cada par aporta una tienda a cada grupo y los dos grupos quedan con 6 tiendas.

**¿Por qué es necesaria?** Si el gerente escogiera qué tiendas reciben el pasillo, lo más probable es que escoja las que "mejor venden" o las que tienen un administrador más colaborador, y ahí ya no sabríamos si el aumento es por la ubicación o por la tienda. Con el sorteo nadie decide, y los factores que no medimos (lo motivado que está el personal, el tipo de clientes, el estado del local) quedan repartidos al azar entre los dos grupos, entonces en promedio no favorecen a ninguno. El emparejamiento ayuda con los factores que sí conocemos (ciudad y tamaño), y el sorteo se encarga de los que no conocemos. Como el investigador asigna el tratamiento con código, es un experimento y no un estudio observacional.

**Línea de código de la asignación (Python):** está en `scripts/asignacion_aleatoria.py`.

```python
rng = np.random.default_rng(20261118)  # semilla fija
for i, par in enumerate(pares, start=1):
    orden = rng.choice(["pasillo_principal", "habitual"], size=2, replace=False)
```

La línea clave es `rng.choice([...], size=2, replace=False)`: para cada par saca los dos niveles en orden aleatorio sin repetir, entonces una tienda queda en pasillo y la otra en habitual. La semilla `20261118` permite que cualquiera vuelva a correr el script y obtenga exactamente el mismo sorteo.

**Resultado de la corrida** (`python scripts/asignacion_aleatoria.py`):

```
 bloque                tienda             grupo
      1     Quito La Carolina          habitual
      1         Quito Cumbaya pasillo_principal
      2        Quito Carcelen pasillo_principal
      2       Quito El Recreo          habitual
      3      Guayaquil Urdesa          habitual
      3 Guayaquil Samborondon pasillo_principal
      4    Guayaquil Alborada          habitual
      4         Guayaquil Sur pasillo_principal
      5         Santo Domingo          habitual
      5            Portoviejo pasillo_principal
      6              Riobamba pasillo_principal
      6                Ibarra          habitual

Tiendas por grupo:
habitual             6
pasillo_principal    6
```

Quedaron 6 tiendas en cada grupo y cada ciudad tiene tiendas en los dos grupos (por ejemplo, en Quito dos van al pasillo y dos se quedan en habitual), que es justo lo que buscaba el emparejamiento.

## 6. Respuesta y medición

- **Variable respuesta:** unidades vendidas del producto estrella por tienda y por semana (columna `ventas_producto` del registro). Se usan unidades y no dólares para que un cambio de precio no se confunda con un cambio en la demanda.
- **Período de medición:** 6 semanas seguidas: semanas 1–2 de línea base (todas en ubicación habitual) y semanas 3–6 de tratamiento. Se miden de lunes a domingo y todas las tiendas arrancan el mismo lunes.
- **Quién registra y cómo (¿ciego?):** las ventas salen automáticamente del sistema de punto de venta (POS) por código de barras, así que no dependen de que alguien cuente a mano. Cada lunes el equipo de BI descarga el reporte de la semana anterior y llena el registro (`tienda, semana, ubicacion, ventas_producto, promocion_simultanea, notas`). El jefe de cada tienda anota en `notas` cualquier novedad (quiebre de stock, feriado, cierre temprano).

Sobre el ciego: el personal de tienda y los clientes no pueden ser ciegos porque el producto se ve en el pasillo. Lo que sí se puede hacer es un **análisis ciego**: la persona que calcula los resultados recibe los grupos codificados como "A" y "B" y solo se revela cuál es cuál cuando el análisis ya está hecho. Así se evita que el analista, sin querer, ajuste el análisis para que salga a favor del pasillo. A los jefes de tienda tampoco se les dice cuál es la hipótesis, solo se les da la instrucción de dónde poner el producto.

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. Tamaño y ciudad de la tienda | **Bloqueo:** se forman pares de tiendas similares y se sortea dentro de cada par, así ningún grupo se queda con las tiendas más grandes o de una sola región. |
| 2. Temporada (quincena, fin de mes, feriados) | **Control por diseño:** todas las tiendas arrancan y terminan en las mismas semanas, y se evita programar el experimento en diciembre o semanas con feriado nacional. Si cae un feriado local se registra en `notas`. |
| 3. Promociones y descuentos | Se congelan las promociones del producto estrella durante las 6 semanas. Si marketing lanza una campaña igual, se registra en `promocion_simultanea` y se revisa el análisis con y sin esas semanas. |
| 4. Precio | Se mantiene el mismo precio en las 12 tiendas todo el período. Además la respuesta está en unidades, no en dólares. |
| 5. Disponibilidad de stock | Se fija un stock mínimo para todas las tiendas y se registra cualquier quiebre en `notas`, porque una semana sin producto en percha no mide el efecto de la ubicación sino la falta de inventario. |
| 6. Afluencia de clientes | Se registra el número de tickets por semana de cada tienda desde el POS, para poder ver si un cambio en ventas es porque entró más gente y no por el pasillo. |
| 7. Tipo de exhibición | Todas las tiendas tratadas usan el mismo estante y el mismo número de frentes en el pasillo, sin carteles ni degustaciones, para que el único cambio sea la ubicación. |

## 8. Limitaciones del diseño

Aunque el diseño trata de ser justo, hay cosas que podrían afectarlo:

- **Pocas tiendas:** con 12 tiendas (6 pares) el poder estadístico es bajo. Si el efecto real del pasillo es pequeño, puede pasar que el experimento no lo detecte y se concluya que "no hay efecto" cuando sí lo había.
- **Canibalización:** el producto estrella puede vender más en el pasillo pero quitándole ventas a otros productos de la tienda o a otras marcas. Este diseño solo mide las ventas del producto estrella, entonces no se puede concluir que la **tienda** gane más.
- **Efecto novedad:** las primeras semanas el producto en un lugar nuevo llama la atención, pero eso puede bajar con el tiempo. Con 4 semanas no se puede saber si el efecto se mantiene en el largo plazo.
- **Que no se cumpla el protocolo:** si algún jefe de tienda mueve el producto antes de tiempo, no respeta el estante acordado o se queda sin stock, el tratamiento ya no es el mismo en todas las tiendas.
- **Generalización:** las 12 tiendas son de ciudades grandes e intermedias. No se puede asegurar que el resultado sirva igual para tiendas pequeñas o rurales, ni para otros productos que no sean el producto estrella.
- **Eventos dentro de un par:** el emparejamiento asume que las dos tiendas del par viven lo mismo durante esas semanas. Si a una le abren competencia al lado o le cierran la calle, eso queda mezclado con el efecto.

## 9. Comparación en código (Python/R)

Se completaron los TODOs de `scripts/comparacion_experimento.py` y se ejecutó con `python scripts/comparacion_experimento.py` sobre `plantillas/registro_experimento.csv`.

**Salida de la parte de la plantilla:**

```
Registro de la plantilla:
          tienda  semana         ubicacion  ventas_producto promocion_simultanea  notas
