import pygame, time

pygame.init() 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake!!")

red= (255, 0, 0)
black = (0,0,0)


#while True:

# pygame.display.update()
# screen.fill(black)
# pygame.draw.rect(screen, red, (100, 100, 20, 20), 0)


movieDic = {'movie 1': 2, 'movie 2': 6, 'movie 3': 10}
# print(movieDic.items())
print(movieDic)
for keys in movieDic:
    if movieDic[keys] > 3:
        print(keys, ':', movieDic[keys])


animalList = ['cat', 'elephant', 'zebra', 'dog']
print(animalList)
animalList.pop()
print(animalList)

# for x in range(1,4,1):
#     for y in range(1,8,1):
#         print('*',end='')

# x=int(input('How many seconds'))
# while x > 0:
#    print(x)
#    x=x-1
#    time.sleep(1)
# print('BLAST OFF')

state = input('What state do you live in')
if state == 'California' or state == 'Oregon' or state == 'Washington' :
   print('We suggest you go for a coastal drive')
else:
   print('You may be better off skiing')

q = input('Do you have an upcoming vacation')
if q == 'yes':
   grade = int(input('What grade are you in'))
   if grade == 11:
       print('Great time to study for SAT')
   else:
       print('have fun then')
elif q == 'no':
    print('have a plesant vacation')




    
