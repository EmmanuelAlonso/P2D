import pygame

#global variables for all classes

WIDTH = 800
HEIGHT = 600
FPS = 60

BLUE = (60, 60, 120)
GREEN = (0, 255, 0)

size = 0

#crea un single linked list
class Node:

    def __init__(self,value,next):
        self.value = value
        self.next = next

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


#para modificar el tamano del frame
class Frame:

    def changeDim(self, height, width):
        screen = pygame.display.set_mode((width, height))
        return screen


current = level_list = Node("def","def")

#class for storange levels
class Level:
    # head =Node("def", "def")
    # size = 0
    def __init__ (self, name = "Default", objects = []):
        self.name = name
        self.listOfObjects = objects
    # def __init__(self,name="Default",argumentos=[]):
        # self.name=name
        # self.head = Node(argumentos, self.head)
        # current = self.head
        # #print(len(argumentos))
        # for eachValue in argumentos :
        #     #for value in eachValue:
        #         #print(value)
        #     self.size = self.size + 1
        #     holder = current
        #     current = Node(eachValue, self.head)
        #     holder.set_next(current)
        # self.argumentos=argumentos
    def getName(self):
        return self.name
    # def get_head(self):
    #     return self.head

    def updateObjects(self):
        for obj in self.listOfObjects:
            obj.update()
        pass

def fill_levels(node,argumentos_del_leve):
    current = node
    #print(len(argumentos_del_leve))
    for index in range(len(argumentos_del_leve)):
        holder = current
        current = Node(Level((" level "+str(index)), argumentos_del_leve[index]), current)
        holder.set_next(current)
    return node
#inicio del juego

current = level_list = fill_levels(level_list,[["player",1,2,3,"false","algo.img", "Behaviour(1,1,30,false,false,true"],["object",1,2,4,"false","block.img", "Behaviour(0,0,0,false,false,false)"], ["object",1,2,6,"false","block.img", "Behaviour(0,0,0,false,false,false)"]])

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Test")
clock = pygame.time.Clock()
#funciones para modificar el display de los levels

#dibuja el level
def draw_level(level_list,current,size):
    print(" draw")
    current = current.get_next()
    for x in range(0,size):
        name = current.get_value().get_head().get_value()
        print(name)
        current = current.get_next()
    current = level_list

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
    draw_level(level_list,current,3)
    pygame.display.flip()

pygame.quit()

