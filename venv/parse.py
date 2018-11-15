import ply.lex as lex
import ply.yacc as yacc
import Behaviour as behaviour
import Console as console
import Objects as objects

def createObject(type, listOfAttributes, objectsToAdd):
    if(type == 'Behaviour'):
        return behaviour.Behaviour(listOfAttributes[0], listOfAttributes[1], listOfAttributes[2],
                                   listOfAttributes[3], listOfAttributes[4], listOfAttributes[5])
    elif(type == 'Object'):
        return objects.Object(listOfAttributes[0], listOfAttributes[1], listOfAttributes[2],
                                   listOfAttributes[3], listOfAttributes[4])
    elif(type == 'Player'):
        return objects.Character(listOfAttributes[0], listOfAttributes[1], listOfAttributes[2],
                                   listOfAttributes[3], listOfAttributes[4])
    elif(type == 'Mob'):
        return objects.Mobs(listOfAttributes[0], listOfAttributes[1], listOfAttributes[2],
                                   listOfAttributes[3], listOfAttributes[4])
    elif(type == 'Level'):
        return console.Level(listOfAttributes[0], objectsToAdd)

tokens = ['TYPENAME', 'LPAREN', 'RPAREN', 'COMMA', 'INT', 'FLOAT', 'DELIMITER', 'ID', 'DOUBLEPOINT', 'WHITESPACE', 'BOOL']

reserved = {
    'Frame':'TYPENAME',
    'Game':'TYPENAME',
    'Player':'TYPENAME',
    'Object':'TYPENAME',
    'Behaviour': 'TYPENAME',
    'Level':'TYPENAME',
    'end':'DELIMITER',
    'True': 'BOOL',
    'False': 'BOOL'
}

t_ignore = r' '
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_DOUBLEPOINT = r':'

def t_WHITESPACE(t):
    r'\s+'
    pass

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# def t_DELIMITER(t):
#     r'[a-z]+'
#     t.type = reserved.get(t.value, 'ID')
#     return t
#
# def t_TYPENAME(t):
#     r'[A-Z][a-zA-Z]*'
#     t.type = reserved.get(t.value, 'ID')
#     return t

def t_ID(t):
    r'[a-zA-Z\.]+'
    t.type = reserved.get(t.value, 'ID')
    if(t.type == 'BOOL'):
        t.value = bool(t.value)
    return t

def t_error(t):
    print(t.value)
    return t

lexer = lex.lex()

def p_main_expression(p):
    '''
    P2D : typelist
    '''
    print("List containing all objects. Each object has (type, list of arguments, list of objects created below if any). List of objects is recursive")
    print(p[1])
    #p[1] contains all the info necessary to build the game


def p_typelist(p):
    '''
    typelist : typedeclar typelist
            | typedeclar
    '''
    try:
        p[0] = [p[1]]+p[2]
    except:
        p[0] = [p[1]]

def p_typedeclar(p):
    '''
    typedeclar : TYPENAME LPAREN empty RPAREN DOUBLEPOINT typelist DELIMITER
                | TYPENAME LPAREN empty RPAREN
                | TYPENAME LPAREN listattr RPAREN DOUBLEPOINT typelist DELIMITER
                | TYPENAME LPAREN listattr RPAREN
    '''
    # if (checkAttributes(p[1], p[3])):
    #     #create instance of the class of type p[1] and supply it to p[0]
    #     #example: Object(p[3][0], p[3][1], p[3][2], p[3][3], p[3][4])
    #     pass
    try:
        p[0] = createObject(p[1], p[3], p[6])
        raise Exception("Yes")
    except:
        p[0] = createObject(p[1], p[3], p[6])
        print(p[0])
        raise Exception("Yes")

def p_simpletypedeclar(p):
    '''
    simpletypedeclar : TYPENAME LPAREN listattr RPAREN
    '''
    p[0] = behaviour.Behaviour(p[3][0], p[3][1], p[3][2], p[3][3], p[3][4], p[3][5])

def p_list_attr(p):
    '''
    listattr : attr COMMA listattr
            | attr
    '''
    try:
        p[0] = [p[1]]+p[3]
    except:
        p[0] = [p[1]]

def p_attr(p):
    '''
    attr : simpletypedeclar
        | BOOL
        | FLOAT
        | INT
        | ID
    '''
    p[0] = p[1]

def p_empty(p):

    '''
   empty :
    '''
    p[0] = None

def p_error(p):
    # raise Exception("Fucked up dude")
    print(p, "is fucked")


def run(p):
    if type(p) == tuple:
        print('Tuple found')
        if p[0] == 'Frame':
            #Code Goes Here
            print('Frame Code!')
    else: print('No Code')

parser = yacc.yacc(debug=1)

s = 'Level(hola): Player(1,2,3, True, face.png, Behaviour(1,2,3,True, True, 4))end'
parser.parse(s)
#s = "Object(2"
lexer.input(s)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

# def createObject(type, listOfAttributes, objectsToAdd):
#     if(type == 'Behaviour'):
#         return behaviour.Behaviour(listOfAttributes[0], listOfAttributes[1], listOfAttributes[2],
#                                    listOfAttributes[3], listOfAttributes[4], listOfAttributes[5])
#     elif(type == 'Object'):
#         return objects.Object(listOfAttributes[0], listOfAttributes[1], listOfAttributes[2],
#                                    listOfAttributes[3], listOfAttributes[4])
#     elif(type == 'Player'):
#         return objects.Character(listOfAttributes[0], listOfAttributes[1], listOfAttributes[2],
#                                    listOfAttributes[3], listOfAttributes[4])
#     elif(type == 'Mob'):
#         return objects.Mobs(listOfAttributes[0], listOfAttributes[1], listOfAttributes[2],
#                                    listOfAttributes[3], listOfAttributes[4])
#     elif(type == 'Level'):
#         return console.Level(listOfAttributes[0], objectsToAdd)

# while True:
#     try:
#         s= input(' ')
#     except EOFError:
#         break
#     parser.parse(s)

# def checkAttributes(type, listOfAttributes):
#     if(type == 'Object'):
#         if(len(listOfAttributes) == 5):
#             if(listOfAttributes[0] != int):
#                 return False
#             if (listOfAttributes[1] != int):
#                 return False
#             if (listOfAttributes[2] != bool):
#                 return False
#             if (listOfAttributes[3] != str):
#                 return False
#             if (listOfAttributes[0] != str):
#                 return False
#         else:
#
#     return True






