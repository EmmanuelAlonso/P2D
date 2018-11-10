import ply.lex as lex
import ply.yacc as yacc

tokens = ['Object', 'Behavior', 'Frame', 'Level', 'Player', 'INT', 'FLOAT', 'LPAREN', 'RPAREN', 'COMMA']

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

def t_Object(t):

    r'\W*(Object)\W*'
    t.type = 'Object'
    return t

def t_Behavior(t):
    r'\W*(Behavior)\W*'
    return t

def t_Frame(t):
    r'\W*(Frame)\W*'
    return t

def t_error(t):
    print("Illegal character")
    t.lexer.skip(1)

lexer = lex.lex()

def p_P2D(p):

    '''
   P2D : expression
        | empty
    '''
    print(p[0])

def p_expression(p):
    '''
    expression : Object LPAREN INT
    '''
    print(p[1])
    p[0] = (p[1], p[2], P[3])

def p_empty(p):

    '''
   empty :
    '''
    p[0] = None


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






