#Add parents to the siblings tuple to create famiy_members
parents = ('father', 'mother')
unpacked_siblings = fathers
print("Siblings:", unpacked_siblings)
print("father:", father)
print ("mother:", mother)

#Create tuples of food categories
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'spinach' ,'brocoli')
animal_products = ('milk' 'cheese', 'egg')

# Join the three tuples into one
food_stuff_tp = fruits + vegetables + animal_products

# Convert the tuple to a list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item(s)
length = len(food_stuff_lt)
mid = length // 2
if length % 2 == 0:
    middle_items = food_stuff_lt[mid - 1:mid + 1]
else:
    middle_items = [food_stuff_lt[mid]]
print("Middle item(s):", middle_items)

# Slice out the first and last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in a tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("Is 'Estonia' a nordic country?", 'Estonia' in nordic_countries)
print("Is 'Iceland' a nordic country?", 'Iceland' in nordic_countries)