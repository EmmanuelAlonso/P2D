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
        self.behaviour = behaviour
        self.reflected = False
        self.totalMovement = 0

    def get_type(self):
        return "object"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dynamic(self):
        return self.dynamic

    def get_image(self):
        return self.image

    def get_image_link(self):
        return self.image_link

    def get_behaviour(self):
        return self.behaviour

    def set_x(self, x):
        self.x = self.rect.centerx

    def set_y(self, y):
        self.y = self.rect.bottom

    def set_dynamic(self, dynamic):
        self.dynamic = dynamic

    def set_image(self, image):
        self.image_link = image

    def set_behaviour(self, behaviour):
        self.behaviour = behaviour

    def update(self):
        # x movement
        if not self.get_behaviour().get_x() == 0 and self.dynamic and not self.reflected:
            self.rect.x += self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_x() < self.totalMovement:
                self.rect.x -= self.totalMovement - self.get_behaviour().get_x()
                self.totalMovement = self.get_behaviour().get_x()
                if self.behaviour.get_reflect():
                    self.totalMovement = 0
                    self.reflected = True
        elif not self.get_behaviour().get_x() == 0 and self.dynamic and self.reflected:
            self.rect.x -= self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_x() < self.totalMovement:
                self.rect.x += self.totalMovement - self.get_behaviour().get_x()
                self.totalMovement = self.get_behaviour().get_x()
                if self.get_behaviour().get_reflect():
                    self.totalMovement = 0
                    self.reflected = False
        if self.get_behaviour().get_repeat() and self.totalMovement == self.get_behaviour().get_x():
            self.totalMovement = 0

            # y movement
            if not self.get_behaviour().get_y() == 0 and self.dynamic and not self.reflected:
                self.rect.y += self.get_behaviour().get_speed()
                self.totalMovement += self.get_behaviour().get_speed()
                if self.get_behaviour().get_y() < self.totalMovement:
                    self.rect.y -= self.totalMovement - self.get_behaviour().get_y()
                    self.totalMovement = self.get_behaviour().get_y()
                    if self.get_behaviour().get_reflect():
                        self.reflected = True
            elif not self.get_behaviour().get_y() == 0 and self.dynamic and self.reflected:
                self.rect.y -= self.get_behaviour().get_speed()
                self.totalMovement += self.get_behaviour().get_speed()
                if self.get_behaviour().get_y() < self.totalMovement:
                    self.rect.y += self.totalMovement - self.get_behaviour().get_y()
                    self.totalMovement = self.get_behaviour().get_y()
                    if self.get_behaviour().get_reflect():
                        self.reflected = False
                self.totalMovement = 0



class Character(pygame.sprite.Sprite):

    
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
        self.totalMovement = 0
        self.canJump = True

    def get_type(self):
        return "character"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dynamic(self):
        return self.dynamic

    def get_image(self):
        return self.image

    def get_image_link(self):
        return self.image_link

    def get_behaviour(self):
        return self.behaviour

    def get_image(self):
        return self.image

    def set_x(self, x):
        self.x = self.rect.centerx

    def set_y(self, y):
        self.y = self.rect.bottom

    def set_dynamic(self, dynamic):
        self.dynamic = dynamic

    def set_image_link(self, image_link):
        self.image_link = image_link

    def set_image(self,image):
        self.image = image

    def set_behaviour(self, behaviour):
        self.behaviour = behaviour

    def update(self):
        keystate = pygame.key.get_pressed()
        #x movement
        if keystate[pygame.K_a]:
            self.speedx += -1
            if self.speedx < -self.get_behaviour().get_speed():
                self.speedx = -self.get_behaviour().get_speed()
        if keystate[pygame.K_d] and not self.get_behaviour().get_x() == 0:
            self.speedx += 1
            if self.speedx > self.get_behaviour().get_speed():
                self.speedx = self.get_behaviour().get_speed()
        if (not keystate[pygame.K_a] and not keystate[pygame.K_d]) or (keystate[pygame.K_a] and keystate[pygame.K_d]):
            if self.speedx > 0:
                self.speedx -= .7
            if self.speedx < 0:
                self.speedx += .7
        #y movement through gravity
        if not self.get_behaviour().get_y() == 0 and self.get_behaviour().get_gravity():
           #self.speedy = 0
            if keystate[pygame.K_w] and self.canJump:
                self.speedy = -15
                #self.canJump = False
            self.speedy += .5
            if self.speedy > self.get_behaviour().get_speed():
                self.speedy = self.get_behaviour().get_speed()
        #y movement through w and s
        elif not self.get_behaviour().get_y() == 0 and not self.get_behaviour().get_gravity():
            if keystate[pygame.K_w]:
                self.speedy = -self.get_behaviour().get_speed()
            if keystate[pygame.K_s]:
                self.speedy = self.get_behaviour().get_speed()
            if (not keystate[pygame.K_w] and not keystate[pygame.K_s]) or (keystate[pygame.K_w] and keystate[pygame.K_s]):
                self.speedy = 0;

        self.rect.x += self.speedx
        self.rect.y += self.speedy
            
            


class Mobs(pygame.sprite.Sprite):
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
        self.totalMovement = 0
        self.canJump = True

    def get_type(self):
        return "mob"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dynamic(self):
        return self.dynamic

    def get_image_link(self):
        return self.image_link

    def get_image(self):
        return self.image

    def get_behaviour(self):
        return self.behaviour

    def set_x(self, x):
        self.x = self.rect.centerx

    def set_y(self, y):
        self.y = self.rect.bottom

    def set_dynamic(self, dynamic):
        self.dynamic = dynamic

    def set_image_link(self, image):
        self.image_link = image

    def set_behaviour(self, behaviour):
        self.behaviour = behaviour

    def update(self):
        # x movement
        if not self.get_behaviour().get_x() == 0 and self.dynamic and not self.reflected:
            self.rect.x += self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_x() < self.totalMovement:
                self.rect.x -= self.totalMovement - self.get_behaviour().get_x()
                self.totalMovement = self.get_behaviour().get_x()
                if self.behaviour.get_reflect():
                    self.totalMovement = 0
                    self.reflected = True
        elif not self.get_behaviour().get_x() == 0 and self.dynamic and self.reflected:
            self.rect.x -= self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_x() < self.totalMovement:
                self.rect.x += self.totalMovement - self.get_behaviour().get_x()
                self.totalMovement = self.get_behaviour().get_x()
                if self.get_behaviour().get_reflect():
                    self.totalMovement = 0
                    self.reflected = False
        if self.get_behaviour().get_repeat() and self.totalMovement == self.get_behaviour().get_x():
            self.totalMovement = 0

            # y movement
            if not self.get_behaviour().get_y() == 0 and self.dynamic and not self.reflected:
                self.rect.y += self.get_behaviour().get_speed()
                self.totalMovement += self.get_behaviour().get_speed()
                if self.get_behaviour().get_y() < self.totalMovement:
                    self.rect.y -= self.totalMovement - self.get_behaviour().get_y()
                    self.totalMovement = self.get_behaviour().get_y()
                    if self.get_behaviour().get_reflect():
                        self.reflected = True
            elif not self.get_behaviour().get_y() == 0 and self.dynamic and self.reflected:
                self.rect.y -= self.get_behaviour().get_speed()
                self.totalMovement += self.get_behaviour().get_speed()
                if self.get_behaviour().get_y() < self.totalMovement:
                    self.rect.y += self.totalMovement - self.get_behaviour().get_y()
                    self.totalMovement = self.get_behaviour().get_y()
                    if self.get_behaviour().get_reflect():
                        self.reflected = False
                self.totalMovement = 0
