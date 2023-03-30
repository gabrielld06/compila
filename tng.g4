grammar tng;

expression : term ((MAIS | MENOS) term)*;

atribuicao : IDENTIFIER ATRIB (expression | STRING | BOOL | IDENTIFIER);

declaracao : tipo atribuicao;

chamada_print : PRINT PAR_E (STRING | IDENTIFIER) PAR_D;

term : factor ((MULT | DIV | MOD) factor)*;

factor : number | PAR_E expression PAR_D;

number : INTEGER | FLOAT | IDENTIFIER;

tipo : TIPO_INT | TIPO_CHAR | TIPO_FLOAT | TIPO_BOOL;

comando : (declaracao | atribuicao | chamada_print) PV;

inicio : tipo IDENTIFIER CHAVE_E (comando)* CHAVE_D;

// bool
expr_bool : expression OP_LOGICO expression;
fator_bool : NOT? (PAR_E expr_bool PAR_D | expr_bool);
cond : fator_bool ((AND | OR) fator_bool)*;

// if
if_bloco : IF PAR_E cond PAR_D CHAVE_E (comando)* CHAVE_D else_bloco?;

// else
else_bloco : ELSE (if_bloco | CHAVE_E (comando)* CHAVE_D);

// for
for_bloco : FOR PAR_E atribuicao PV cond PV atribuicao PAR_D CHAVE_E (comando)* CHAVE_D;

// while
while_bloco : FOR PAR_E cond PAR_D CHAVE_E (comando)* CHAVE_D;

// Palavras-chave
IF : 'if';
ELSE : 'else';
FOR : 'for';
WHILE : 'while';
RETURN : 'return';
PRINT : 'print';
TIPO_INT : 'int';
TIPO_CHAR : 'char';
TIPO_FLOAT : 'float';
TIPO_BOOL : 'bool';

// Operadores aritméticos
MAIS : '+';
MENOS : '-';
MULT : '*';
DIV : '/';
MOD : '%';
INC : '++';
DEC : '--';
ATRIB : '=';

// Operadores lógicos
OP_LOGICO : MENOR | MAIOR | MENOR_IG | MAIOR_IG | IGUAL | N_IGUAL;
MENOR : '<';
MAIOR : '>';
MENOR_IG : '<=';
MAIOR_IG : '>=';
IGUAL : '==';
N_IGUAL : '!=';
AND : 'and' | '&&';
OR : 'or' | '||';
NOT : 'not' | '!';

// Delimitadores
PAR_E : '(';
PAR_D : ')';
CHAVE_E : '{';
CHAVE_D : '}';
PV : ';';
VIRG : ',';
PONTO : '.';

// Tipos
INTEGER : [0-9]+;
FLOAT : [0-9]+ '.' [0-9]* | '.' [0-9]+;
BOOL : 'True' | 'False';
IDENTIFIER : [a-zA-Z][a-zA-Z0-9]*;
STRING : '"' ( CHAR_ESP | ~('\\'|'"') )* '"'; // aceita todos os caracteres exceto \ e "
fragment CHAR_ESP : '\\' [tnr"'\\]; // CHAR_ESP pode ser \t, \n, \r, '\"' e \\

// Ignora espaços brancos
WS         : [ \t\n\r]+ -> skip ;