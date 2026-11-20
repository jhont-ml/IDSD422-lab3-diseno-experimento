# comparacion_experimento.py — Comparación de grupos (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/comparacion_experimento.py

import numpy as np
import pandas as pd
from scipy import stats

pd.set_option("display.width", 120)

# TODO 1: carga plantillas/registro_experimento.csv con pandas
df = pd.read_csv("plantillas/registro_experimento.csv")
print("Registro de la plantilla:")
print(df.to_string(index=False))

# TODO 2: calcula e imprime el promedio de ventas_producto por ubicacion
print("\nPromedio de ventas_producto por ubicacion:")
prom = df.groupby("ubicacion")["ventas_producto"].mean()
print(prom)
print("Diferencia (pasillo - habitual):", prom["pasillo_principal"] - prom["habitual"])

# TODO 3: imprime el número de registros por grupo (value_counts)
print("\nRegistros por grupo:")
print(df["ubicacion"].value_counts())

# TODO 4: escribe 2–3 líneas de interpretación (sección 9 de la plantilla):
#         por qué con 4 filas no se puede concluir y qué le faltaría al análisis
print("\nInterpretacion:")
print("- Son 4 tiendas distintas en una sola semana: ninguna se mide en las dos ubicaciones,")
print("  asi que la diferencia puede venir de la tienda y no del pasillo.")
print("- Guayaquil Centro tenia promocion simultanea, eso infla el promedio del pasillo.")
print("- Faltaria correr el protocolo completo (10 tiendas x 4 semanas) y hacer un analisis pareado.")


# ---------------------------------------------------------------
# Simulación del experimento y análisis pareado (material complementario)
# Datos ficticios, solo sirven para probar que el análisis funciona
# ---------------------------------------------------------------
tiendas = ["Quito Norte", "Quito Sur", "Guayaquil Centro", "Guayaquil Norte",
           "Cuenca Centro", "Cuenca Sur", "Ambato Centro", "Manta", "Loja", "Machala"]
semanas = [1, 2, 3, 4]

# --- Diseño: sorteo de la condición inicial de cada tienda (con semilla) ---
rng = np.random.default_rng(1234597)
primera = rng.choice(["pasillo_principal", "habitual"], size=len(tiendas))

filas = []
for tienda, cond in zip(tiendas, primera):
    otra = "habitual" if cond == "pasillo_principal" else "pasillo_principal"
    for s in semanas:
        filas.append({"tienda": tienda, "semana": s,
                      "ubicacion": cond if s % 2 == 1 else otra})
diseno = pd.DataFrame(filas)

# corrida del sorteo (seccion 5)
print("\n=== Sorteo de la condicion inicial (semilla 1234597) ===")
print("Tienda            | Semanas 1 y 3      | Semanas 2 y 4")
for tienda, cond in zip(tiendas, primera):
    otra = "habitual" if cond == "pasillo_principal" else "pasillo_principal"
    print(f"{tienda:<17} | {cond:<18} | {otra}")
print("Empiezan en pasillo:", list(primera).count("pasillo_principal"))
print("Empiezan en habitual:", list(primera).count("habitual"))

# --- Simulación de ventas (datos ficticios, solo para probar el análisis) ---
rng = np.random.default_rng(1234598)
efecto_tienda = dict(zip(tiendas, rng.normal(1100, 120, len(tiendas))))
efecto_semana = {1: 0, 2: 30, 3: 60, 4: 90}

diseno["ventas_producto"] = (
    diseno["tienda"].map(efecto_tienda)
    + diseno["semana"].map(efecto_semana)
    + (diseno["ubicacion"] == "pasillo_principal") * 220
    + rng.normal(0, 90, len(diseno))
).round(0).astype(int)

# Promoción simultánea registrada (confusor)
diseno["promocion_simultanea"] = "no"
mask = (diseno["tienda"] == "Guayaquil Centro") & (diseno["semana"] == 1)
diseno.loc[mask, "promocion_simultanea"] = "si"
diseno.loc[mask, "ventas_producto"] += 180

diseno.to_csv("plantillas/resultado_simulacion (2).csv", index=False)

# --- Análisis pareado: una fila por tienda ---
piv = diseno.groupby(["tienda", "ubicacion"])["ventas_producto"].mean().unstack()
piv["diferencia"] = piv["pasillo_principal"] - piv["habitual"]
print("\n=== Simulacion: 10 tiendas x 4 semanas = 40 registros ===")
print(piv.round(1))

n = len(piv)
media = piv["diferencia"].mean()
dev = piv["diferencia"].std(ddof=1)
print(f"\nMedia de la diferencia: {media:.2f}")
print(f"Desviación estándar: {dev:.2f}")

t_crit = stats.t.ppf(0.975, df=n - 1)
ic_inf = media - t_crit * dev / n ** 0.5
ic_sup = media + t_crit * dev / n ** 0.5
print(f"IC 95% = [{ic_inf:.2f}, {ic_sup:.2f}]")

prueba = stats.ttest_rel(piv["pasillo_principal"], piv["habitual"])
print(f"Prueba t pareada: t = {prueba.statistic:.2f}, p = {prueba.pvalue:.10f}")
