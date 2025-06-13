# 1. Declarar una lista vacía
lista_vacia = []

# 2. Declarar una lista con más de 5 elementos
lista_muestra = [10, 20, 30, 40, 50, 60, 70]

# 3. Obtener la longitud de la lista
longitud = len(lista_muestra)
print("Longitud de la lista:", longitud)

# 4. Obtener el primer, medio y último elemento
primer_elemento = lista_muestra[0]
elemento_medio = lista_muestra[len(lista_muestra) // 2]
ultimo_elemento = lista_muestra[-1]
print("Primer elemento:", primer_elemento)
print("Elemento medio:", elemento_medio)
print("Último elemento:", ultimo_elemento)

# 5. Declarar lista llamada datos_personales
datos_personales = ["Juan", 30, 1.75, "Casado", "Av. Siempre Viva 742"]
print("Datos personales:", datos_personales)

# 6. Declarar lista de empresas de tecnología
empresas_tecnologia = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("Empresas de tecnología:", empresas_tecnologia)

# 7. Número de empresas
print("Número de empresas:", len(empresas_tecnologia))

# 8. Imprimir primera, media y última empresa
print("Primera empresa:", empresas_tecnologia[0])
print("Empresa del medio:", empresas_tecnologia[len(empresas_tecnologia) // 2])
print("Última empresa:", empresas_tecnologia[-1])

# 9. Modificar una empresa
empresas_tecnologia[1] = "Alphabet"
print("Empresas modificadas:", empresas_tecnologia)

# 10. Agregar una empresa
empresas_tecnologia.append("Tesla")
print("Después de agregar:", empresas_tecnologia)

# 11. Insertar una empresa en el medio
empresas_tecnologia.insert(len(empresas_tecnologia) // 2, "Spotify")
print("Después de insertar en el medio:", empresas_tecnologia)

# 12. Cambiar una empresa a mayúsculas (IBM excluida)
for i in range(len(empresas_tecnologia)):
    if empresas_tecnologia[i] != "IBM":
        empresas_tecnologia[i] = empresas_tecnologia[i].upper()
        break  # Solo cambiar una
print("Después de convertir a mayúsculas:", empresas_tecnologia)

# 13. Unir las empresas con el separador "#;  "
empresas_unidas = "#;  ".join(empresas_tecnologia)
print("Empresas unidas:", empresas_unidas)

# 14. Verificar si una empresa existe
print("¿Existe 'TESLA'?:", "TESLA" in empresas_tecnologia)

# 15. Ordenar alfabéticamente
empresas_tecnologia.sort()
print("Empresas ordenadas:", empresas_tecnologia)

# 16. Invertir el orden
empresas_tecnologia.reverse()
print("Empresas en orden descendente:", empresas_tecnologia)

# 17. Cortar las primeras 3 empresas
print("Primeras 3 empresas:", empresas_tecnologia[:3])

# 18. Cortar las últimas 3 empresas
print("Últimas 3 empresas:", empresas_tecnologia[-3:])

# 19. Cortar la empresa(s) del medio
indice_medio = len(empresas_tecnologia) // 2
if len(empresas_tecnologia) % 2 == 0:
    print("Empresas del medio:", empresas_tecnologia[indice_medio - 1: indice_medio + 1])
else:
    print("Empresa del medio:", empresas_tecnologia[indice_medio])

# 20. Eliminar la primera empresa
empresas_tecnologia.pop(0)
print("Después de eliminar la primera:", empresas_tecnologia)

# 21. Eliminar la empresa del medio
indice_medio = len(empresas_tecnologia) // 2
empresas_tecnologia.pop(indice_medio)
print("Después de eliminar la del medio:", empresas_tecnologia)

# 22. Eliminar la última empresa
empresas_tecnologia.pop()
print("Después de eliminar la última:", empresas_tecnologia)

# 23. Eliminar todas las empresas
empresas_tecnologia.clear()
print("Lista después de vaciarla:", empresas_tecnologia)

# 24. Eliminar completamente la lista
del empresas_tecnologia
# print(empresas_tecnologia)  # Esto lanzará un error si se descomenta

# 25. Unir dos listas
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
pila_unida = front_end + back_end
print("Pila unida:", pila_unida)

# 26. Insertar Python y SQL después de Redux
pila_completa = pila_unida.copy()
indice_redux = pila_completa.index("Redux")
pila_completa[indice_redux + 1:indice_redux + 1] = ["Python", "SQL"]
print("Pila completa:", pila_completa)