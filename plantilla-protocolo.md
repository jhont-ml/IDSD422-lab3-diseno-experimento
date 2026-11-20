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

**¿Por qué es necesaria?** Si el gerente decidiera qué tiendas empiezan en el pasillo, podría escoger sin querer las que mejor venden o las que estaban por tener una buena semana, y ese sesgo se mezclaría con el efecto. Con el sorteo nadie elige, y cualquier factor que no medimos (una obra en la calle, un administrador nuevo, un evento local) tiene la misma probabilidad de caer en cualquiera de las dos secuencias. Además, sortear el orden evita que todas las tiendas tengan el pasillo justo en las semanas que de por sí venden más. Como el investigador es quien asigna con código, el estudio es un experimento y no un estudio observacional.

**Línea de código de la asignación (Python):** el sorteo está en `scripts/comparacion_experimento.py`, en la parte "DISENIO DE EXPERIMENTO". Para ver la corrida por separado se ejecuta este bloque:

```python
import numpy as np

tiendas = ["Quito Norte", "Quito Sur", "Guayaquil Centro", "Guayaquil Norte",
           "Cuenca Centro", "Cuenca Sur", "Ambato Centro", "Manta", "Loja", "Machala"]

rng = np.random.default_rng(1234597)  # semilla fija
primera = rng.choice(["pasillo_principal", "habitual"], size=len(tiendas))

for tienda, cond in zip(tiendas, primera):
    print(tienda, cond)
```

La línea clave es `rng.choice(["pasillo_principal", "habitual"], size=len(tiendas))`, que le asigna al azar a cada tienda la ubicación con la que empieza. La semilla `1234597` hace que el sorteo sea reproducible: cualquier persona que corra el código obtiene exactamente la misma asignación.

**Resultado de la corrida:**

```
Quito Norte habitual
Quito Sur pasillo_principal
Guayaquil Centro habitual
Guayaquil Norte pasillo_principal
Cuenca Centro pasillo_principal
Cuenca Sur habitual
Ambato Centro habitual
Manta habitual
Loja habitual
Machala pasillo_principal
```

Con esto, la secuencia de cada tienda queda así (en las semanas 2 y 4 pasa a la ubicación contraria):

| Tienda | Semanas 1 y 3 | Semanas 2 y 4 |
|---|---|---|
| Quito Norte | habitual | pasillo principal |
| Quito Sur | pasillo principal | habitual |
| Guayaquil Centro | habitual | pasillo principal |
| Guayaquil Norte | pasillo principal | habitual |
| Cuenca Centro | pasillo principal | habitual |
| Cuenca Sur | habitual | pasillo principal |
| Ambato Centro | habitual | pasillo principal |
| Manta | habitual | pasillo principal |
| Loja | habitual | pasillo principal |
| Machala | pasillo principal | habitual |

El sorteo dejó 4 tiendas empezando en pasillo y 6 en habitual. Como `choice` sortea cada tienda por separado, no garantiza un 5 y 5 exacto, pero eso no afecta la comparación principal: todas las tiendas pasan igual 2 semanas por cada ubicación. Lo único es que en las semanas 1 y 3 hay un poco más de tiendas en habitual, y en las semanas 2 y 4 un poco más en pasillo. Si se quisiera un balance exacto se podría usar `rng.permutation(["pasillo_principal"] * 5 + ["habitual"] * 5)`.

## 6. Respuesta y medición

- **Variable respuesta:** ventas semanales del producto estrella en USD por tienda (columna `ventas_producto` del registro).
- **Período de medición:** 4 semanas consecutivas, de lunes a domingo, con las 10 tiendas empezando el mismo lunes. El cambio de ubicación se hace el domingo en la noche, después del cierre, para que cada semana empiece completa en su condición.
- **Quién registra y cómo (¿ciego?):** el dato sale del sistema de punto de venta (POS) por código de barras, no de un conteo manual. Cada lunes el analista de BI descarga el reporte de la semana anterior y llena una fila por tienda en el registro (`tienda, semana, ubicacion, ventas_producto, promocion_simultanea, notas`). El administrador de cada tienda reporta cualquier novedad de la semana (quiebre de stock, feriado, cierre) para la columna `notas`.

