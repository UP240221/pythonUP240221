resultado = 'thirty' + 'python'
print(resultado) #output: thirty days of python 

resultado = 'coding' + 'for' + 'All'
print(resultado) #output: coding for all

company = "coding for all"

print(company) #salida: coding for all

print(len(company)) #salida: 14

print(company.upper()) #salida: coding for all

print(company.lower()) #salida: coding for all

print(company.capitalize()) #salida:coding for all 
print(company.title()) #salida:coding for all
print(company.swapcase()) #salida: coding for all
 
primera_palabra = company.split()[0]
print(primera_palabra) #salida: coding

print(company.find('coding') != -1) #salida: true
print('coding' in company) #salida: true

print(company.replace('coding','python')) #salida:python for all

cadena = 'python for everyone'
print(cadena.replace('everyone','all'))

print(company.split()) #salida: ['coding','for','all']

s = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
empresas = s.split(',')
print(empresas)

print(company[0]) #salida: C

print(len(company) - 1)  #salida: 13

print(company[10]) #salida: ' ' (espacio)

cadena = 'python for everyone'
acronimo = ''.join(palabra[0] for palabra in cadena.split())
print(acronimo) #salida: PFE

acronimo = ''.join(palabra[0] for palabra in company.split())
print(acronimo) #salida: CFA

print("Índice de 'C':", company.index("C"))  # 0
print("Índice de 'F':", company.index("F"))  # 7
frase5 = "Coding For All People"
print("Última 'l':", frase5.rfind('l'))  # 17

cadena= 'coding for all people'
print(cadena.rfinfI('1')) #salida: 19

oracion = 'you cannot end a sentece with because because because is a conjuction'
print(oracion.find('because')) # salida 31

print(oracion.rindex('because')) #salida 47

inicio = oracion.find ('because')
fin = oracion.rfind('because') + len('because')
print(oracion[inicio:fin]) #salida because because because

print(oracion.find('because')) # salida: 31

inicio = oracion.find('because')
fin = oracion.rfind('because') + len('because')
print(oracion[inicio:fin]) #salida: because because because
print(company.startswith('coding')) #salida: true

cadena = '  coding for all'
print(cadena.strip()) #salida: 'coding for all'

var1 = '30Daysof python'
var2 = 'thirty_days_of_python'
print(var1.isidentifier()) #salida: false
print(var2.isidentifier()) #salida:true

bibliotecas = ['Django','flask','bottle','pyramid','falcon']
print('#'.join(bibliotecas)) #salida 'django# flask# bottle# pyramid# falcon'

print("Estoy disfrutando e¿de este desafio.\nMe pregunto que sera lo siguiente.")

print("Nombre\t\tedad\tpais\tciudad\nasasabeneh\t250\tfinlandia\thelsinki")

radio = 10
area = 3.1416* radio ** 2
print(f"El area de un triangulo de un circulo con radio {radio}es{area}metros cuadrados.")

a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a **b }")

