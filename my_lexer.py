"""
This file has the functionality of creating tokens from an input file that contains a funtion call with parameters.

Author: Ricardo Y. Rodriguez Gonzalez
Student ID: 802-18-2754
"""
import ply.lex as lex

tokens = (
    'DIGIT',
    'ALPHA',
    'DELIMITER',
    'ID',
    'KEYWORD',
)

t_DIGIT = r'([0-9])'
t_ALPHA = r'([_A-Za-z])'
t_DELIMITER = r'\(|\)|\[|\]|,|;'
t_ignore = '\t'
t_ignore_COMMENT = r'\#.'
t_ignore_WHITESPACE = r'\s+'

keywords = {
    'communicate': 'KEYWORD',
    'my_func': 'KEYWORD',
}


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID')
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build Lexer
lexer = lex.lex()