**Ciego:** no se puede ocultar el tratamiento al personal ni a los clientes, porque el producto en el pasillo se ve. Por eso se aplica un ciego en el análisis: el analista recibe la columna de ubicación codificada como "A" y "B" y solo se le revela qué es cada código cuando ya calculó los resultados. A los administradores no se les explica la hipótesis, solo se les entrega el calendario de dónde va el producto cada semana, para que no cambien su forma de trabajar.

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. Diferencias entre tiendas (tamaño, ciudad, clientes) | **Bloqueo:** cada tienda pasa por las dos condiciones y se compara consigo misma, así el efecto de la tienda se cancela en la diferencia. |
| 2. Tendencia de las semanas (quincena, fin de mes) | **Alternancia y sorteo del orden:** cada tienda tiene pasillo y habitual intercalados, y el sorteo hace que unas empiecen en pasillo y otras en habitual, así cada semana tiene tiendas en las dos condiciones. Se evita diciembre y semanas con feriado nacional. |
| 3. Promociones simultáneas | Se pide a marketing no lanzar promociones del producto durante el experimento. Si alguna ocurre igual, se registra en `promocion_simultanea` y se revisa el análisis con y sin esa semana. |
| 4. Precio | Se mantiene el mismo precio en las 10 tiendas las 4 semanas; cualquier cambio obligatorio se anota en `notas`. |
| 5. Stock disponible | Se asegura un inventario mínimo antes de cada semana y se registra cualquier quiebre, porque una semana sin producto en percha no mide la ubicación. |
| 6. Forma de exhibición | Mismo número de frentes y misma presentación en las dos ubicaciones, sin carteles, degustaciones ni impulsadoras, para que solo cambie el lugar. |
| 7. Afluencia de clientes | Se registra el número de tickets semanales de cada tienda para detectar semanas con tráfico anormal. |

## 8. Limitaciones del diseño

- **Efecto de arrastre:** como el producto cambia de lugar cada semana, algunos clientes que lo encontraron en el pasillo pueden seguir buscándolo (o comprarlo con más frecuencia) la semana siguiente en la ubicación habitual. Eso reduciría la diferencia medida y haría que el efecto parezca menor de lo que es.
- **Semanas cortas:** con una semana por bloque, una sola novedad (un feriado local, un día de lluvia fuerte, un quiebre de stock) pesa mucho en el promedio de esa tienda.
- **Orden no balanceado:** el sorteo dejó 4 tiendas empezando en pasillo y 6 en habitual. Si las ventas suben semana a semana, las semanas 2 y 4 (con más tiendas en pasillo) podrían favorecer un poco al pasillo.
- **Pocas tiendas:** el análisis se hace con n = 10 diferencias. Si el efecto real es pequeño, puede que la prueba no lo detecte.
- **Canibalización:** solo se miden las ventas del producto estrella. Si el producto vende más en el pasillo quitándole ventas a otros artículos, el experimento no lo vería, así que no se puede concluir que la tienda en total gane más.
- **Duración:** en 4 semanas no se sabe si el efecto se mantiene o si es solo novedad que desaparece cuando los clientes se acostumbran.
- **Generalización:** las conclusiones valen para estas 10 tiendas, este producto y este período. No se pueden extender directamente a otras tiendas o productos de RetailAndina.

## 9. Comparación en código (Python/R)

Se completaron los TODOs de `scripts/comparacion_experimento.py` y `scripts/comparacion_experimento.R`, y se ejecutaron desde la raíz del repositorio sobre `plantillas/registro_experimento.csv`:

```
python scripts/comparacion_experimento.py
Rscript scripts/comparacion_experimento.R
```

**Salida de Python (parte de la plantilla):**

```
             tienda  semana  ... promocion_simultanea  notas
0       Quito Norte       1  ...                   no    NaN
1         Quito Sur       1  ...                   no    NaN
2  Guayaquil Centro       1  ...                   si    NaN
3   Guayaquil Norte       1  ...                   no    NaN

[4 rows x 6 columns]

ubicacion
habitual             1040.0
pasillo_principal    1335.0
Name: ventas_producto, dtype: float64

ubicacion
pasillo_principal    2
habitual             2
Name: count, dtype: int64
```

**Salida de R:**

```
Promedio de ventas por ubicación:
          ubicacion ventas_producto
1          habitual            1040
2 pasillo_principal            1335

Número de registros por ubicación:
         habitual pasillo_principal
                2                 2

Promedio por tienda y ubicación:
                 habitual pasillo_principal
Guayaquil Centro       NA              1420
Guayaquil Norte      1100                NA
Quito Norte            NA              1250
Quito Sur             980                NA

Tiendas con observaciones emparejadas: 0

No existen suficientes observaciones emparejadas.
No es posible calcular diferencias estadísticas ni realizar una prueba t pareada válida.
```

### ¿Qué grupo muestra mayor venta promedio en la plantilla?

El pasillo principal: 1335 USD de promedio contra 1040 USD de la ubicación habitual, una diferencia de 295 USD. Python y R dan el mismo resultado.

### ¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?

Porque son cuatro tiendas distintas en una sola semana, dos en cada ubicación, y ninguna se observa en las dos condiciones. La tabla de R lo muestra claro: cada tienda tiene un `NA` en una de las columnas, así que hay **0 tiendas emparejadas** y no se puede hacer la prueba t pareada. La diferencia de 295 USD puede deberse simplemente a que Quito Norte y Guayaquil Centro venden más que Quito Sur y Guayaquil Norte, sin importar dónde esté el producto. Además, Guayaquil Centro tuvo una promoción simultánea esa semana, así que en esa fila el efecto de la promoción y el del pasillo están mezclados. Con n = 2 por grupo tampoco se puede estimar bien la variabilidad. El promedio por grupo solo describe estas cuatro filas; no prueba nada sobre la ubicación.

### Si el experimento se ejecutara con mi protocolo, ¿qué le faltaría a este análisis para ser justo?

