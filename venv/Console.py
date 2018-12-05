import pygame
import Objects
import Behaviour
#global variables for all classes

WIDTH = 800
HEIGHT = 600
FPS = 60

BLUE = (60, 60, 120)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

#class for storange levels
class Level:

    def __init__ (self, name = "Default", objects = []):
        self.name = name
        self.listOfObjects = objects

    def getName(self):
        return self.name

    def get_objects(self):
        return self.listOfObjects
    def get_size(self):
        return len(self.listOfObjects)
    def updateObjects(self):
        for obj in self.listOfObjects:
            obj.update()



current = "empty"
#inicio del juego


class Console:
    gameOver = False
    LevelComplete = False
    gameCompleted = False
    current = "void"

    def __init__(self):
        pass
    def set_current(self, current):
        self.current = current
    def collision_player_object(self,player,object):
        player_xr=player.get_x()+player.get_image().get_rect().size[0]
        player_xl=player.get_x()
        player_yu=player.get_y()
        player_yd=player.get_y()+player.get_image().get_rect().size[1]
        object_xr=object.get_x()+object.get_image().get_rect().size[0]
        object_xl=object.get_x()
        object_yu = object.get_y()
        object_yd=object.get_y()+object.get_image().get_rect().size[1]

        if (player_xr >= object_xl and player_xl <= object_xr) and (player_yd >= object_yu and player_yu <= object_yd):
            if player.get_y()>object.get_y() and player_xr > object_xl + 5 and player_xl<object_xr-5:
                return 2
            if player.get_y()<object.get_y()  and player_xr > object_xl + 5 and player_xl<object_xr-5:
                player.rect.y = object.rect.y - player.rect.size[1]
                return 3
            if player.get_x()<object.get_x():
                return 0
            if player.get_x()>object.get_x() :
                return 1

        return -1

    def collision(self,objects):
        player = "lechuga"
        for index in range(len(objects)):
            if objects[index].get_type()=="character":
               player = objects[index]
        if player != "lechuga":
            hasL = False
            hasR = False
            hasU = False
            hasD = False
            for index in range(len(objects)):
                if (objects[index].get_type()=="object"):

                    side = self.collision_player_object(player, objects[index])
                    if(side == 0 and not hasR):
                        hasR=True
                    if (side == 1 and not hasL):
                        hasL = True
                    if (side == 2 and not hasU):
                        hasU = True
                    if (side == 3 and not hasD):
                        hasD = True
                    if player.get_y() > HEIGHT:
                        self.gameOver = True
                    if player.get_y() <= 0:
                        hasU = True
                    if player.get_x()+player.get_image().get_rect().size[0] >= WIDTH:
                        hasR = True
                    if player.get_x() <= 0:
                        hasL = True

                elif (objects[index].get_type() == "mob"):
                    if(self.collision_player_object(player, objects[index])!=-1):
                        self.gameOver = True
                elif (objects[index].get_type() == "goal"):
                    if (self.collision_player_object(player, objects[index]) != -1):
                        print ("completed")

                        self.LevelComplete = True
            player.get_coldirection()[0] = hasR
            player.get_coldirection()[1] = hasL
            player.get_coldirection()[2] = hasU
            player.get_coldirection()[3] = hasD

        # moverse entre los levels



    def add_sprites(self, current,all_sprites):

        for index in range(len(current.get_value().get_objects())):
            all_sprites.add(current.get_value().get_objects()[index])

        return all_sprites

    def update_level(self,current ,all_sprites):
        current2 = current.get_next()
        if  current2 == None:
            self.gameCompleted =True
        else:
            current =current2
            print(current)
            all_sprites.empty()
            all_sprites = self.add_sprites(current, pygame.sprite.Group())

        return (all_sprites,current)

    def run(self):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("P2D Game")
        clock = pygame.time.Clock()

        all_sprites = pygame.sprite.Group()

        self.add_sprites(self.current, all_sprites)

        running = True
        while running:

            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            all_sprites.update()
            screen.fill(BLUE)
            all_sprites.draw(screen)
            self.collision(self.current.get_value().get_objects())
            if self.LevelComplete:
                updates_valuess=self.update_level(self.current,all_sprites)
                all_sprites=updates_valuess[0]
                self.current=updates_valuess[1]
                if self.gameCompleted:
                    all_sprites.empty()
                    screen.fill(WHITE)
                    font = pygame.font.Font(None, 36)
                    text = font.render("Game Completed", True, BLACK)
                    text_rect = text.get_rect()
                    text_x = screen.get_width() / 2 - text_rect.width / 2
                    text_y = screen.get_height() / 2 - text_rect.height / 2
                    screen.blit(text, [text_x, text_y])
                    all_sprites = self.update_level( self.current,all_sprites)
                    running = False
                self.LevelComplete = False


            if self.gameOver:
                all_sprites.empty()
                screen.fill(BLACK)
                font = pygame.font.Font(None, 36)
                text = font.render("Game Over", True, WHITE)
                text_rect = text.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 - text_rect.height / 2
                screen.blit(text, [text_x, text_y])

            pygame.display.flip()

        pygame.quit()
