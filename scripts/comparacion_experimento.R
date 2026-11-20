# comparacion_experimento.R — Comparación de grupos (R)
# Ejecutar desde la raíz del repositorio:
# Rscript scripts/comparacion_experimento.R

# TODO 1: Leer el archivo CSV
df <- read.csv(
  "plantillas/registro_experimento.csv",
  stringsAsFactors = FALSE
)

# TODO 2: Promedio de ventas por ubicación
cat("\nPromedio de ventas por ubicación:\n")

print(aggregate(
  ventas_producto ~ ubicacion,
  data = df,
  FUN = mean
))

# TODO 3: Número de registros por grupo
cat("\nNúmero de registros por ubicación:\n")
print(table(df$ubicacion))

# 3. Mostrar datos del experimento
cat("\nDatos del experimento:\n")

print(df[, c(
  "tienda", "semana", "ubicacion",
  "ventas_producto", "promocion_simultanea"
)])

# 4. Promedio por tienda y ubicación
media_tienda <- tapply(
  df$ventas_producto,
  list(df$tienda, df$ubicacion),
  mean
)

cat("\nPromedio por tienda y ubicación:\n")
print(round(media_tienda, 0))

# 5. Diferencias entre ubicaciones por tienda
# Seleccionar únicamente tiendas con ambas ubicaciones
tiendas_validas <- complete.cases(media_tienda)

media_pareada <- media_tienda[
  tiendas_validas, , drop = FALSE
]

cat("\nTiendas con observaciones emparejadas:",
    nrow(media_pareada), "\n")

# 6. Análisis de diferencias
if (nrow(media_pareada) >= 2) {

  diferencias <- media_pareada[, "pasillo_principal"] -
                 media_pareada[, "habitual"]

  cat("\nDiferencias entre ubicaciones por tienda:\n")
  print(diferencias)

  # Promedio general de las diferencias
  print(mean(diferencias))

  # Promedio y desviación estándar
  media <- mean(diferencias)
  dev <- sd(diferencias)

  cat("\n")
  cat("Promedio de la diferencia de ventas entre ubicaciones:",
      media, "\n")
  cat("Desviación estándar de la diferencia de ventas entre ubicaciones:",
      dev, "\n")

  # Intervalo de confianza del 95%
  n <- length(diferencias)

  t_crit <- qt(0.975, df = n - 1)

  ic_inf <- media - (t_crit * dev / sqrt(n))
  ic_sup <- media + (t_crit * dev / sqrt(n))

  cat(sprintf("IC 95%% = [%.2f, %.2f]\n",
              ic_inf, ic_sup))

  # Prueba p-value: t de Student pareada
  if (dev > 0) {

    prueba <- t.test(
      media_pareada[, "pasillo_principal"],
      media_pareada[, "habitual"],
      paired = TRUE
    )

    cat("p-value:", prueba$p.value, "\n")

  } else {
    cat("\nNo se puede calcular la prueba t:",
        "las diferencias no presentan variabilidad.\n")
  }

} else {

  cat("\nNo existen suficientes observaciones emparejadas.\n")
  cat("No es posible calcular diferencias estadísticas",
      "ni realizar una prueba t pareada válida.\n")
}

# TODO 4: Interpretación de los resultados
cat("\nInterpretación de los resultados:\n")

cat("Con solo 4 registros no es posible establecer conclusiones confiables sobre el efecto de la ubicación en las ventas.\n")

cat("Es necesario aumentar el número de observaciones por grupo para obtener resultados estadísticamente más sólidos.\n")

cat("También se deben controlar factores externos, como las promociones simultáneas, y evaluar la significancia estadística.\n")
