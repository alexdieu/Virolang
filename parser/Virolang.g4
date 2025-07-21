// parser/Virolang.g4
grammar Virolang;

prog: stat* EOF;

stat: assignment ';';

assignment
    : ID '=' expression
    ;

expression
    : 'create' type '(' (param (',' param)*)? ')'  # createExpr
    | expression '!' expression                  # infectExpr
    | 'design' '(' (param (',' param)*)? ')'       # designExpr
    | 'load_genome' '(' param ')'                # loadGenomeExpr
    | expression 'calibrate' '(' param ')'       # calibrateExpr
    | ID                                         # idExpr
    ;

type: 'virus' | 'host' | 'population';

param: ID ':' value;

value
    : STRING
    | NUMBER
    | BOOL
    | '[' (value (',' value)*)? ']'
    | ID
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' (~["\r\n])*? '"';
NUMBER: [0-9]+ ('.' [0-9]+)?;
BOOL: 'true' | 'false';
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' .*? '\n' -> skip;
