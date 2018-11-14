
class Behaviour:
    def __init__(self, xMov, yMov, speed, repeat, reflect, gravity):
        self.xMov = xMov
        self.yMov = yMov
        self.speed = speed
        self.repeat = repeat
        self.reflect = reflect
        self.gravity = gravity

    def get_x(self):
        return self.xMov

    def get_y(self):
        return self.yMov

    def get_speed(self):
        return self.speed

    def get_repeat(self):
        return self.repeat

    def get_reflect(self):
        return self.reflect

    def get_gravity(self):
        return self.gravity

    def set_x(self, xMov):
        self.xMov = xMov

    def set_y(self, yMov):
        self.yMov = yMov

    def set_speed(self, speed):
        self.speed = speed

    def set_repaet(self, repeat):
        self.repeat = repeat

    def set_reflect(self, reflect):
        self.reflect = reflect

    def set_gravity(self, gravity):
        self.gravity = gravity
