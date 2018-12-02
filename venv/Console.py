import pygame
import Objects
import Behaviour
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

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("platform.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = 4*HEIGHT / 5

#current = level_list = Node("def","def")

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
    def get_objects(self):
        return self.listOfObjects
    def get_size(self):
        return len(self.listOfObjects)
    def updateObjects(self):
        for obj in self.listOfObjects:
            obj.update()


def fill_levels(node,argumentos_del_leve):
    current = node
    #print(len(argumentos_del_leve))
    for index in range(len(argumentos_del_leve)):
        holder = current
        current = Node(Level((" level "+str(index)), argumentos_del_leve[index]), current)
        holder.set_next(current)
    return node
#inicio del juego

#current = level_list = fill_levels(level_list,[["player",1,2,3,"false","algo.img", "Behaviour(1,1,30,false,false,true"],["object",1,2,4,"false","block.img", "Behaviour(0,0,0,false,false,false)"], ["object",1,2,6,"false","block.img", "Behaviour(0,0,0,false,false,false)"]])
# beehaviour = Behaviour.Behaviour(10,0,1,False,False,False)
# objeto = [Objects.Object(800,800,True,"venv/face.png",beehaviour),Objects.Object(100,10,True,"venv/face.png",beehaviour),Objects.Object(200,20,True,"venv/face.png",beehaviour)]
# level = Level("Test 1",objeto)
current = None
class Console:

    def __init__(self):
        pass

    def collision_player_object(self,player,object):
        player_xr=player.get_x()+player.get_image().get_rect().size[0]
        player_xl=player.get_x()
        player_yu=player.get_y()
        player_yd=player.get_y()+player.get_image().get_rect().size[1]
        object_xr=object.get_x()+object.get_image().get_rect().size[0]
        object_xl=object.get_x()
        object_yu = object.get_y()
        object_yd=object.get_y()+object.get_image().get_rect().size[1]
        print("=============================CODE========================================")
        print (player_xr >= object_xl and player_xl <= object_xr)
        print (player_yd >= object_yu and player_yu <= object_yd)
        # print("{} {}".format(player_xr, object_xl))
        # print("P_xr-)_xl")
        # print("{} {}".format(player_xl, object_xr))
        # print("P_xl-)_xr")
        # print("{} {}".format(player_yd, object_yu))
        # print("P_yd-)_yu")
        # print("{} {}".format(player_yu, object_yd))
        # print("P_yu-)_yd")
        if (player_xr >= object_xl and player_xl <= object_xr) and (player_yd >= object_yu and player_yu <= object_yd):
            #if(player.get_x()<object.get_x() ):
               # return 0
            #if player.get_x()>object.get_x() :
                #return 1
            if player.get_y()>object.get_y() :
                return 2
            if player.get_y()<object.get_y() :
                return 3


        return -1
       # print("size: ")
        #print(current.get_value().get_objects()[0].get_image().get_rect().size[0])

    def collision(self,objects):
        player = "lechuga"
        for index in range(len(objects)):
            if objects[index].get_type()=="character":
               player = objects[index]
        print(player)
        if player != "lechuga":
            for index in range(len(objects)):
                if(player != objects[index]  ):
                    return  self.collision_player_object(player, objects[index])
        return -1



    def add_sprites(self,current, all_sprites):

        print("adding sprites to group")
        print(len(current.get_value().get_objects()))

        for index in range(len(current.get_value().get_objects())):
            print((current.get_value().get_objects()[index].get_x()))
            all_sprites.add(current.get_value().get_objects()[index])

        return all_sprites

    def run(self):
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Moving Test")
        clock = pygame.time.Clock()

        all_sprites = pygame.sprite.Group()
        plats = pygame.sprite.Group()
        platform = Platform()


        all_sprites=self.add_sprites(current, all_sprites)
        all_sprites.add(platform)
        #plats.add(platform)
        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            all_sprites.update()
            screen.fill(BLUE)
            all_sprites.draw(screen)
            print (self.collision(current.get_value().get_objects()))

            pygame.display.flip()

        pygame.quit()
        #funciones para modificar el display de los levels

        #dibuja el level



    #moverse entre los levels
    def update_level(level_list):
         pass


