# This Program works as a Parser. It returns the parser tree from an input of tokens created by the lexer.
# Author: Ricardo Y. Rodriguez Gonzalez
# Student ID: 802-18-2754
import ply.yacc as yacc
from my_lexer import tokens


def p_communication_function(p):
    'function : funcname LPAREN param DELIMITER param RPAREN'
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6]


def p_fucntion_name(p):
    'funcname : KEYWORD'
    p[0] = p[1]

def p_paramter(p):
    'param : ID'
    p[0] = p[1]


def p_lparen(p):
    'LPAREN : funcname DELIMITER param DELIMITER'
    p[0] = p[2]


def p_rparen(p):
    'RPAREN : DELIMITER param DELIMITER'
    p[0] = p[3]


def p_error(p):
    print("Syntax error at token", p, "line:", p.lexer.lineno)


# Build Parser
parser = yacc.yacc()

# parser
while True:
    try:
        s = input('communicate(destination, origin)')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
