import Behaviour
import pygame
class Object(pygame.sprite.Sprite):

    def __init__(self, x, y, dynamic, image, behaviour):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speedx = 0
        self.speedy = 0
        self.dynamic = dynamic
        self.image_link = image
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.rect = self.image.get_rect()
        self.behaviour = behaviour
        self.reflected = False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dynamic(self):
        return self.dynamic

    def get_image(self):
        return self.image_link

    def get_behaviour(self):
        return self.behaviour

    def set_y(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_dynamic(self, dynamic):
        self.dynamic = dynamic

    def set_image(self, image):
        self.image_link = image

    def set_behaviour(self, behaviour):
        self.behaviour = behaviour

    def update(self):
        # x movement
        if not behaviour.get_x() == 0 and behaviour.get_dynamic() and not self.reflected:
            self.rect.x += behaviour.get_speed()
            self.totalMovement += behaviour.get_speed()
            if behaviour.get_x() < self.totalMovement:
                self.rect.x -= self.totalMovement - behaviour.get_x()
                self.totalMovement = behaviour.get_x()
                if behaviour.get_reflect():
                    self.reflected = True
        elif not behaviour.get_x() == 0 and behaviour.get_dynamic() and self.reflected:
            self.rect.x -= behaviour.get_speed()
            self.totalMovement += behaviour.get_speed()
            if behaviour.get_x() < self.totalMovement:
                self.rect.x += self.totalMovement - behaviour.get_x()
                self.totalMovement = behaviour.get_x()
                if behaviour.get_reflect():
                    self.reflected = False
        if behaviour.get_repeat() and self.totalMovement == behaviour.get_x():
            self.totalMovement = 0

            # y movement
            if not behaviour.get_y() == 0 and behaviour.get_dynamic() and not self.reflected:
                self.rect.y += behaviour.get_speed()
                self.totalMovement += behaviour.get_speed()
                if behaviour.get_y() < self.totalMovement:
                    self.rect.y -= self.totalMovement - behaviour.get_y()
                    self.totalMovement = behaviour.get_y()
                    if behaviour.get_reflect():
                        self.reflected = True
            elif not behaviour.get_y() == 0 and behaviour.get_dynamic() and self.reflected:
                self.rect.y -= behaviour.get_speed()
                self.totalMovement += behaviour.get_speed()
                if behaviour.get_y() < self.totalMovement:
                    self.rect.y += self.totalMovement - behaviour.get_y()
                    self.totalMovement = behaviour.get_y()
                    if behaviour.get_reflect():
                        self.reflected = False
            if behaviour.get_repeat() and self.totalMovement == behaviour.get_y():
                self.totalMovement = 0



class Character(pygame.sprite.Sprite):
    
    def __init__(self, x, y, dynamic, image, behaviour):
        pygame.sprite.Sprite.__init__(self)
        self.properties = Object(x, y, dynamic, image, behaviour)
        self.sprite = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.rect = self.image.get_rect()
        self.canJump = True


    def get_properties(self):
        return self.properties

    def set_properties(self, x, y, dynamic, image, behaviour):
        self.properties = Object(x, y, dynamic, image, behaviour)

    def update(self):
        keystate = pygame.key.get_pressed()
        #x movement
        if keystate[pygame.K_a] and not self.properties.get_behaviour().get_x() == 0:
            self.properties.speedx += -1
            if self.properties.speedx > self.properties.get_behaviour().get_speed():
                self.properties.speedx = self.properties.get_behaviour().get_speed()
        if keystate[pygame.K_d] and not self.properties.get_behaviour().get_x() == 0:
            self.properties.speedx += 1
        if (not keystate[pygame.K_a] and not keystate[pygame.K_d]) or (keystate[pygame.K_a] and keystate[pygame.K_d]):
            if self.properties.speedx > 0:
                self.properties.speedx -= .7
            if self.properties.speedx < 0:
                self.properties.speedx += .7
        #y movement through gravity
        if self.canJump and not self.properties.get_behaviour().get_y() == 0 and self.properties.get_behaviour().get_gravity():
            self.properties.speedy = 0
            if keystate[pygame.K_w] and self.canJump:
                self.properties.speedy = -15
                self.canJump = False
            self.properties.speedy += .5
            if self.properties.speedy > self.properties.get_behaviour().get_speed():
                self.properties.speedy = self.properties.get_behaviour().get_speed()
        #y movement through w and s
        elif not self.properties.get_behaviour().get_y() == 0:
            if keystate[pygame.K_w]:
                self.properties.speedy = -self.properties.get_behaviour().get_speed()
            if keystate[pygame.K_s]:
                self.properties.speedy = self.properties.get_behaviour().get_speed()

        self.properties.rect.x += self.properties.speedx
        self.properties.rect.y += self.properties.speedy
            
            


class Mobs(pygame.sprite.Sprite):
    def __init__(self, x, y, dynamic, image, behaviour):
        pygame.sprite.Sprite.__init__(self)
        self.properties = Object(x, y, dynamic, image, behaviour)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.totalMovement = 0;

    def get_properties(self):
        return self.properties

    def set_properties(self, x, y, dynamic, image, behaviour):
        self.properties = Object(x, y, dynamic, image, behaviour)

    def update(self):
        #x movement
        if not self.properties.get_behaviour().get_x() == 0 and self.properties.get_behaviour().get_dynamic() and not self.reflected:
            self.properties.rect.x += self.properties.get_behaviour().get_speed()
            self.totalMovement += self.properties.get_behaviour().get_speed()
            if self.properties.get_behaviour().get_x() < self.totalMovement:
                self.properties.rect.x -= self.totalMovement-self.properties.get_behaviour().get_x()
                self.totalMovement = self.properties.get_behaviour().get_x()
                if behaviour.get_reflect():
                    self.reflected = True
        elif not self.properties.get_behaviour().get_x() == 0 and self.properties.get_behaviour().get_dynamic() and self.reflected:
            self.properties.rect.x -= self.properties.get_behaviour().get_speed()
            self.totalMovement += self.properties.get_behaviour().get_speed()
            if self.properties.get_behaviour().get_x() < self.totalMovement:
                self.properties.rect.x += self.totalMovement - self.properties.get_behaviour().get_x()
                self.totalMovement = self.properties.get_behaviour().get_x()
                if self.properties.get_behaviour().get_reflect():
                    self.reflected = False
        if self.properties.get_behaviour().get_repeat() and self.totalMovement == self.properties.get_behaviour().get_x():
            self.totalMovement = 0

            # y movement
            if not self.properties.get_behaviour().get_y() == 0 and self.properties.get_behaviour().get_dynamic() and not self.reflected:
                self.rect.y += self.properties.get_behaviour().get_speed()
                self.totalMovement += self.properties.get_behaviour().get_speed()
                if self.properties.get_behaviour().get_y() < self.totalMovement:
                    self.properties.rect.y -= self.totalMovement - self.properties.get_behaviour().get_y()
                    self.totalMovement = self.properties.get_behaviour().get_y()
                    if self.properties.get_behaviour().get_reflect():
                        self.reflected = True
            elif not self.properties.get_behaviour().get_y() == 0 and self.properties.get_behaviour().get_dynamic() and self.reflected:
                self.properties.rect.y -= self.properties.get_behaviour().get_speed()
                self.totalMovement += self.properties.get_behaviour().get_speed()
                if self.properties.get_behaviour().get_y() < self.totalMovement:
                    self.properties.rect.y += self.totalMovement - self.properties.get_behaviour().get_y()
                    self.totalMovement = self.properties.get_behaviour().get_y()
                    if self.properties.get_behaviour().get_reflect():
                        self.reflected = False
            if self.properties.get_behaviour().get_repeat() and self.totalMovement == self.properties.get_behaviour().get_y():
                self.totalMovement = 0
