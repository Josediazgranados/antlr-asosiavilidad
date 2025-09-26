grammar ExprRight;

prog : expr EOF ;

expr
    : <assoc=right> expr '^' expr             # PowRight
    | <assoc=right> expr op=('*'|'/') expr    # MulDivRight
    | <assoc=right> expr op=('+'|'-') expr    # AddSubRight
    | INT                                     # Int
    | '(' expr ')'                            # Parens
    ;

INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;

