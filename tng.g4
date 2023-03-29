grammar tng;

expression : term (('+'|'-') term)* ;
term       : factor (('*'|'/') factor)* ;
factor     : INTEGER | '(' expression ')' ;

INTEGER    : [0-9]+ ;
WS         : [ \t\n\r]+ -> skip ;