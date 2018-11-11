class Object:

    def __init__(self, x, y, dynamic, image, behaviour):
        self.x = x
        self.y = y
        self.dynamic = dynamic
        self.image = image
        self.behaviour = behaviour

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dynamic(self):
        return self.dynamic

    def get_image(self):
        return self.image

    def get_behaviour(self):
        return self.behaviour

    def set_y(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_dynamic(self, dynamic):
        self.dynamic = dynamic

    def set_image(self, image):
        self.image = image

    def set_behaviour(self, behaviour):
        self.behaviour = behaviour


class Character:
    def __init__(self, x, y, dynamic, image, behaviour):
        self.properties = Object(x, y, dynamic, image, behaviour)

    def get_properties(self):
        return self.properties

    def set_properties(self, x, y, dynamic, image, behaviour):
        self.properties = Object(x, y, dynamic, image, behaviour)


class Mobs:
    def __init__(self, x, y, dynamic, image, behaviour):
        self.properties = Object(x, y, dynamic, image, behaviour)

    def get_properties(self):
        return self.properties

    def set_properties(self, x, y, dynamic, image, behaviour):
        self.properties = Object(x, y, dynamic, image, behaviour)
