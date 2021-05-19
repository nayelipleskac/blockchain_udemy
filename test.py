def myFunc(int_in):
    return int_in/5

if __name__ == 'main':
    print(myFunc(7))
else:
    print('test imported not invoked')

class myClass:
    oneval = 17
    def div(self, int_in):
        try:
             return int_in/self.oneval
        except TypeError:
           print('must pass integer to div!')
           return 0
        except:
            print('unknown error in div')
            return 0
    def __init__(self, inval):
        self.oneval = inval

class newClass (myClass):
    name = 'Nayeli'
    def __repr__(self):
        return self.name + ': oneval is = to ' + str(self.oneval)

C = myClass(4)
B = myClass(10)
# C.oneval = 4
print(C.oneval)
print(C.div(34))
print(B.div(34))

N = newClass(12)
# print(N.name)

print(N.div('rutebega'))

# printing N.name, which is the name variable
# newClass also has a number val of 12
# div is dividing 36, the imported number by the instantiated number 12 to get 3
print(N.div(36))
print(N)

