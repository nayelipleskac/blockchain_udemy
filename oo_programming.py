class dog:
    # __init__ automatically called on creation of object
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
    # method bark

    def bark(self):
        print(self.name, 'yipped')


puggles = dog('pug', 'sparky')

puggles.bark()

#1:
class shapes:
    def __init__(self, sides, name):
        self.sides = sides,
        self.name = name,

    def action(self):
        print(self.sides, self.name,)


shape1 = shapes('4', 'rectangle')
shape2 = shapes('3', 'triangle')
shape3 = shapes('0', 'circle')
shape4 = shapes('5', 'pentagon')

shape1.action()
shape2.action()
shape3.action()
shape4.action()

#2:
class dog:
    def __init__(self, name, eye_color, fur_color, breed, age):
        self.name = name
        self.eye_color = eye_color
        self.fur_color = fur_color
        self.breed = breed
        self.age = age

    def show_info(self):
        print('My dog\'s name is', self.name, 'and he is a', self.age, 'year old',
              self.breed, 'with', self.eye_color, 'eyes and', self.fur_color, 'colored fur')


myDog = dog('arty', 'brown', 'yellow', 'terrier', '5')
dog2 = dog('sparky', 'blue', 'black', 'lab', '3')
dog3 = dog('scout', 'black', 'white', 'terrier-mix', '1')

myDog.show_info()
dog2.show_info()
dog3.show_info()

#3:
class person:
    def __init__(self, person_name, person_age, petlist):
        self.person_name = person_name
        self.age = person_age
        self.petlist = petlist

    def show_names(self):
        for each in self.petlist:
            print('dog name: ', each.name,)

    def person_petlist(self):
        print('person name: ', self.person_name)
        for each in self.petlist:
            print('dog eye color:', each.eye_color)


info = person('nayeli', '14', [myDog, dog2, dog3])
info.show_names()
info.person_petlist()

#4:
class state:
    def __init__(self, name, capital_city, population):
        self.name = name
        self.capital_city = capital_city
        self.population = population

    def show_info(self):
        print('The state of', self.name, 'has cap. city of',
              self.capital_city, 'with a pop of ', self.population)
    # def city(self, stateInput):
    #     for each in stateList:
    #         if stateInput == each.name:
    #             return self.capital_city
    #             print(each.city())
    #         else:
    #             print('Sorry, that name wasn\'t in the list!')


state1 = state('California', 'Sacremento', '15000')
state2 = state('Nevada', 'Carson City', '4000')
state3 = state('Hawaii', 'Honolulu', '2000')
state4 = state('New York', 'Albany', '10500')
state5 = state('Oregon', 'Salem', '7600')

stateList = [state1, state2, state3, state4, state5]

for each in stateList:
    print(each.show_info())

# stateInput = input('Enter a state name in list: ')

# for each in stateList:
#     if stateInput == each.name:
#         print(each.show_info())
#     else:
#         print('sorry, that item is not in list!')

# #5/6:
# class store:
#     def __init__(self, storeName, cart, shoppingList):
#         self.storeName = storeName
#         self.cart = cart
#         self.shoppingList = shoppingList
#     def addCartItem(self):
#         self.cart[nameInput] = quantityInput
#     def removeCartItem(self):
#         self.cart.pop(cartNameInput)
#     def addListItem(self):
#         self.shoppingList[listNameInput] = listQuantityInput
#     def removeListItem(self):
#         self.cart.pop(listNameInput)
#     def show_info(self):
#         print(self.storeName, 'cart: ', self.cart, 'shopping list:', self.shoppingList)
    

# info = store('myShop', {'plants': 15, 'hoodie': 3, 'iPhone': 2}, {'headphones': 50, 'bag': 25, 'picture': 40, 'computer': 110, 'mouse': 35})

# userInput = input('Do you want to add or remove an item?')

# if userInput == 'add':
#     userInput2 = input('To the cart or to the list?')
#     if userInput2 == 'cart':
#         nameInput = input('Enter in the name of a new item: ')
#         quantityInput = int(input('Enter in a quantity for item: '))
#         info.addCartItem()
#     if userInput2 == 'list':
#         listNameInput = input('Enter in the name of a new item: ')
#         listQuantityInput = int(input('Enter in a quantity for item: '))
#         info.addListItem()

# if userInput == 'remove':
#     userInput2 = input('From the cart or to the list?')
#     if userInput2 == 'cart':
#         info.show_info()
#         cartNameInput = input('What item do you wish to remove from the cart?')    
#         info.addCartItem()
#     if userInput2 == 'list':
#         info.show_info()
#         listNameInput = input('What item do you wish to remove from the list?') 
#         info.addListItem()

# info.show_info()

