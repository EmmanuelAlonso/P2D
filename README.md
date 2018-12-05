# P2D

This project is a programming language called P2D, which stands for platform 2D and is used to create simple 2D video games.


Reserved: Level, Player, Mob, Object, Behaviour, Goal

Tokens: TYPENAME, LPAREN, RPAREN, COMMA, INT, FLOAT, DELIMITER, ID, DOUBLEPOINT, WHITESPACE, BOOL



Grammar Rules:
P2D : levellist

levellist : level levellist 
                | level

level : LEVEL LPAREN listattr RPAREN DOUBLEPOINT typelist DELIMITER

typelist : typedeclar typelist 
                | typedeclar
 
typedeclar : TYPENAME LPAREN empty RPAREN DOUBLEPOINT typelist DELIMITER
                | TYPENAME LPAREN empty RPAREN
                | TYPENAME LPAREN listattr RPAREN DOUBLEPOINT typelist DELIMITER
                | TYPENAME LPAREN listattr RPAREN
                
simpletypedeclar : TYPENAME LPAREN listattr RPAREN

listattr : attr COMMA listattr 
                | attr
 
attr : simpletypedeclar 
                | BOOL 
                | FLOAT 
                | INT 
                | ID
                
                
                
Guide:

The language consists of declaring levels, and within those levels you declare all of the game objects that will be displayed in the level.
To finish declaring the level with all its objects, type "end" which is the delimiter.


There are four types of objects in the language:
1. Player:
    This object has WASD keys preassigned to movement, so that the player can move the character.
2. Mob:
    This object represents enemies, which will kill the player if it comes into contact with him.
3. Object:
    This represents a normal object in the game and its attributes can be customized to reflect how it behaves when it comes 
    into contact with other types.
4. Goal:
    This object represents the goal of the level. If the player touches it, the level is complete.
5. Behaviour:
    This represents the movement behavior of other objects to which it is assigned as an attribute. All preassigned movement and
    behaviors are specified with this type.


Each of these objects have to be declared inside a level and their attributes must be specified as such: Typename(atrr1, atrr2,...)
These attributes can be strings, integers, True or False, floats, or other TypeDeclarations of objects.

The attributes for each object are:
1. Player(xPosition(integer), yPosition(integer), imagePath(String), Behaviour(TypeDeclaration))
2. Mob(xPosition(integer), yPosition(integer), imagePath(String), Behaviour(TypeDeclaration))
3. Object(xPosition(integer), yPosition(integer), imagePath(String), Behaviour(TypeDeclaration))
4. Goal(xPosition(integer), yPosition(integer), imagePath(String), Behaviour(TypeDeclaration))
5. Behaviour(xMovement(integer), yMovement(integer), Speed(float), MovementCharacteristic(LOOP, CONTINUOUS, or DEFAULT), Gravity(boolean))
6. Level(Name(String))



Example Code:

Level(Classic):
  Player(60 , 525,face.png, Behaviour(5,5,5.0,DEFAULT, True))
  Object(0, 600, floor.png, Behaviour(0,0,0.0, DEFAULT, False))
  Object(420, 600, wall.png, Behaviour(0,0,0.0, DEFAULT, False))
  Object(200, 300, redplat.png, Behaviour(0,0,0.0, DEFAULT, False))
  Mob(200, 275, enemy.png, Behaviour(150,1,2.0, CONTINUOUS, True))
  Object(45, 80, purplat.png, Behaviour(0,120,2.0, LOOP, False))
  Object(200, 120, longplat.png, Behaviour(0,0,0.0, DEFAULT, False))
  Object(420, 145, longplat.png, Behaviour(0,0,0.0, DEFAULT, False))
  Object(755, 600, grplat.png, Behaviour(0,0,0.0, DEFAULT, False))
  Object(495, 400, wall.png, Behaviour(0,0,0.0, DEFAULT, False))
  Object(1000, 510, floor.png, Behaviour(0,0,0.0, DEFAULT, False))
  Mob(615, 435, enemy.png, Behaviour(150,0,2.0, LOOP, False))
  Object(590, 600, longplat.png, Behaviour(0,0,0.0, DEFAULT, False))
  Goal(750, 575, coin.png, Behaviour(0,0,0.0, DEFAULT, False))
end
Level(Dodge):
  Player(60 , 525,ufo.png, Behaviour(5,5,8.0,DEFAULT, False))
  Object(400, 600, floor.png, Behaviour(0,0,0.0, DEFAULT, False))
  Object(400, 75, floor.png, Behaviour(0,0,0.0, DEFAULT, False))
  Object(0, 525, wall.png, Behaviour(0,0,0.0, DEFAULT, False))
  Object(0, 325, wall.png, Behaviour(0,0,0.0, DEFAULT, False))
  Mob(400, 150, asteroid.png, Behaviour(0,400,3.0, LOOP, False))
  Object(0, 125, wall.png, Behaviour(0,0,0.0, DEFAULT, False))
  Object(800, 525, wall.png, Behaviour(0,0,0.0, DEFAULT, False))
  Object(800, 325, wall.png, Behaviour(0,0,0.0, DEFAULT, False))
  Object(800, 125, wall.png, Behaviour(0,0,0.0, DEFAULT, False))
  Mob(215, 420, asteroid.png, Behaviour(150,0,8.0, CONTINUOUS, False))
  Mob(515, 125, asteroid.png, Behaviour(150,0,5.0, CONTINUOUS, False))
  Mob(415, 225, asteroid.png, Behaviour(150,0,10.0, CONTINUOUS, False))
  Mob(615, 325, asteroid.png, Behaviour(150,0,5.0, CONTINUOUS, False))
  Mob(325, 500, asteroid.png, Behaviour(150,0,3.0, CONTINUOUS, False))
  Goal(710, 140, coin.png, Behaviour(0,0,0.0, DEFAULT, False))
end


HOW TO RUN:

To run your code, write it in a text file and when you run the parse python script, write the name of the file(if in same directory)
or the path to the file.
