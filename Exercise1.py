#Lists
names = ["Andrew", "Eve","Norah", "Laurah", "Rorlyn"]
#Removing the first name
names[0] = "Akanga"
print(names)
#Adding a sixth name
names.append("Martha")
print(names)
#inserting a name in the 3rd position
names.insert(2, "Bathel")
print(names)
#Remove a specific index element
names.pop(3)
print(names)

#Accessing elements using negative indexing
print(names[-1])

#Slicing
cars = list(("Ford Mustarg","Aston Martin Valkyrie", "Pagani Huayra", "Porsche 911", "McLaren Senna", "Koenigsegg Jesko", "Bugatti Chiron"))
print(cars[2:5])

#Copying a list
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]
copy_countries = countries.copy()
print(copy_countries)


#looping through a list
for country in  countries:
    print(country)

#Sorting a list
animal = ["Dog", "Cat", "Elephant", "Lion", "Tiger"]
#ascending
animal.sort()
print(animal)
#descending
animal.sort(reverse=True)
print(animal)

for a in animal:
    if "a" in a:
        print(a)


#Joining a list
first_names = ["Bwebale", "Akanga", "Segunja"]
Second_names= ["Grey", "Andrew", "Alma"]

Full_name = first_names + Second_names
print(Full_name)
Full_name.clear()
i=0
while i < len(first_names):
    temp = first_names[i] + " " + Second_names[i]
    Full_name.append(temp)
    i+=1

for name in Full_name:
    print(name)


#Tuples

x = ("samsung", "iphone", "tecno", "redmi")
print(x[-2])

# x[1]= "itel"
# print(x)
#Tuples are immutable so trying to update a tuple after creation will throw an error
#However, I can convert a tuple to a list, then update the list and convert it back
x = list(x)
x[1]= "itel"
x = tuple(x)
print(x)

x = list(x)
x.append("Huawei")
x = tuple(x)
print(x)

for i in x:
    print(i)

x = list(x)
x.pop(0)
x = tuple(x)
print(x)


cities = tuple(("Kampala", "Masaka", "Mbarara", "Jinja", "Gulu"))
city1, city2, *city3 = cities
print(city1)
print(city3)

print(cities[1:4])


first_names = ("Bwebale", "Akanga", "Segunja")
second_names = ("Grey", "Andrew", "Alma")   
full_names = first_names + second_names
print(full_names)

colors = ("red", "green", "blue")
print(colors*3)


thistuple = (1,3,7,8,7,5,4,6,8,5)
count = 0
for i in thistuple:
    if i == 8:
        count+=1
print(count)


#Sets
fav_drinks = set(("Smirnoff", "Tusk lite", "Nile Special"))
fav_drinks.add("Bell Lager")
fav_drinks.add("Walagi") # Atimes
print(fav_drinks)


my_set = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in my_set)

my_set.remove("kettle")
print(my_set)
#Removing an element that doesnt exist will throw an error
# however using discard() will remove an element if it exists and do nothing if it doesn't

my_set.discard("Baby cooker")
print(my_set)

for i in my_set:
    print(i)

#Can't change the values of a set once created but you can add and remove elements

sweet = {"fight", "so dirty", "but love" , "so sweet"}
sweet.add("talk so pretty")
sweet.add("but your heart got teeth")

print(sweet)

first_names = {"Bwebale", "Akanga", "Segunja"}
second_names = {"Grey", "Andrew", "Alma"}
full_names = first_names.union(second_names)



#Strings
age = 20
name = "Andrew"

print("My name is " + name + " and I am " + str(age) + " years old")
print(f"My name is {name} and I am {str(age)} years old")
print("My name is {} and I am {} years old".format(name, age))

txt = "      Hello, Uganda!     "
print(txt.strip()) # removes trailing and leading spaces

print(txt.replace("U", "V"))
#note replace() does not change the original string, it returns a new string


y = "I am proudly Ugandan"
print(y[1:4])

x = 'All "Data Scientists" are cool!'



#Dictionaries
Shoes = {
    "brand" : "Nick",
    "color" : "black",
    "size" : 41
}

print(Shoes["size"])
Shoes["brand"] = "Adidas"
print(Shoes["brand"])
Shoes["type"] = "sneakers"
print(Shoes)

for key in Shoes:
    print(key)

for key in Shoes:
    print(Shoes[key])

#looping keys and values at once
for key, value in Shoes.items():
    print(key, value)

if "size" in Shoes:
    print("ofcourse")


Shoes.pop("color")
print(Shoes)

Shoes.clear()
print(Shoes)

my_dic = {
    "name": "Andrew",
    "age": 20,
    "country": "Uganda",
    "city": "Kampala"
} 

copy_dic = my_dic.copy()
print(copy_dic)


tired = {
    "Monday": {"8am": "Tired", "9am": "Tired", "10am": "Tired"},
    "Tuesday": {"8am": "Tired", "9am": "Tired", "10am": "Tired"},
    "Wednesday": {"8am": "Tired", "9am": "Tired", "10am": "Tired"},
    "Thursday": {"8am": "Tired", "9am": "Tired", "10am": "Tired"},
    "Friday": {"8am": "Tired", "9am": "Tired", "10am": "Tired"},
    "Saturday": {"8am": "Tired", "9am": "Tired", "10am": "Tired"},
}

print(tired["Monday"]["8am"])