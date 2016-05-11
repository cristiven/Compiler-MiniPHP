# -*- coding: utf-8 -*-
import ply.yacc as yacc
from miniphp_lexical import tokens
import miniphp_lexical
import os, sys

VERBOSE = 1

def p_program(p):
	'program : declaration_list'
	pass

def p_declaration_list_1(p):
	'declaration_list : declaration_list  declaration'
	pass

def p_declaration_list_2(p):
	'declaration_list : declaration'
	pass

def p_declaration(p):
	'''declaration : var_declaration
				  | fun_declaration
	'''
	pass


def p_var_declaration_1(p):
	'var_declaration : type_specifier var_declaration2 SEMICOLON'
	pass

def p_var_declaration_2(p):
	'var_declaration : type_specifier ID LBRACKET NUMBER RBRACKET SEMICOLON'
	pass

def p_var_declaration_3(p):
	'''var_declaration2 : ID COMMA var_declaration2
	                               | ID
	                               | ID ASSIGNMENT NUMBER COMMA var_declaration2
	                               | ID ASSIGNMENT NUMBER
	                               | TIMES ID COMMA var_declaration2
	                               | TIMES ID
	                               | ID ASSIGNMENT ID COMMA var_declaration2
	                               | ID ASSIGNMENT ID
	                               | COMMA
	                               | TIMES TIMES ID
	                               | TIMES TIMES ID COMMA var_declaration2
	                               | AMPERSANT ID
	                               | AMPERSANT ID COMMA var_declaration2

        '''
	pass

def p_type_specifier_2(p):
	'type_specifier : STATIC'
	pass

def p_type_specifier_3(p):
	'type_specifier : CONST'
	pass

def p_type_specifier_4(p):
	'type_specifier : TBOOL'
	pass

def p_type_specifier_5(p):
	'type_specifier : FBOOL'
	pass

def p_type_specifier_6(p):
	'type_specifier : VOID'
	pass

def p_non_type_specifier_1(p):
	'non_type_specifier : ECHO'
	pass

def p_non_type_specifier_2(p):
	'non_type_specifier : GLOBAL'
	pass

def p_non_type_specifier_3(p):
	'non_type_specifier : PRINT'
	pass

def p_non_type_specifier_4(p):
	'non_type_specifier : STRLEN'
	pass

def p_non_type_specifier_5(p):
	'non_type_specifier : FUNCTION'
	pass

def p_non_type_specifier_6(p):
	'non_type_specifier : NULL'
	pass

def p_non_type_specifier_7(p):
	'non_type_specifier : SUBSTR'
	pass

def p_non_type_specifier_8(p):
	'non_type_specifier : STRTOUPPER'
	pass

def p_non_type_specifier_9(p):
	'non_type_specifier : STRTOLOWER'
	pass

def p_non_type_specifier_10(p):
	'non_type_specifier : STRPOS'
	pass

def p_non_type_specifier_11(p):
	'non_type_specifier : PHP'
	pass

def p_non_type_specifier_12(p):
	'non_type_specifier : RETURN'
	pass


def p_fun_declaration(p):
	'fun_declaration : type_specifier ID LPAREN params RPAREN compount_stmt'
	pass

def p_fun_declaration_1(p):
	'fun_declaration : ID LPAREN params non_type_specifier RPAREN compount_stmt'
	pass

def p_params_1(p):
	'params : param_list'
	pass

def p_params_2(p):
	'params : VOID'
	pass

def p_param_list_1(p):
	'param_list : param_list COMMA param'
	pass

def p_param_list_2(p):
	'param_list : param'
	pass

def p_param_list_3(p):
	'param_list : empty'
	pass

def p_param_1(p):
	'param : type_specifier ID'
	pass

def p_param_2(p):
	'param : type_specifier ID LBRACKET RBRACKET'
	pass

def p_compount_stmt(p):
	'compount_stmt : LBLOCK local_declarations statement_list RBLOCK'
	pass

def p_local_declarations_1(p):
	'local_declarations : local_declarations var_declaration'
	pass

