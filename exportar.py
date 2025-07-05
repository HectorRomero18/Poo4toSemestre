import json

# Cambia este nombre si tu archivo tiene otro
with open("json_plano_completo.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

inserts_por_tabla = {}

for registro in datos:
    modelo = registro.pop("modelo")
    app, tabla = modelo.lower().split(".")  # convierte app.Modelo a app_modelo
    tabla_sql = f"{app}_{tabla}"

    columnas = ", ".join(registro.keys())
    valores = []
    for val in registro.values():
        if val is None:
            valores.append("NULL")
        elif isinstance(val, str):
            valores.append(f"'{val.replace("'", "''")}'")
        else:
            valores.append(str(val))
    valores_str = ", ".join(valores)

    insert = f"INSERT INTO {tabla_sql} ({columnas}) VALUES ({valores_str});"

    if tabla_sql not in inserts_por_tabla:
        inserts_por_tabla[tabla_sql] = []
    inserts_por_tabla[tabla_sql].append(insert)

# Guardar todos los inserts en un archivo SQL
with open("datos_insertables.sql", "w", encoding="utf-8") as f:
    for tabla, inserts in inserts_por_tabla.items():
        f.write(f"-- Inserts para tabla {tabla}\n")
        f.write("\n".join(inserts))
        f.write("\n\n")

print("✅ Archivo SQL generado como datos_insertables.sql")
