import ply.lex as lex
import sys

# list of tokens
tokens = (
    #Reserverd words
    'AS',
    'ECHO',
    'GLOBAL',
    'STATIC',
    'CONST',
    'PRINT',
    'STRLEN',
    'FUNCTION',
    'RETURN',
    'NULL',
    'SUBSTR',
    'STRTOUPPER',
    'STRTOLOWER',
    'STRPOS',
    'PHP',
    'ID',
    'NUMBER',
    'FBOOL',
    'TBOOL',
    'STRING',
    'VOID',
    'INCLUDE'

    #Punctuation sign
    'DOLAR',                    #$
    'DOT',                      #.
    'COLON',                    #:
    'COMMA',                    #,
    'SEMICOLON',                #;
    'LPAREN',                   #(
    'RPAREN',                   #)
    'LBLOCK',                   #{
    'RBLOCK',                   #}
    'LBRACKET',                 #[
    'RBRACKET',                 #]
    'AMPERSANT',                #&
    'MODULE',                   #%
#    'RQSTION',                 #?
#    'SIMBOLS',

    #Operators
    'HASHTAG',                  ##
    'ASSIGNMENT',               #=
    'PLUS',                     #+
    'MINUS',                    #-
    'TIMES',                    #*
    'DIVIDE',                   #/
    'PLUSASSI',                 #+=
    'MINUSASSI',                #-=
    'DOTASSI',                  #.= Une cadenas
    'GREATER',                  #>
    'LESS',                     #<
    'LESSEQUAL',                #<=
    'GREATEREQUAL',             #>=
    'ISEQUAL',                  #==
    'BOOLEQUAL',                #===
    'DISTINTEQUAL',             #!=
    'PLUSPLUS',                 #++
    'MINUSMINUS',               #--
    'DISTINT',                  #!
    'AND',                      #Y
    'OR',                       #O
    'ASSIARRAY',                #=> Operador de asignacion de un tipo array

    #Structure control

    'IF',
    'ELSE',
    'DO',
    'WHILE',
    'ENDWHILE',
    'FOR',
    'FOREACH',
    'ENDFOR',
    'ENDFOREACH',
    'SWITCH',
    'CASE',
    'ENDSWITCH',
    'BREAK',
    'CONTINUE',
    'DEFAULT',

    #Class and objects

    'ARRAY',
    'CLASS',
    'PUBLIC',
    'PROTECTED',
    'PRIVATED',
    'NEW',
    'EXTENDS',
)

# Regular expressions rules for a simple tokens
t_DOT = r'\.'
t_COLON = r':'
t_COMMA = r','
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_AMPERSANT = r'\&'
t_MODULE = r'\%'
t_HASHTAG = r'\#'
t_ASSIGNMENT =  r'='             #=
t_PLUS =  r'\+'                   #+
t_MINUS =  r'-'                  #-
t_TIMES =  r'\*'                  #*
t_DIVIDE =  r'/'                 #/
t_LESS =   r'<'                  #<
t_GREATER = r'>'                 #>
t_DISTINT =  r'!'                #!
#t_RQSTION = '\?'                  #?

# Functions

def t_ID(t):
    r'\$(\w+(_\d\w)*)'
    return t

def t_DOLAR(t):
    r'\$'
    return t

#Punctuation sign

def t_ARRAY(t):
    r'array'
    return t

# Operators

def t_PHP(t):
    r'php'
    return t

def t_STRPOS(t):
    r'strpos'
    return t

def t_PLUSASSI(t):
    r'\+\='
    return t

def t_MINUSASSI(t):
    r'-='
    return t

def t_DOTASSI(t):
    r'\.\='
    return t

def t_LESSEQUAL(t):
    r'<='
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_ISEQUAL(t):
    r'=='
    return t

def t_BOOLEQUAL(t):
    r'==='
    return t

def t_DISTINTEQUAL(t):
    r'!='
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MINUSMINUS(t):
    r'--'
    return t

def t_AND(t):
    r'\&\&'
    return t

def t_OR(t):
    r'\|\|'
    return t

def t_ASSIARRAY(t):
    r'=>'
    return t


# Structure control

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_DO(t):
    r'do'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_ENDWHILEWHILE(t):
    r'endwhile'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_FOR(t):
    r'for'
    return t

def t_ENDFOREACH(t):
    r'endforeach'
    return t

def t_ENDFOR(t):
    r'endfor'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_ENDSWITCH(t):
    r'endswitch'
    return t

def t_CASE(t):
    r'case'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DEFAULT(t):
    r'default'
    return t

# Reserverd words

def t_AS(t):
    r'as'
    return t

def t_FBOOL(t):
    r'false'
    return t

def t_TBOOL(t):
    r'true'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_GLOBAL(t):
    r'global'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_CONST(t):
    r'const'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_STRLEN(t):
    r'strlen'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_NULL(t):
    r'null'
    return t

def t_SUBSTR(t):
    r'substr'
    return t

def t_STRTOUPPER(t):
    r'strtoupper'
    return t

def t_STRTOLOWER(t):
    r'strtolower'
    return t

def t_VOID(t):
    r'void'
    return t

def t_INCLUDE(t):
    r'include'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'".+"'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

def test(data, lexer):
    lexer.input(data)
    while True:
            tok = lexer.token()
            if not tok:
                break
            print (tok)

lexer = lex.lex()


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'test.c'
    f = open(fin, 'r')
    data = f.read()
    print (data)
    lexer.input(data)
    test(data, lexer)
    input()
