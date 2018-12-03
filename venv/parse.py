import ply.lex as lex
import ply.yacc as yacc
import Console as console
import Behaviour as behaviour
import Objects as objects

def createObject(type, attrs, objs):
    if(type == 'Object'):
        return objects.Object(attrs[0], attrs[1], attrs[2], attrs[3], attrs[4])
    elif (type == 'Player'):
        return objects.Character(attrs[0], attrs[1], attrs[2], attrs[3], attrs[4])
    elif (type == 'Mobs'):
        return objects.Mobs(attrs[0], attrs[1], attrs[2], attrs[3], attrs[4])
    elif (type == 'Level'):
        return console.Level(attrs[0], objs) # Len = 1 Behaviour is 6

tokens = ['TYPENAME', 'LPAREN', 'RPAREN', 'COMMA', 'INT', 'FLOAT', 'DELIMITER', 'ID', 'DOUBLEPOINT', 'WHITESPACE', 'BOOL', 'LEVEL']

reserved = {
    'Frame':'TYPENAME',
    'Player':'TYPENAME',
    'Object':'TYPENAME',
    'Level':'LEVEL',
    'Behaviour' : 'TYPENAME',
    'Mobs' : 'TYPENAME',
    'True' : 'BOOL',
    'False' : 'BOOL',
    'end':'DELIMITER'
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

def t_ID(t):
    r'[a-zA-Z\./]+'
    t.type = reserved.get(t.value, 'ID')
    if(t.type == 'BOOL'):
        if(t.value == 'True'):
            t.value = True
        else:
            t.value = False
    return t

lexer = lex.lex()

def p_main(p):
    '''
    P2D : levellist
    '''
    head = None
    if(len(p[1]) != 0):
        head = console.Node(p[1][0], None)
        current = head
        i = 1;
        while(i<len(p[1])):
            current.set_next(console.Node(p[1][i], None))
            current = current.get_next()

    console.current = head
    console.Console().run()

def p_levellist(p):
    '''
    levellist : level levellist
            | level
    '''
    try:
        p[0] = [p[1]]+p[2]
    except:
        p[0] = [p[1]]

def p_level(p):
    '''
    level : LEVEL LPAREN listattr RPAREN DOUBLEPOINT typelist DELIMITER
    '''

    if(not checkAttributes('Level', p[3])):
        raise Exception('Invalid attributes for type Level')
    p[0] = console.Level(p[3][0], p[6])

def p_main_expression(p):
    '''
    P2D : typelist
    '''
    print("List containing all objects. Each object has (type, list of arguments, list of objects created below if any). List of objects is recursive")
    print(p[1])


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
    if not checkAttributes(p[1], p[3]):
         raise Exception('Invalid attributes for type', p[1])
    try:
        p[0] = createObject(p[1], p[3], p[6])
    except:
        p[0] = createObject(p[1], p[3], 0)

def p_simpletypedeclar(p):
    '''
    simpletypedeclar : TYPENAME LPAREN listattr RPAREN
    '''
    if(p[1] != 'Behaviour'):
        raise Exception('Invalid entity for outer entity')

    if(not checkAttributes('Behaviour', p[3])):
        raise Exception('Invalid attributes for type Behaviour')
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
    p[0] = list()


def run(p):
    if type(p) == tuple:
        print('Tuple found')
        if p[0] == 'Frame':
            #Code Goes Here
            print('Frame Code!')
    else: print('No Code')

def checkAttributes(type, listOfAttributes):
    print('Checking.../n')
    print(type + ' Found...')

    if(type == 'Player' or type == 'Object' or type == 'Mobs') :
        print('Checking Player Len')
        if (len(listOfAttributes) == 5):
            print('Checking Player x')
            if isinstance( listOfAttributes[0] , int) != True :
                print('x failed')
                return False
            print('Checking Player y')
            if isinstance( listOfAttributes[1] , int) != True:
                return False
            print('Checking Player Dynamic')
            if isinstance( listOfAttributes[2] , bool) != True:
                return False
            print('Checking Player Icon')
            if isinstance( listOfAttributes[3] , str) != True:
                print(str(listOfAttributes[3].__class__.__name__))
                print('icon failed')
                return False
            print('Checking Player Behaviour')
            print(str(listOfAttributes[4].__class__.__name__))
            if (isinstance(listOfAttributes[4], behaviour.Behaviour) != True):
                print(str(listOfAttributes[4].__class__.__name__))
                print('Player Check Failed')
                return False
        else:
            print('Player Check Failed end')
            return False



    if(type == 'Frame'):
        #print('Frame Found...\n')
        print('List has length ' + str(len(listOfAttributes)))
        if(len(listOfAttributes) == 2):
            print('Checking Frame: ' + str(listOfAttributes[0]) + ' ' + str(listOfAttributes[1]))
            if (isinstance(listOfAttributes[0],int)) == False:
                return False
            if (isinstance(listOfAttributes[1],int)) == False:
                print('False Found')
                return False
        else:
            return False
    if(type == 'Level'):
        if (len(listOfAttributes) == 1):
            if isinstance(listOfAttributes[0], str) != True:
                    print('Level Name check Failed')
                    return False
        else:
            return false

    if (type == 'Behaviour'):
        if (len(listOfAttributes) == 6):
            if isinstance(listOfAttributes[0], int) != True:
                return False
            if isinstance(listOfAttributes[1], int) != True:
                return False
            if isinstance(listOfAttributes[2], float) != True:
                return False
            if isinstance( listOfAttributes[3] , str) != True and (listOfAttributes[3] == 'LOOP' or listOfAttributes[3] == 'CONTINUOUS' or listOfAttributes[3] == 'DEFAULT'):
                return False
            if isinstance( listOfAttributes[4] , bool) != True:
                return False
        else:
            return False
    return True


parser = yacc.yacc(debug=1)

filename = input('File: ')

file = open(filename, 'r')

s = ''
for line in file:
    s+=line

parser.parse(s)
lexer.input(s)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)







