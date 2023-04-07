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
# TODO: ver se ta certo o tratamento de expressão -> parece q sim :) 
#       precedencia booleana -> NOT | ( ) -> AND -> OR -> (OP_RELACIONAIS) ;; fazer a regra no mesmo formato da expr aritmetica deve funcionar e sem muito trabalho
#           exemplo:    True or False and False deve retornar True
#       não testei o if e else corretamente por causa disso ^
#       for, while
#       arquivos de testes que cobrem todos os erros && testes automatizado :3
#       input de dados (cin, scan)


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
    def insertCode(self, c):
        if len(self.errors) == 0:
            self.code += c

    # Visit a parse tree produced by tngParser#expression.
    # expression : term ((MAIS | MENOS) term)*;
    def visitExpression(self, ctx:tngParser.ExpressionContext):
        nodes = ctx.getChildCount()

        c = ctx.getChild(0)
        left = self.visit(c)
        
        if not left: return None
        
        for i in range(1, nodes):
            c = ctx.getChild(i)

            if c.getText() == '+' or c.getText() == '-': 
                op = c.getText()
                continue

            right = self.visit(c)
            
            if not right: return None

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
    def visitTerm(self, ctx:tngParser.TermContext):
        nodes = ctx.getChildCount()

        c = ctx.getChild(0)
        left = self.visit(c)

        if not left: return None
        
        for i in range(1, nodes):
            c = ctx.getChild(i)

            if c.getText() == '*' or c.getText() == '/' or c.getText() == '%': 
                op = c.getText()
                continue

            right = self.visit(c)

            if not right: return None

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
    def visitFactor(self, ctx:tngParser.FactorContext):
        if ctx.number():
            value = self.visit(ctx.number())

            c = ctx.number().getChild(0)
            token = c.symbol
            type = tngLexer.symbolicNames[token.type]   # pega o nome do tipo do nó terminal

            if type == 'IDENTIFIER':
                if not value: return None

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


    # Visit a parse tree produced by tngParser#atribuicao.
    # atribuicao : IDENTIFIER ATRIB (id | expression | string | bool) PV;
    # INT <- INT FLOAT
    # FLOAT <- INT FLOAT
    # BOOL <- BOOL
    # STRING <- STRING
    def visitAtribuicao(self, ctx:tngParser.AtribuicaoContext):
        identificador = ctx.IDENTIFIER()     # identificador

        if not identificador: return None

        nome = identificador.getText()          # nome do identificador
        token = identificador.symbol            # simbolo do identificador
        tipo = self.symbolTable[nome]['tipo']   # pega o nome do tipo do identificador

        c = ctx.getChild(2)                     # (id | expression | string | bool)
        value = self.visit(c)
        
        if not value: return None

        try:
            if ctx.expression():    # atribuição de expressões aritmeticas
                if tipo == 'int':
                    self.symbolTable[nome]['value'] = (int(value) if type(value) != str else value)  # type(value) != str : caso de atribuição com identificador
                elif tipo == 'float':
                    self.symbolTable[nome]['value'] = (float(value) if type(value) != str else value)
                else:
                    raise Exception(f"Type conversion from numeric to {tipo} not supported")
            else:    # atribuição de string, bool ou identificador
                token_val = c.getChild(0).symbol
                tipo_val = tngLexer.symbolicNames[token_val.type]
                
                if tipo == 'string' and tipo_val == 'STRING' or tipo == 'bool' and tipo_val == 'BOOL':
                    self.symbolTable[nome]['value'] = value
                elif tipo_val == 'IDENTIFIER':
                    value_atr = self.symbolTable[value]['value']
                    tipo_atr = self.symbolTable[value]['tipo']

                    if tipo == tipo_atr:
                        self.symbolTable[nome]['value'] = value_atr
                    elif tipo == 'int' and tipo_atr == 'float':
                        self.symbolTable[nome]['value'] = (int(value_atr) if type(value_atr) != str else value_atr)
                    elif tipo == 'float' and tipo_atr == 'int':
                        self.symbolTable[nome]['value'] = (float(value_atr) if type(value_atr) != str else value_atr)
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
            
        self.insertCode(f"{nome} = {self.symbolTable[nome]['value']};\n")
            
        return value


    # Visit a parse tree produced by tngParser#declaracao.
    def visitDeclaracao(self, ctx:tngParser.DeclaracaoContext):
        tipo = ctx.tipo().getText()                         # int, float, bool, char ou string
        identificador = ctx.atribuicao().IDENTIFIER()    # identificador | pode ter dois identificadores, por isso [0] 
        nome = ctx.atribuicao().IDENTIFIER().getText()   # nome do identificador
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

        self.insertCode(f"{tipo} ")

        return self.visit(ctx.atribuicao())


    # Visit a parse tree produced by tngParser#chamada_print.
    # PRINT PAR_E (STRING | IDENTIFIER) PAR_D;
    def visitChamada_print(self, ctx:tngParser.Chamada_printContext):
        self.insertCode("cout << ")

        if ctx.IDENTIFIER():
            identificador = ctx.IDENTIFIER()     # identificador
            nome = ctx.IDENTIFIER().getText()    # nome do identificador
            token = identificador.symbol
            
            if nome in self.symbolTable:
                self.insertCode(f"{nome} ")
            else:
                self.errors.append({
                    'error' : 'Variable not declared',
                    'id'    : nome,
                    'line'  : token.line,
                    'column': token.column
                })
        else:
            self.insertCode(f"{ctx.STRING().getText()} ")

        self.insertCode("<< endl;\n")

        return None


    # Visit a parse tree produced by tngParser#Integer.
    def visitInteger(self, ctx:tngParser.IntegerContext):
        return int(ctx.getChild(0).getText())
    

    # Visit a parse tree produced by tngParser#string.
    def visitString(self, ctx:tngParser.StringContext):
        return str(ctx.getChild(0).getText())


    # Visit a parse tree produced by tngParser#Float.
    def visitFloat(self, ctx:tngParser.FloatContext):
        return float(ctx.getChild(0).getText())


    # Visit a parse tree produced by tngParser#id.
    def visitId(self, ctx:tngParser.IdContext):
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


    # Visit a parse tree produced by tngParser#Identifier.
    def visitIdentifier(self, ctx:tngParser.IdentifierContext):
        print(ctx.IDENTIFIER().getText())

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
    def visitBool(self, ctx:tngParser.BoolContext):
        return ctx.BOOL()
    

    # Visit a parse tree produced by tngParser#TipoInt.
    def visitTipoInt(self, ctx:tngParser.TipoIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#TipoFloat.
    def visitTipoFloat(self, ctx:tngParser.TipoFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#TipoBool.
    def visitTipoBool(self, ctx:tngParser.TipoBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#comando.
    def visitComando(self, ctx:tngParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#inicio.
    def visitInicio(self, ctx:tngParser.InicioContext):
        self.insertCode("#include <iostream>\nusing namespace std;\nint main(){\n")

        self.visitChildren(ctx)

        self.insertCode("return 0;\n}\n")


    # Visit a parse tree produced by tngParser#expr_bool.
    # expr_bool : (expression (MENOR | MAIOR | MENOR_IG | MAIOR_IG | IGUAL | N_IGUAL) expression) | BOOL;
    def visitExpr_bool(self, ctx:tngParser.Expr_boolContext):
        if ctx.BOOL():
            return ctx.BOOL().getText() == "True"
        
        c = ctx.getChild(0)
        left = c.accept(self)

        c = ctx.getChild(1)
        op = c.getText()

        c = ctx.getChild(2)
        right = c.accept(self)

        if (type(left) == int or type(left) == float) and (type(right) == int or type(right) == float):
            if op == '<':
                result = left < right
            elif op == '>':
                result = left > right
            elif op == '<=':
                result = left <= right
            elif op == '>=':
                result = left >= right
            elif op == '==':
                result = left == right
            else:
                result = left != right
        else:
            if type(left) == bool:
                left = str(left).lower()
            if type(right) == bool:
                right = str(right).lower()
            result = f"{left}{op}{right}"

        return result


    # Visit a parse tree produced by tngParser#fator_bool.
    # fator_bool : NOT? (PAR_E expr_bool PAR_D | expr_bool);
    def visitFator_bool(self, ctx:tngParser.Fator_boolContext):
        c = ctx.expr_bool()
        result = c.accept(self)

        if ctx.NOT():
            if type(result) == bool:
                result = not result
            else:
                result = f"not {result} "
        else:
            result = result

        return result


    # Visit a parse tree produced by tngParser#cond.
    # cond : fator_bool ((AND | OR) fator_bool)*;
    def visitCond(self, ctx:tngParser.CondContext):
        nodes = ctx.getChildCount()
        result = self.defaultResult()

        c = ctx.getChild(0)
        left = c.accept(self)

        for i in range(1, nodes):
            c = ctx.getChild(i)

            if c.getText() == 'and' or c.getText() == 'or' or c.getText() == '&&' or c.getText() == '||': 
                op = c.getText()
                continue

            right = c.accept(self)

            if type(left) == bool and type(right) == bool:
                if op == 'and' or c.getText() == '&&':
                    left = left and right
                else:
                    left = left or right
            else:
                if type(left) == bool:
                    left = str(left).lower()
                if type(right) == bool:
                    right = str(right).lower()
                left = f"{left} {op} {right} "
        
        if type(left) == bool:
            left = str(left).lower()
        return left


    # Visit a parse tree produced by tngParser#if_bloco.
    # if_bloco : IF PAR_E cond PAR_D CHAVE_E (comando)* CHAVE_D else_bloco?;
    def visitIf_bloco(self, ctx:tngParser.If_blocoContext):

        c = ctx.getChild(2)
        cond = c.accept(self)

        self.insertCode(f"if({cond}) {{\n")

        comandos = ctx.comando()
        
        for c in comandos:
            c.accept(self)

        self.insertCode(f"}}\n")

        if ctx.else_bloco():
            ctx.else_bloco().accept(self)
        
        return None


    # Visit a parse tree produced by tngParser#else_bloco.
    # else_bloco : ELSE (if_bloco | CHAVE_E (comando)* CHAVE_D);
    def visitElse_bloco(self, ctx:tngParser.Else_blocoContext):
        if ctx.if_bloco():
            self.insertCode(f"else ")

            ctx.if_bloco().accept(self)
        else:
            self.insertCode(f"else {{\n")

            comandos = ctx.comando()
            
            for c in comandos:
                c.accept(self)

            self.insertCode(f"}}\n")

        return None


    # Visit a parse tree produced by tngParser#for_bloco.
    def visitFor_bloco(self, ctx:tngParser.For_blocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#while_bloco.
    def visitWhile_bloco(self, ctx:tngParser.While_blocoContext):
        return self.visitChildren(ctx)


del tngParser