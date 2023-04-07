from antlr4 import *
from tngVisitor import tngVisitor
from tngLexer import tngLexer
import inspect # print(inspect.getmembers(token.getTokenSource(), predicate=inspect.ismethod)) # get class methods

if __name__ is not None and "." in __name__:
    from .tngParser import tngParser
else:
    from tngParser import tngParser


# DONE (eu acho) atribuição, declaração e tratamento de expressões
#   * expressões são resolvidas se possiveis (não possuem variaveis), então já é feita uma mini otimização
#       no caso de uma expressão possuir uma variavel, é armazenado uma string com ela, no test, 
#           fon é uma expressão possivel de se resolver completamente e asdfasdf34 não
#       atribuição, declaração e tratamento de expressões booleanas
#       if, else
#       print
#       06/04:
#       exprVistor gera erro se tiver identificador não numerico (stirng / bool)
#       atribuição obedece o seguinte:
#           INT <- INT | FLOAT
#           FLOAT <- INT | FLOAT
#           BOOL <- BOOL
#           STRING <- STRING
#               gerando erro caso contrario;
#               tive que fazer um id : IDENTIFIER nas regras mesmo motivo (esse codigo ia ficar mais feio se nao tivesse, é o sacrificio);
#                   um detalhe sobre a regra, o antlr resolve redundancias pela ordem de aparencia na regra, por isso, pra identificar identificadores, id deve vir antes
#                       caso contrario consideraria os identificadores como expression
#                           -> atribuicao : IDENTIFIER ATRIB (id | expression | string | bool) PV;
#       07/04
#       precedencia booleana -> NOT | ( ) -> AND -> OR -> (OP_RELACIONAIS) ;; fazer a regra no mesmo formato da expr aritmetica deve funcionar e sem muito trabalho
#           exemplo:    True or False and False deve retornar True
#       linha e bloco de comentario
#       input de dados (cin, scan)
#       for, while
# TODO: ver se ta certo o tratamento de expressão -> parece q sim :) 
#       arquivos de testes que cobrem todos os erros && testes automatizado :3
#       otimização?
#       assembly?


