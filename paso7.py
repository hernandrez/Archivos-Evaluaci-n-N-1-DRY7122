import json

# Abrir archivo JSON
with open('archivo.json', 'r') as f:
    # Leer archivo y cargar contenido en una variable
    contenido_json = json.load(f)

# Convertir JSON a string
contenido_str = json.dumps(contenido_json)

# Imprimir string
print(contenido_str)