Le faltaría tener las 40 filas del protocolo (10 tiendas × 4 semanas) con la asignación del sorteo de la sección 5, para que cada tienda aparezca en las dos ubicaciones. Con eso, en vez de comparar promedios simples por ubicación, se calcula para cada tienda la diferencia entre su promedio en pasillo y su promedio en habitual, y se aplica una prueba t pareada sobre esas 10 diferencias, reportando también el intervalo de confianza. Por último, habría que revisar las semanas con promoción simultánea o quiebre de stock para ver si cambian el resultado.

### Prueba con datos simulados (material complementario)

El script de Python también simula el protocolo completo con el sorteo de la sección 5 y guarda los 40 registros en `plantillas/resultado_simulacion (2).csv`. En la simulación se programó un efecto de +220 USD para el pasillo y una promoción de +180 USD en Guayaquil Centro en la semana 1, como confusor. La salida del análisis pareado es:

```
Promedio de la diferencia de ventas entre ubicaciones: 239.7
Desviación estándar de la diferencia de ventas entre ubicaciones: 102.39471557545231
IC %95 = [166.4512330781982 , 312.9487669218018
p-value: 4.091661932963184e-05
```

| Indicador | Resultado |
|---|---|
| Tiendas y semanas | 10 tiendas × 4 semanas = 40 registros simulados |
| Promedio de las diferencias por tienda | 239,70 USD |
| Desviación estándar de las diferencias | 102,39 USD |
| Intervalo de confianza del 95 % | [166,45 ; 312,95] USD |
| Prueba t pareada (p-valor) | 0,0000409 |

**Interpretación:** con los datos simulados, la diferencia promedio entre pasillo y habitual es de 239,70 USD por tienda y el intervalo de confianza del 95 % (166,45 a 312,95) no incluye el cero, con un p-valor mucho menor a 0,05. El análisis recupera un efecto cercano al que se programó (240 frente a 220); sale un poco más alto por el ruido aleatorio y porque el pasillo cayó más veces en las semanas 2 y 4, que tienen una tendencia de ventas más alta. Pero esto **no es evidencia sobre RetailAndina**: los datos son ficticios y el efecto se puso a propósito en la simulación. Solo sirve para comprobar que, si el experimento se ejecuta, el análisis pareado está listo para responder la pregunta. Además, las 40 filas son mediciones repetidas de 10 tiendas, por eso la prueba se hace sobre las 10 diferencias y no sobre las 40 filas.

### Interpretación final

En la plantilla de 4 filas el pasillo principal muestra 295 USD más de promedio, pero eso es solo descriptivo: no hay tiendas emparejadas, hay una promoción mezclada y la muestra es mínima, así que no se puede decir que la ubicación cause el aumento. La simulación muestra que, con el protocolo completo de 10 tiendas × 4 semanas y un análisis pareado, sí se podría detectar un efecto de ese tamaño. Para tomar una decisión real, RetailAndina tendría que ejecutar el protocolo, controlar los factores de la sección 7 y analizar sus propios datos.

## 10. Bonus: adaptación a un ensayo clínico (vacuna)

El mismo esquema se puede pasar a un ensayo de una vacuna, con un cambio importante: en una vacuna no se puede hacer que la misma persona alterne entre vacuna y placebo, porque una vez vacunada la protección se queda (sería un arrastre total). Por eso se mantiene la lógica de control y aleatorización, pero con grupos paralelos.

- **Hipótesis:** H₀: la proporción de participantes que se infectan en 6 meses es igual o mayor en el grupo vacuna que en el grupo placebo. H₁: la proporción de infectados es menor en el grupo vacuna.
- **Unidad experimental:** cada participante voluntario, por ejemplo N = 2000 adultos sin infección previa confirmada.
- **Factor y niveles:** factor = sustancia inyectada; niveles = vacuna y placebo. El tratamiento es recibir la vacuna.
- **Grupo de control:** los participantes que reciben placebo; muestran cuántos se infectarían en el mismo período sin la vacuna.
- **Aleatorización:** igual que con las tiendas se sortea con semilla, pero aquí conviene un sorteo balanceado, por ejemplo `rng.permutation(["vacuna"] * 1000 + ["placebo"] * 1000)`, y de preferencia dentro de bloques de edad para que cada grupo tenga la misma proporción de jóvenes y adultos mayores.
- **Respuesta:** infección confirmada por prueba de laboratorio durante 6 meses de seguimiento (sí/no).
- **Ciego:** aquí sí es posible un **doble ciego**: las dos inyecciones se ven iguales y ni el participante ni el médico saben qué recibió cada uno. Con las tiendas esto no se podía porque el producto en el pasillo se ve.
- **Factores a controlar:** edad, enfermedades previas, nivel de exposición (por ejemplo, personal de salud), región y uso de medidas de protección, ya sea bloqueando o registrándolos.
- **Limitaciones:** si el virus circula poco durante el estudio habrá pocos casos y poco poder; con 6 meses no se sabe cuánto dura la protección, y los efectos adversos muy raros necesitan muestras más grandes.
