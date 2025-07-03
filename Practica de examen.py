print(8+9)
print(10-9)
print(19*5)
print(100/10)
print(8**2)
print(10%100)
print(50//2)

print('Martin')
print('Aguascalientes')
print('Victoria','Brayan','Liliana')

print(type(10))
print(type(9.8))
print(type(4 -4j))
print(type['Asabeneh','python','finlandia'])
print(type('Martin'))
print(type['Victoria','Brayan','Liliana'])
print(type('Aguascalientes'))

g=19
print(9)
print(8,9)
print(10+g)
print('ola','lol','Ananin')
print("I love the videogames")
print(type['manzana','pera','melon'])
print(True)

print('distancia eclauidiana')
p1 =(2,3)
p2 =(10,8)
distancia= suma_de_cuadrados= ((p2[0]**2)+(p1[1]**2))
print('la distancia eclauidiana de los puntos',p1, "y",p2,round(distancia,2))

#Day 2 
first_name ='Martin'
last_name ='Emanuel'
country ='Aguascalientes'
city='Aguascalientes'
age ='19'
year ='2006'
is_married = 'falso'
true ='si'
is_light_on = 'si'
first_name,last_name,country,city= 'Martin','Emanuel','Aguascalientes','Aguascalientes'

print("Data types")
print("first_name:", type(first_name))
print("last_name:", type(last_name))
print("country:", type(country))
print("city:", type(age))
print("year:", type(year))
print("age:", type(age))
print("is_married:", type(is_married))
print("true:", type(true))
print("is_light_onI:", type(is_light_on))

if len(first_name) > len(last_name):
    print("first name is longer than last name")
elif len(first_name) < len(last_name):
    print("last name is longer than firs name")
else:
    print("first name and last name have equal length")


num_one = 5
num_two = 6
total = num_one + num_two
diff = num_one - num_two
product= num_one * num_two
division = num_one/num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("\nNumber Operations:")
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor division:", floor_division)

#Circle calculations
radious= 30
pi= 3.1416
area_of_circle= pi * radious ** 2 
circum_of_circle = 2 * pi* radious

#User print for radious
radious = float(input("/nEnter a radious for the circle: "))
area= pi * radious ** 2
print("Area with your radious:", area)

#Use information input
print("/nPlease enter your personal information:")
first_name= input("first name: ")
last_name= input("last name: ")
country = input("country: ")
age = input("age: ")

print("/nUser Information:")
print("first_name:", first_name)
print("last_name:", last_name)
print("country:", country)
print("age:", age)

#Python keywords
print("/nPython keywords")
help('keywords')

