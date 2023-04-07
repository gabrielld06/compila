grammar tng;

expression : term ((MAIS | MENOS) term)*;

term : factor ((MULT | DIV | MOD) factor)*;

factor : number | PAR_E expression PAR_D;

atribuicao : id ATRIB (id | string | expr_bool | expression) PV;

declaracao : tipo atribuicao?;

chamada_print : PRINT PAR_E (string | id | expression | expr_bool) PAR_D PV;

chamada_input : INPUT PAR_E id PAR_D PV;

number : INTEGER        # Integer
       | FLOAT          # Float
       | IDENTIFIER     # Identifier
       ;

tipo : TIPO_INT         # TipoInt
     | TIPO_FLOAT       # TipoFloat
     | TIPO_BOOL        # TipoBool
     | TIPO_STRING      # TipoString
     ;

string : STRING; // foi necessário por causa da geração do analisador síntatico

bool : BOOL; // foi necessário por causa da geração do analisador síntatico

id : IDENTIFIER; // foi necessário por causa da geração do analisador síntatico

comando : (declaracao | atribuicao | chamada_print | chamada_input | if_bloco | for_bloco | while_bloco);

inicio : MAIN CHAVE_E (comando)* CHAVE_D EOF;

expr_bool      : term_bool (OR term_bool)*;
term_bool      : factor_bool (AND factor_bool)*;
factor_bool    : NOT? (cond | PAR_E expr_bool PAR_D);
cond           : (expression OP_LOGICO expression) | bool | id;

// if
if_bloco  : IF PAR_E expr_bool PAR_D CHAVE_E (comando)* CHAVE_D else_bloco?;

// else
else_bloco : ELSE (if_bloco | CHAVE_E (comando)* CHAVE_D);

// for
for_bloco : FOR PAR_E (declaracao | atribuicao)? expr_bool PV (it=atribuicao)? PAR_D CHAVE_E (comando)* CHAVE_D;

// while
while_bloco : WHILE PAR_E expr_bool PAR_D CHAVE_E (comando)* CHAVE_D;

// Palavras-chave
IF             : 'if';
ELSE           : 'else';
FOR            : 'for';
WHILE          : 'while';
RETURN         : 'return';
PRINT          : 'print';
INPUT          : 'input';
TIPO_INT       : 'int';
TIPO_STRING    : 'string';
TIPO_FLOAT     : 'float';
TIPO_BOOL      : 'bool';
MAIN           : 'main';

// Operadores aritméticos
MAIS      : '+';
MENOS     : '-';
MULT      : '*';
DIV       : '/';
MOD       : '%';
INC       : '++';
DEC       : '--';
ATRIB     : '=';

// Operadores lógicos
OP_LOGICO : MENOR | MAIOR | MENOR_IG | MAIOR_IG | IGUAL | N_IGUAL;
MENOR     : '<';
MAIOR     : '>';
MENOR_IG  : '<=';
MAIOR_IG  : '>=';
IGUAL     : '==';
N_IGUAL   : '!=';
AND       : 'and' | '&&';
OR        : 'or' | '||';
NOT       : 'not' | '!';

// Delimitadores
PAR_E     : '(';
PAR_D     : ')';
CHAVE_E   : '{';
CHAVE_D   : '}';
PV        : ';';
VIRG      : ',';
PONTO     : '.';

// Tipos
INTEGER             : [0-9]+;
FLOAT               : [0-9]+ '.' [0-9]* | '.' [0-9]+;
BOOL                : 'True' | 'False';
IDENTIFIER          : [a-zA-Z][a-zA-Z0-9_]*;
STRING              : '"' ( CHAR_ESP | ~('\\'|'"') )* '"'; // aceita todos os caracteres exceto \ e "
fragment CHAR_ESP   : '\\' [tnr"'\\]; // CHAR_ESP pode ser \t, \n, \r, '\"' e \\

// Ignora espaços brancos
WS             : [ \t\n\r]+ -> skip;
LINECOMMENT    : ('//' | '#') ~[\r\n]* -> skip;
BLOCKCOMMENT   : '/*' .*? '*/' -> skip;