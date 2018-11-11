import Objects
obj = Objects.Object(300,300,False,"/obj.png","behavior")
character = Objects.Character(0,300,True,"/char.png","behavior")
mob = Objects.Mobs(100,300,True,"/mob.png","behavior")

#object tester
print("Object")
print("Coordinates:")
print(obj.get_x(), obj.get_y())
print("Dynamic? ", obj.dynamic)
print("Image location and name: ", obj.get_image())
print("Behavior: ", obj.get_behaviour())

#character tester
print("\nCharacter")
print("Coordinates:")
print(character.get_properties().get_x(), character.get_properties().get_y())
print("Dynamic? ", character.get_properties().dynamic)
print("Image name: ", character.get_properties().get_image())
print("Behavior: ", character.get_properties().get_behaviour())

#mob tester
print("\nMob")
print("Coordinates:")
print(mob.get_properties().get_x(), mob.get_properties().get_y())
print("Dynamic? ", mob.get_properties().dynamic)
print("Image name: ", mob.get_properties().get_image())
print("Behavior: ", mob.get_properties().get_behaviour())