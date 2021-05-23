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


class person:
    def __init__(self, person_name, person_age, petlist):
        self.person_name = person_name
        self.age = person_age
        self.petlist =  petlist
    def show_names(self):
        for each in self.petlist:
            print('dog name: ', each.name,)
    def person_petlist(self):
        print('person name: ' ,self.person_name)
        for each in self.petlist:
            print('dog eye color:', each.eye_color)
    
info = person('nayeli', '14', [myDog, dog2, dog3])
info.show_names()
info.person_petlist()


class state:
    def __init__(self, name, capital_city, population):
        self.name = name
        self.capital_city = capital_city
        self.population = population
    def show_info(self):
        print('The state of', self.name, 'has cap. city of', self.capital_city, 'with a pop of ', self.population)
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

stateInput = input('Enter a state name in list: ')

for each in stateList:
    if stateInput == each.name:
        print(each.show_info())
    else:
        for i in range(1,2,1):

            print(i)


class shopping:
    def __init__(self, storeName, cart):
        self.storeName = storeName
        self.cart = cart
    def show_info(self):
        print(self.storeName, 'cart: ', self.cart)

info = shopping('myShop', {'plants': 15, 'hoodie': 10, 'iPhone': 200})

nameInput = input('Enter in the name of a new item: ')
priceInput = int(input('Enter in a price for item: '))


info.show_info()





