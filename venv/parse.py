import ply.lex as lex
import ply.yacc as yacc

tokens = ['Object', 'Behavior', 'Frame', 'Level', 'Player', 'Type', 'Icon','INT', 'FLOAT', 'LPAREN', 'RPAREN','COMMA']

t_ignore = r' '

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_OBJECT(t):

    r'\W*(Object)'
    t.type = 'Object'
    return t

def t_Behavior(t):
    r'\W*(Behavior)'
    t.type = 'Behavior'
    return t

def t_Frame(t):
    r'\W*(Frame)'
    t.type = 'Frame'
    return t

def t_Type(t):
    r'\W*(Type)'
    t.type = 'Type'
    return t

def t_Icon(t):
    r'\W*(Icon)'
    return t

def t_error(t):
    print("Illegal character")
    t.lexer.skip(1)

lexer = lex.lex()

def p_P2D(p):

    '''
   P2D : OBJECT
        | display
        | empty
    '''
    run(p[1])

def p_display(p):
    '''
    display :  Frame LPAREN INT COMMA INT RPAREN
    '''
    p[0] = (p[1], p[3], p[5])
    print(p[0])

def p_OBJECT(p):
    '''
    OBJECT : Object LPAREN INT COMMA INT COMMA INT COMMA Type COMMA Behavior RPAREN
    '''
    print(p[4])
    print(p[5])
    p[0] = (p[1], p[3], p[5], p[7], p[9], p[11])
    print(p[0])

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


#s = "Object(2"

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#print(tok)

while True:
    try:
        s= input(' ')
    except EOFError:
        break
    parser.parse(s)






