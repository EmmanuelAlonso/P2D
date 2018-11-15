import ply.lex as lex
import ply.yacc as yacc


tokens = ['TYPENAME', 'LPAREN', 'RPAREN', 'COMMA', 'INT', 'FLOAT', 'DELIMITER', 'ID', 'DOUBLEPOINT', 'WHITESPACE']

reserved = {
    'Frame':'TYPENAME',
    'Player':'TYPENAME',
    'Object':'TYPENAME',
    'Level':'TYPENAME',
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

def t_DELIMITER(t):
    r'[a-z]+'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_TYPENAME(t):
    r'[A-Z][a-zA-Z]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_ID(t):
    r'[a-zA-Z]+'
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
    if (checkAttributes(p[1], p[3])):
        #create instance of the class of type p[1] and supply it to p[0]
        #example: Object(p[3][0], p[3][1], p[3][2], p[3][3], p[3][4])
        pass
    try:
        p[0] = (p[1], p[3], p[6])
    except:
        p[0] = (p[1], p[3])

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
    attr : FLOAT
        | INT
        | ID
    '''
    p[0] = p[1]
# def t_OBJECT(t):
#
#     r'\W*(Object)'
#     t.type = 'Object'
#     return t
#
# def t_Behavior(t):
#     r'Behavior'
#     t.type = 'Behavior'
#     t.value = 'Behavior'
#     return t
#
# def t_Frame(t):
#     r'\W*(Frame)'
#     t.type = 'Frame'
#     return t
#
# def t_Type(t):
#     r'Type'
#     t.type = 'Type'
#     t.value = 'Type'
#     return t
#
# def t_Icon(t):
#     r'\W*(Icon)'
#     return t
#
# def t_error(t):
#     print("Illegal character")
#     t.lexer.skip(1)
#
# lexer = lex.lex()
#
# def p_P2D(p):
#
#     '''
#    P2D : OBJECT
#         | display
#         | empty
#     '''
#     run(p[1])
#
# def p_display(p):
#     '''
#     display :  Frame LPAREN INT COMMA INT RPAREN
#     '''
#     p[0] = (p[1], p[3], p[5])
#     print(p[0])
#
# def p_OBJECT(p):
#     '''
#     OBJECT : Object LPAREN INT COMMA INT COMMA INT COMMA Type COMMA Behavior RPAREN
#     '''
#     print(p[4])
#     print(p[5])
#     p[0] = (p[1], p[3], p[5], p[7], p[9], p[11])
#     print(p[0])

# def p_TYPE(p):
#     '''
#     TYPE : Type Type INT
#     '''
#     p[0] = (p[1], p[2], p[3])
#     print(p[0])

def p_empty(p):

    '''
   empty :
    '''
    p[0] = None


def run(p):
    if type(p) == tuple:
        print('Tuple found')
        if p[0] == 'Frame':
            #Code Goes Here
            print('Frame Code!')
    else: print('No Code')

parser = yacc.yacc(debug=1)

s = '''
Frame(800, 800): 
    Level():
        Object(1,2,4,5,6, hola) 
        Player(1,2,3)
    end
end
'''
parser.parse(s)
#s = "Object(2"
lexer.input(s)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

# while True:
#     try:
#         s= input(' ')
#     except EOFError:
#         break
#     parser.parse(s)

def checkAttributes(type, listOfAttributes):
    if(type == 'Object'):
        if(len(listOfAttributes) == 5):
            if(listOfAttributes[0] != int):
                return False
            if (listOfAttributes[1] != int):
                return False
            if (listOfAttributes[2] != bool):
                return False
            if (listOfAttributes[3] != str):
                return False
            if (listOfAttributes[0] != str):
                return False
    return True