def p_local_declarations_2(p):
	'local_declarations : empty'
	pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	pass

def p_statement_list_2(p):
	'statement_list : empty'
	pass

def p_statement(p):
	'''statement : expression_stmt
				| compount_stmt
				| selection_stmt
				| iteration_stmt
				| return_stmt
	'''
	pass

def p_expression_stmt_1(p):
	'expression_stmt : expression SEMICOLON'
	pass

def p_expression_stmt_2(p):
	'expression_stmt : SEMICOLON'
	pass

def p_selection_stmt_1(p):
	'selection_stmt : IF LPAREN statement RPAREN statement'
	pass

def p_selection_stmt_2(p):
	'selection_stmt : IF LPAREN expression RPAREN statement ELSE statement'
	pass

def p_selection_stmt_3(p):
	'selection_stmt : SWITCH LPAREN var RPAREN statement'
	pass

def p_selection_stmt_4(p):
	'selection_stmt : CASE NUMBER COLON statement BREAK SEMICOLON'
	pass

def p_selection_stmt_5(p):
	'selection_stmt : DEFAULT COLON statement BREAK SEMICOLON'
	pass

def p_iteration_stmt_1(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN statement'
	pass

def p_iteration_stmt_2(p):
	'iteration_stmt : FOR LPAREN var_declaration2 SEMICOLON expression SEMICOLON additive_expression RPAREN statement'
	pass

def p_iteration_stmt_1(p):
	'iteration_stmt : FOREACH LPAREN expression RPAREN statement'
	pass

def p_iteration_stmt_3(p):
	'iteration_stmt : FOREACH LPAREN var_declaration RPAREN ASSIGNMENT statement ENDFOREACH'
	pass

def p_return_stmt_2(p):
	'return_stmt : RETURN SEMICOLON'
	pass

def p_return_stmt_3(p):
	'return_stmt : RETURN expression SEMICOLON'
	pass

def p_expression_1(p):
	'expression : var ASSIGNMENT expression'
	pass

def p_expression_2(p):
	'expression : simple_expression'
	pass

def p_expression_3(p):
	'expression : var ASSIGNMENT AMPERSANT ID'
	pass

def p_var_1(p):
	'var : ID'
	pass

def p_var_2(p):
	'var : ID LBRACKET expression RBRACKET'
	pass

def p_simple_expression_1(p):
	'simple_expression : additive_expression relop additive_expression'
	pass

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	pass


def p_relop(p):
	'''relop : LESS
			| LESSEQUAL
			| GREATER
			| GREATEREQUAL
			| DISTINTEQUAL
			| DISTINT
			| ISEQUAL
	'''
	pass

def p_additive_expression_1(p):
	'''additive_expression : additive_expression addop term

        '''
	pass

def p_additive_expression_2(p):
	'additive_expression : term'
	pass

def p_additive_expression_3(p):
	'additive_expression : term MINUSMINUS'
	pass

def p_additive_expression_4(p):
	'additive_expression : term PLUSPLUS'
	pass

def p_addop(p):
	'''addop : PLUS
			| MINUS
	'''
	pass

def p_term_1(p):
	'term : term mulop factor'
	pass

def p_term_2(p):
	'term : factor'
	pass

def p_mulop(p):
	'''mulop : 	TIMES
				| DIVIDE
	'''
	pass

def p_factor_1(p):
	'factor : LPAREN expression RPAREN'
	pass

def p_factor_2(p):
	'factor : var'
	pass

def p_factor_3(p):
	'factor : call'
	pass

def p_factor_4(p):
	'factor : NUMBER'
	pass

def p_call(p):
	'call : ID LPAREN args RPAREN'
	pass

def p_args(p):
	'''args : args_list
			| empty
	'''
	pass

def p_args_list_1(p):
	'args_list : args_list COMMA expression'
	pass

def p_args_list_2(p):
	'args_list : expression'
	pass

def p_empty(p):
	'empty :'
	pass

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'test.c'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Hola Jorge, no tienes errores sintacticos")
	#input()
