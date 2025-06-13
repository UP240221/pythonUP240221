# Lista de edades de 10 estudiantes
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Ordenar la lista y encontrar la edad mínima y máxima
edades.sort()
edad_min = min(edades)
edad_max = max(edades)
print("Edades ordenadas:", edades)
print("Edad mínima:", edad_min)
print("Edad máxima:", edad_max)

# 2. Agregar la edad mínima y máxima nuevamente a la lista
edades.extend([edad_min, edad_max])
print("Lista con min y max agregados:", edades)

# 3. Calcular la mediana (valor del medio o promedio de los dos del medio)
edades.sort()  # Asegurarse que esté ordenada 
n = len(edades)
if n % 2 == 0:
    mediana = (edades[n//2 - 1] + edades[n//2]) / 2
else:
    mediana = edades[n//2]
print("Mediana de edades:", mediana)

# 4. Calcular el promedio (media)
promedio = sum(edades) / len(edades)
print("Promedio de edades:", promedio)

# 5. Calcular el rango (máximo - mínimo)
rango = max(edades) - min(edades)
print("Rango de edades:", rango)

# 6. Comparar valor absoluto entre (mínimo - promedio) y (máximo - promedio)
diferencia_min = abs(edad_min - promedio)
diferencia_max = abs(edad_max - promedio)
print("Diferencia entre min y promedio:", diferencia_min)
print("Diferencia entre max y promedio:", diferencia_max)

# 7. Lista de países
paises = ['China', 'Rusia', 'EEUU', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']

# Encontrar el país o países del medio
n_paises = len(paises)
if n_paises % 2 == 0:
    paises_medios = paises[n_paises//2 - 1 : n_paises//2 + 1]
else:
    paises_medios = [paises[n_paises//2]]
print("País(es) del medio:", paises_medios)

# 8. Dividir la lista en dos mitades
if n_paises % 2 == 0:
    mitad1 = paises[:n_paises//2]
    mitad2 = paises[n_paises//2:]
else:
    mitad1 = paises[:n_paises//2 + 1]
    mitad2 = paises[n_paises//2 + 1:]
print("Primera mitad:", mitad1)
print("Segunda mitad:", mitad2)

# 9. Desempaquetar los tres primeros y el resto como países escandinavos
pais1, pais2, pais3, *paises_escandinavos = paises
print("Primer país:", pais1)
print("Segundo país:", pais2)
print("Tercer país:", pais3)
print("Países escandinavos:", paises_escandinavos)