class tngSemantic(tngVisitor):
    
    def __init__(self):
        self.symbolTable = {}   # {
                                # 'tipo' : str,
                                # 'value' : int | float | bool | str | None
                                # }

        self.errors = []    # {
                            # 'error' : 'Variable not declared' 
                            #         | 'Variable already declared' 
                            #         | 'Type conversion from {tipo_from} to {tipo_to} not supported' 
                            #         | 'Cannot perform arithmetic operation on non-numeric variable', 
                            # 'id'    : str,
                            # 'line'  : int,
                            # 'column': int
                            # }
        
        self.code = ""

    # Retorna se o programa deve ser compilado ou não
    def compile(self) -> bool:
        return len(self.errors) == 0

    # Insere c no codigo fonte a ser compilado
    def insertCode(self, c) -> None:
        if len(self.errors) == 0:
            self.code += c + '\n'


    '''
        EXPRESSOES ARITMETICAS
    '''

    # Visit a parse tree produced by tngParser#expression.
    # expression : term ((MAIS | MENOS) term)*;
    def visitExpression(self, ctx:tngParser.ExpressionContext) -> int | float | str | None:
        nodes = ctx.getChildCount()

        c = ctx.getChild(0)

        left = self.visit(c)
        
        if left == None: return None
        
        for i in range(1, nodes):
            c = ctx.getChild(i)

            if c.getText() == '+' or c.getText() == '-': 
                op = c.getText()
                continue

            right = self.visit(c)
            
            if right == None: return None

            if type(left) != str and type(right) != str:
                if op == '+':
                    left += right
                else:
                    left -= right
            else:
                left = f"{left}{op}{right}"

        return left
    
    # Visit a parse tree produced by tngParser#term.
    # term : factor ((MULT | DIV | MOD) factor)*;
    def visitTerm(self, ctx:tngParser.TermContext) -> int | float | str | None:
        nodes = ctx.getChildCount()

        c = ctx.getChild(0)
        left = self.visit(c)

        if left == None: return None
        
        for i in range(1, nodes):
            c = ctx.getChild(i)

            if c.getText() == '*' or c.getText() == '/' or c.getText() == '%': 
                op = c.getText()
                continue

            right = self.visit(c)

            if right == None: return None

            if type(left) != str and type(right) != str:
                if op == '*':
                    return left * right
                elif op == '/':
                    return left / right
                else:
                    return left % right
            else:
                left = f"{left}{op}{right}"

        return left

    # Visit a parse tree produced by tngParser#factor.
    # factor : number | PAR_E expression PAR_D;
    def visitFactor(self, ctx:tngParser.FactorContext) -> int | float | str | None:
        if ctx.number():
            value = self.visit(ctx.number())

            c = ctx.number().getChild(0)
            token = c.symbol
            type = tngLexer.symbolicNames[token.type]   # pega o nome do tipo do nó terminal

            if type == 'IDENTIFIER':
                if value == None: return None

                nome = value.getText()

                if self.symbolTable[nome]['tipo'] == 'int' or self.symbolTable[nome]['tipo'] == 'float':
                    return f'{value}'
                else:
                    self.errors.append({
                        'error' : 'Cannot perform arithmetic operation on non-numeric variable',
                        'id'    : nome,
                        'line'  : token.line,
                        'column': token.column
                    })

                    return None

            return value
        else:
            return self.visit(ctx.expression())


    '''
        EXPRESSOES BOOLEANAS
    '''


    # Visit a parse tree produced by tngParser#expr_bool.
    # expr_bool : term_bool (OR term_bool)*;
    def visitExpr_bool(self, ctx:tngParser.Expr_boolContext) -> str | None:
        nodes = ctx.getChildCount()

        c = ctx.getChild(0)

        left = self.visit(c)

        if left == None: return None

        for i in range(2, nodes, 2):
            c = ctx.getChild(i)

            right = self.visit(c)

            if right == None: return None

            left = left or right if type(left) == bool and type(right) == bool else f"{left if type(left) == str else ('true' if left else 'false')} or {right if type(right) == str else ('true' if right else 'false')}"

        return f"{left if type(left) == str else ('true' if left else 'false')}"


    # Visit a parse tree produced by tngParser#term_bool.
    # term_bool : factor_bool (AND factor_bool)*;
    def visitTerm_bool(self, ctx:tngParser.Term_boolContext) -> bool | str | None:
        nodes = ctx.getChildCount()

        c = ctx.getChild(0)

        left = self.visit(c)

        if left == None: return None

        for i in range(2, nodes, 2):
            c = ctx.getChild(i)

            right = self.visit(c)

            if right == None: return None

            left = left and right if type(left) == bool and type(right) == bool else f"{left if type(left) == str else ('true' if left else 'false')} and {right if type(right) == str else ('true' if right else 'false')}"

        return left


    # Visit a parse tree produced by tngParser#factor_bool.
    # factor_bool : NOT? (cond | PAR_E expr_bool PAR_D);
    def visitFactor_bool(self, ctx:tngParser.Factor_boolContext) -> bool | str | None:
        if ctx.cond():
            value = self.visit(ctx.cond())
        else:
            value = self.visit(ctx.expr_bool())

        if value == None: return None

        if type(value) == bool:
            return not value if ctx.NOT() else value
        else: 
            return f"not {value if type(value) == str else 'true' if value else 'false'}" if ctx.NOT() else value


    # Visit a parse tree produced by tngParser#cond.
    # cond : (expression OP_LOGICO expression) | bool | id;
    def visitCond(self, ctx:tngParser.CondContext) -> bool | str | None:
        if ctx.bool_():
            return self.visit(ctx.bool_())
        elif ctx.id_():
            return self.visit(ctx.id_())
        else:
            op = ctx.OP_LOGICO().getText()

            left = self.visit(ctx.expression()[0])

            if left == None: return None

            right = self.visit(ctx.expression()[1])

            if right == None: return None

            if type(left) != str and type(right) != str:
                if op == '<':
                    return left < right
                elif op == '>':
                    return left > right
                elif op == '<=':
                    return left <= right
                elif op == '>=':
                    return left >= right
                elif op == '==':
                    return left == right
                else:
                    return left != right
            else:                
                return f"{left} {op} {right}"


    '''
        BLOCOS DE COMANDO
    '''    


    # Visit a parse tree produced by tngParser#inicio.
    def visitInicio(self, ctx:tngParser.InicioContext) -> None:
        self.insertCode("#include <iostream>\nusing namespace std;\nint main(){")

        for c in ctx.comando():
            code = self.visit(c)
            if code != None: self.insertCode(code)

        self.insertCode("return 0;\n}")


    # Visit a parse tree produced by tngParser#comando.
    def visitComando(self, ctx:tngParser.ComandoContext) -> any:
        return self.visitChildren(ctx)

    
    # Visit a parse tree produced by tngParser#atribuicao.
    # atribuicao : IDENTIFIER ATRIB (id | expression | string | expr_bool) PV;
    # INT <- INT | FLOAT
    # FLOAT <- INT | FLOAT
    # BOOL <- BOOL
    # STRING <- STRING
    def visitAtribuicao(self, ctx:tngParser.AtribuicaoContext) -> str | None:
        identificador = ctx.id_()[0].IDENTIFIER()   # identificador

        nome = self.visit(ctx.getChild(0))          # nome do identificador
        
        if nome == None: return None

        token = identificador.symbol            # simbolo do identificador
        tipo = self.symbolTable[nome]['tipo']   # pega o nome do tipo do identificador

        c = ctx.getChild(2)                     # (id | expression | string | bool)
        value = self.visit(c)
        
        if value == None: return None

        try:
            if ctx.expression():    # atribuição de expressões aritmeticas
                if tipo == 'int':
                    self.symbolTable[nome]['value'] = (int(value) if type(value) != str else value)  # type(value) != str : caso de atribuição com identificador
                elif tipo == 'float':
                    self.symbolTable[nome]['value'] = (float(value) if type(value) != str else value)
                else:
                    raise Exception(f"Type conversion from numeric to {tipo} not supported")
            elif ctx.expr_bool():    # atribuição de expressões booleanas
                if tipo == 'bool':
                    if type(value) == str:
                        self.symbolTable[nome]['value'] = value
                    else:
                        self.symbolTable[nome]['value'] = 'true' if value else 'false'
                else:
                    raise Exception(f"Type conversion from numeric to {tipo} not supported")
            else:    # atribuição de string, bool ou identificador
                token_val = c.getChild(0).symbol
                tipo_val = tngLexer.symbolicNames[token_val.type]
                
                if tipo == 'string' and tipo_val == 'STRING':
                    self.symbolTable[nome]['value'] = value
                elif tipo_val == 'IDENTIFIER':
                    tipo_atr = self.symbolTable[value]['tipo']

                    if tipo == tipo_atr:
                        self.symbolTable[nome]['value'] = value
                    elif tipo == 'int' and tipo_atr == 'float':
                        self.symbolTable[nome]['value'] = (int(value) if type(value) != str else value)
                    elif tipo == 'float' and tipo_atr == 'int':
                        self.symbolTable[nome]['value'] = (float(value) if type(value) != str else value)
                    else:
                        raise Exception(f"Type conversion from {tipo_atr} to {tipo} not supported")
                else:
                    raise Exception(f"Type conversion from {tipo_val} to {tipo} not supported")
        except Exception as e:
            self.errors.append({
                'error' : str(e),
                'id'    : nome,
                'line'  : token.line,
                'column': token.column
            })

            return None
            
        return f"{nome} = {self.symbolTable[nome]['value']};"


    # Visit a parse tree produced by tngParser#declaracao.
    def visitDeclaracao(self, ctx:tngParser.DeclaracaoContext) -> str | None:
        tipo = ctx.tipo().getText()                         # int, float, bool, char ou string
        identificador = ctx.atribuicao().id_()[0].IDENTIFIER()       # identificador | pode ter dois identificadores, por isso [0] 
        nome = identificador.getText()      # nome do identificador
        token = identificador.symbol                        # simbolo do identificador

        if nome in self.symbolTable:
            self.errors.append({
                'error' : 'Variable already declared',
                'id'    : nome,
                'line'  : token.line,
                'column': token.column
            })
        else:
            self.symbolTable[nome] = {
                'tipo' : tipo,
                'value' : None
            }

        return f'{tipo} {self.visit(ctx.atribuicao())}'
    

    # Visit a parse tree produced by tngParser#chamada_print.
    # PRINT PAR_E (string | id) PAR_D PV;
    def visitChamada_print(self, ctx:tngParser.Chamada_printContext) -> str | None:

        string = self.visit(ctx.getChild(2))

        if string == None: return None

        return f"cout << {string} << endl;"
    
    
    # Visit a parse tree produced by tngParser#chamada_input.
    # chamada_input : INPUT PAR_E id PAR_D PV;
    def visitChamada_input(self, ctx:tngParser.Chamada_inputContext) -> str | None:

        identifier = self.visit(ctx.id_())

        if not identifier: return None

        return f"cin >> {identifier};"
    

    # Visit a parse tree produced by tngParser#if_bloco.
    # if_bloco : IF PAR_E expr_bool PAR_D CHAVE_E (comando)* CHAVE_D else_bloco?;
    def visitIf_bloco(self, ctx:tngParser.If_blocoContext) -> str | None:
        c = ctx.expr_bool()

        cond = self.visit(c)

        code = f"if({cond}) {{\n"

        comandos = ctx.comando()
        
        for c in comandos:
            cmd = self.visit(c)
            if cmd != None: code += cmd + '\n'

        code += f"}}"

        if ctx.else_bloco():
            code += self.visit(ctx.else_bloco())
        
        return code


    # Visit a parse tree produced by tngParser#else_bloco.
    # else_bloco : ELSE (if_bloco | CHAVE_E (comando)* CHAVE_D);
    def visitElse_bloco(self, ctx:tngParser.Else_blocoContext) -> str | None:
        if ctx.if_bloco():
            code = f" else "

            code += self.visit(ctx.if_bloco())
        else:
            code = f" else {{\n"

            comandos = ctx.comando()
            
            for c in comandos:
                cmd = self.visit(c)
                if cmd != None: code += cmd + '\n'

            code += f"}}"

        return code


    # Visit a parse tree produced by tngParser#for_bloco.
    # for_bloco : FOR PAR_E (declaracao | atribuicao)? expr_bool PV (it=atribuicao)? PAR_D CHAVE_E (comando)* CHAVE_D;
    def visitFor_bloco(self, ctx:tngParser.For_blocoContext) ->  str | None:
        inic = ';'
        it = ' '
        if ctx.declaracao() or ctx.atribuicao():
            inic = self.visit(ctx.getChild(2))
        if ctx.it:
            it = self.visit(ctx.it)
        
        expr_bool = self.visit(ctx.expr_bool())

        code = f'for({inic}{expr_bool};{it[:-1]}) {{\n'

        comandos = ctx.comando()
        for c in comandos:
            cmd = self.visit(c)
            if cmd != None: code += cmd + '\n'

        code += f'}}'

        return code


    # Visit a parse tree produced by tngParser#while_bloco.
    # while_bloco : WHILE PAR_E expr_bool PAR_D CHAVE_E (comando)* CHAVE_D;
    def visitWhile_bloco(self, ctx:tngParser.While_blocoContext) -> str | None:        
        expr_bool = self.visit(ctx.expr_bool())

        code = f'while({expr_bool}) {{\n'

        comandos = ctx.comando()
        for c in comandos:
            cmd = self.visit(c)
            if cmd != None: code += cmd + '\n'

        code += f'}}'

        return code


    '''
        TIPOS - TALVEZ REMOVER
    ''' 

    
    # Visit a parse tree produced by tngParser#TipoInt.
    def visitTipoInt(self, ctx:tngParser.TipoIntContext) -> None:
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#TipoFloat.
    def visitTipoFloat(self, ctx:tngParser.TipoFloatContext) -> None:
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#TipoBool.
    def visitTipoBool(self, ctx:tngParser.TipoBoolContext) -> None:
        return self.visitChildren(ctx)
    

    '''
        NOS TERMINAIS
    '''


    # Visit a parse tree produced by tngParser#Integer.
    def visitInteger(self, ctx:tngParser.IntegerContext) -> int:
        return int(ctx.getChild(0).getText())
    

    # Visit a parse tree produced by tngParser#string.
    def visitString(self, ctx:tngParser.StringContext) -> str:
        return str(ctx.getChild(0).getText())


    # Visit a parse tree produced by tngParser#Float.
    def visitFloat(self, ctx:tngParser.FloatContext) -> float:
        return float(ctx.getChild(0).getText())


    # Visit a parse tree produced by tngParser#id.
    def visitId(self, ctx:tngParser.IdContext) -> str | None:
        if ctx.IDENTIFIER().getText() in self.symbolTable:
            return ctx.IDENTIFIER().getText()
        else:
            self.errors.append({
                'error' : 'Variable not declared',
                'id'    : ctx.IDENTIFIER().getText(),
                'line'  : ctx.IDENTIFIER().symbol.line,
                'column': ctx.IDENTIFIER().symbol.column
            })
            return None
        
    
    # Visit a parse tree produced by tngParser#Identifier. -> desnecessario?
    def visitIdentifier(self, ctx:tngParser.IdentifierContext) -> str | None:
        if ctx.IDENTIFIER().getText() in self.symbolTable:
            return ctx.IDENTIFIER()
        else:
            self.errors.append({
                'error' : 'Variable not declared',
                'id'    : ctx.IDENTIFIER().getText(),
                'line'  : ctx.IDENTIFIER().symbol.line,
                'column': ctx.IDENTIFIER().symbol.column
            })
            return None
    
    
    # Visit a parse tree produced by tngParser#bool.
    def visitBool(self, ctx:tngParser.BoolContext) -> bool:
        return ctx.BOOL().getText() == 'True'

del tngParser