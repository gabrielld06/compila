from antlr4 import *
from tngVisitor import tngVisitor
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
#       if,
#       print
# TODO: ver se ta certo o tratamento de expressão
#       else, for, while
#       visitor para tipos são meio redundantes, é possivel recuperar o valor sem um visitor (linha 138, visitDeclaracao)
#       ver como isso vai gerar código


class tngSemantic(tngVisitor):
    
    def __init__(self):
        self.symbolTable = {}   # { 
                                # 'tipo' : str,
                                # 'value' : int | float | bool | str | None
                                # }

        self.errors = []    # { 
                            # 'error' : 'Variable not declared' | 'Variable already declared', 
                            # 'id'    : str, 
                            # 'line'  : int, 
                            # 'column': int
                            # }
        
        self.code = ""

    # Visit a parse tree produced by tngParser#expression.
    def visitExpression(self, ctx:tngParser.ExpressionContext):
        nodes = ctx.getChildCount()
        result = self.defaultResult()

        c = ctx.getChild(0)
        left = c.accept(self)
        
        for i in range(1, nodes):
            if not self.shouldVisitNextChild(ctx, result):
                return result

            c = ctx.getChild(i)

            if c.getText() == '+' or c.getText() == '-': 
                op = c.getText()
                continue

            right = c.accept(self)

            if (type(left) == int or type(left) == float) and (type(right) == int or type(right) == float):
                if op == '+':
                    left += right
                else:
                    left -= right
            else:
                left = f"{left}{op}{right}"

        return left
    
    # Visit a parse tree produced by tngParser#term.
    def visitTerm(self, ctx:tngParser.TermContext):
        nodes = ctx.getChildCount()
        result = self.defaultResult()

        c = ctx.getChild(0)
        left = c.accept(self)
        
        for i in range(1, nodes):
            if not self.shouldVisitNextChild(ctx, result):
                return result

            c = ctx.getChild(i)

            if c.getText() == '*' or c.getText() == '/' or c.getText() == '%': 
                op = c.getText()
                continue

            right = c.accept(self)

            if (type(left) == int or type(left) == float) and (type(right) == int or type(right) == float):
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
    def visitFactor(self, ctx:tngParser.FactorContext):
        if ctx.number():
            return self.visitChildren(ctx)
        else:
            return self.visit(ctx.getChild(1))


    # Visit a parse tree produced by tngParser#atribuicao.
    # atribuicao : IDENTIFIER ATRIB (expression | STRING | BOOL | IDENTIFIER);
    def visitAtribuicao(self, ctx:tngParser.AtribuicaoContext):
        identificador = ctx.IDENTIFIER()[0]     # identificador | pode ter dois identificadores, por isso [0] 
        nome = ctx.IDENTIFIER()[0].getText()    # nome do identificador
        token = identificador.symbol            # simbolo do identificador

        value = self.visit(ctx.getChild(2))     # resultado da expressão

        if nome in self.symbolTable:
            if self.symbolTable[nome]['tipo'] == 'int':
                self.symbolTable[nome]['value'] = (int(value) if type(value) != str else value)
            elif self.symbolTable['tipo'] == 'float':
                self.symbolTable[nome]['value'] = (float(value) if type(value) != str else value)
            elif self.symbolTable['tipo'] == 'bool':
                self.symbolTable[nome]['value'] = (bool(value) if type(value) != str else value)
            else:
                self.symbolTable[nome]['value'] = (str(value) if type(value) != str else value)
            
            self.code += f"{nome} = {self.symbolTable[nome]['value']};\n"
        else:
            self.errors.append({
                'error' : 'Variable not declared',
                'id'    : nome,
                'line'  : token.line,
                'column': token.column
            })
            
        return value


    # Visit a parse tree produced by tngParser#declaracao.
    def visitDeclaracao(self, ctx:tngParser.DeclaracaoContext):
        tipo = ctx.tipo().getText()                         # int, float, bool, char ou string
        identificador = ctx.atribuicao().IDENTIFIER()[0]    # identificador | pode ter dois identificadores, por isso [0] 
        nome = ctx.atribuicao().IDENTIFIER()[0].getText()   # nome do identificador
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

        self.code += f"{tipo} "

        return self.visit(ctx.atribuicao())


    # Visit a parse tree produced by tngParser#chamada_print.
    # PRINT PAR_E (STRING | IDENTIFIER) PAR_D;
    def visitChamada_print(self, ctx:tngParser.Chamada_printContext):
        self.code += "cout << "

        if ctx.IDENTIFIER():
            identificador = ctx.IDENTIFIER()     # identificador
            nome = ctx.IDENTIFIER().getText()    # nome do identificador
            token = identificador.symbol
            
            if nome in self.symbolTable:
                self.code += f"{nome} "
            else:
                self.errors.append({
                    'error' : 'Variable not declared',
                    'id'    : nome,
                    'line'  : token.line,
                    'column': token.column
                })
        else:
            self.code += f"{ctx.STRING().getText()} "

        self.code += "<< endl;\n"

        return None


    # Visit a parse tree produced by tngParser#Integer.
    def visitInteger(self, ctx:tngParser.IntegerContext):
        return int(ctx.getChild(0).getText())


    # Visit a parse tree produced by tngParser#Float.
    def visitFloat(self, ctx:tngParser.FloatContext):
        return float(ctx.getChild(0).getText())


    # Visit a parse tree produced by tngParser#Identifier.
    def visitIdentifier(self, ctx:tngParser.IdentifierContext):
        return ctx.IDENTIFIER()


    # Visit a parse tree produced by tngParser#TipoInt.
    def visitTipoInt(self, ctx:tngParser.TipoIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#TipoChar.
    def visitTipoChar(self, ctx:tngParser.TipoCharContext):
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
        self.code += "#include <iostream>\nusing namespace std;\nint main(){\n"

        self.visitChildren(ctx)

        self.code += "return 0;\n}\n"


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

        self.code += f"if({cond}) {{\n"

        comandos = ctx.comando()
        
        for c in comandos:
            c.accept(self)

        self.code += f"}}\n"
        
        return None


    # Visit a parse tree produced by tngParser#else_bloco.
    def visitElse_bloco(self, ctx:tngParser.Else_blocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#for_bloco.
    def visitFor_bloco(self, ctx:tngParser.For_blocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#while_bloco.
    def visitWhile_bloco(self, ctx:tngParser.While_blocoContext):
        return self.visitChildren(ctx)


del tngParser