#7:
class phoneBook:
    def __init__(self,  contacts):
        
        self.contacts = contacts
    def show_info(self):
        for each in self.contacts:
            print(each, self.contacts[each])
    def addEntry(self):
        self.contacts[nameinput] = numberInput
    def removeEntry(self):
        self.contacts.pop(nameinput)
    def getName(self):
        print(self.contacts[retrieveName])

info = phoneBook({'nayeli': '755-818-2719', 'julian': '919-200-9001', 'arty': '510-600-7437'})

choiceInput = input('add or remove contact? ')
if choiceInput == 'add':
    nameinput = input('Enter in a name: ')
    if nameinput in info.contacts:
            print('sorry, this name is already in the contacts!')
    else:
        numberInput = input('Enter in a phone number: ')
        info.addEntry()
if choiceInput == 'remove':
    nameinput = input('Enter a name to remove: ')
    if nameinput in info.contacts:
        confirm = input('Are you sure? ')
        if confirm == 'yes':
            info.removeEntry()
        if confirm == 'no':
            print('denied')
    else:
        print('this name was not in contacts')

retrieveName = input('Enter a name to retrieve: ')
if retrieveName in info.contacts:
    info.getName()

info.show_info()


#8:
class zoo:
    def __init__(self, zooName, population, food, habitat):
        self.zooName = zooName
        self.population = population
        self.food = food
        self.habitat = habitat
    def addAnimal(self):
        self.population[addName] = addPop
        self.food[addName] = addFood
        self.habitat[addName] = addHab
    def removeAnimal(self):
        self.population.pop(removeName)
        self.food.pop(removeName)
        self.habitat.pop(removeName)
    def show_info(self):
        print(self.zooName, ':')
        for each in self.population:
            # print('populations:')
            print(each + ':' , self.population[each])
        for each in self.food:
            # print('foods:')
            print(each + ':' , self.food[each])
        for each in self.habitat:
            # print('habitats:')
            print(each + ':' ,self.habitat[each])

            # print(self.zooName, self.population, self.food, self.habitat

animal1 = 'zebra'
animal2 = 'fish'
animal3 = 'red panda'

info = zoo('MyZoo', {animal1: 10, animal2: 500, animal3: 2}, {animal1: 'grass', animal2: 'insects', animal3: 'grass'} , {animal1: 'grasslands', animal2: 'pond', animal3: 'jungle'})


userInput = input('Do you want to add or remove an animal? ')

if userInput == 'add':
  addName = input('Enter in the name of a new animal: ')
  addPop = int(input('Enter in a pop value: '))
  addFood = input('Enter in a food value: ')
  addHab = input('Enter in a habitat: ')
  info.addAnimal()
if userInput == 'remove':
  for keys in info.population:
    print(keys)
  # info.show_info()
  removeName = input('What animal would you like to remove? ')
  # info.show_info()

info.show_info()

class zoo:
    def __init__(self, zooName, population, food, habitat):
        self.zooName = zooName
        self.population = population
        self.food = food
        self.habitat = habitat
    def addAnimal(self):
        self.population[addName] = addPop
        self.food[addName] = addFood
        self.habitat[addName] = addHab
    def removeAnimal(self):
        self.population.pop(removeName)
        self.food.pop(removeName)
        self.habitat.pop(removeName)
    def show_info(self):
        print(self.zooName, ':')
        for each in self.population:
            # print('populations:')
            print(each + ':' , self.population[each])
        for each in self.food:
            # print('foods:')
            print(each + ':' , self.food[each])
        for each in self.habitat:
            # print('habitats:')
            print(each + ':' ,self.habitat[each])

            # print(self.zooName, self.population, self.food, self.habitat

animal1 = 'zebra'
animal2 = 'fish'
animal3 = 'red panda'

info = zoo('MyZoo', {animal1: 10, animal2: 500, animal3: 2}, {animal1: 'grass', animal2: 'insects', animal3: 'grass'} , {animal1: 'grasslands', animal2: 'pond', animal3: 'jungle'})


userInput = input('Do you want to add or remove an animal? ')

if userInput == 'add':
  addName = input('Enter in the name of a new animal: ')
  if addName in info.population:
    print('This animal is already in the zoo!')
  else:
    addPop = int(input('Enter in a pop value: '))
    addFood = input('Enter in a food value: ')
    addHab = input('Enter in a habitat: ')
    info.addAnimal()
    info.show_info()
if userInput == 'remove':
  for keys in info.population:
    print(keys)
  removeName = input('What animal would you like to remove? ')
  if removeName not in info.population:
      print('That animal is not in the zoo!')
  info.removeAnimal()
  info.show_info()


# myDict = {'zebra': 10, 'fish': 500}
# print(myDict.keys())
# #printing keys
# for key in myDict:
#   print(key)
# #printing vals
# print(myDict['zebra'], myDict['fish'])



