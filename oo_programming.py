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
dog2 = dog('sparky', 'brown', 'black', 'lab', '3')
dog3 = dog('scout', 'black', 'white', 'terrier-mix', '1')
myDog.show_info()
dog2.show_info()
dog3.show_info()


class person:
    def __init__(self, name, age, petlist):
        self.name = name
        self.age = age
        self.petlist =  petlist
    def show_names(self):
        for each in self.petlist:
            print('dog name: ', each.name, 'dog age:  ', each.age)
    
info = person('nayeli', '14', [myDog, dog2, dog3])
info.show_names()
