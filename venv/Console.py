import pygame

#global variables for all classes

WIDTH = 800
HEIGHT = 600
FPS = 60

BLUE = (60, 60, 120)
GREEN = (0, 255, 0)



#para modificar el tamano del frame
class Frame:

    def changeDim(self, height, width):
        screen = pygame.display.set_mode((width, height))
        return screen

#class for storange levels
class Level:
    def __init__(self,name="Default",argumentos="argumentos"):
        self.name=name
        self.argumentos=argumentos
    def getName(self):
        return self.name



#crea un single linked list
class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

class Object(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, Type, image):

        #Spawn point (x,y)
        self.rect.centerx = xPos
        self.rect.bottom = yPos

        #Type declaration
        self.type = Type

        #Image insertion
        self.image = image

        #Behaviors



def fill_levels(node,argumentos_del_level):
    return node
#inicio del juego


level_list = Node(Level("level1","argumentos"),"2")
fill_levels(level_list,"argumentos")

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Test")
clock = pygame.time.Clock()
#funciones para modificar el display de los levels

#dibuja el level
def draw_level(level_list):
    print(" draw")
    name = level_list.getValue().getName()
    print(name)

#moverse entre los levels
def update_level(level_list):
    pass

def update(level):
    print(level)
    update_structures()
    update_player()
    update_Mobs()


def update_structures():
    print(" structure")

def update_player():
    print(" player")

def update_Mobs():
    print(" Mobs")


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLUE)
    update("current level")
    draw_level(level_list)
    pygame.display.flip()

pygame.quit()

