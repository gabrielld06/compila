# Generated from tng.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tngParser import tngParser
else:
    from tngParser import tngParser

# This class defines a complete listener for a parse tree produced by tngParser.
class tngListener(ParseTreeListener):

    # Enter a parse tree produced by tngParser#expression.
    def enterExpression(self, ctx:tngParser.ExpressionContext):
        pass

    # Exit a parse tree produced by tngParser#expression.
    def exitExpression(self, ctx:tngParser.ExpressionContext):
        pass


    # Enter a parse tree produced by tngParser#atribuicao.
    def enterAtribuicao(self, ctx:tngParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by tngParser#atribuicao.
    def exitAtribuicao(self, ctx:tngParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by tngParser#declaracao.
    def enterDeclaracao(self, ctx:tngParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by tngParser#declaracao.
    def exitDeclaracao(self, ctx:tngParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by tngParser#chamada_print.
    def enterChamada_print(self, ctx:tngParser.Chamada_printContext):
        pass

    # Exit a parse tree produced by tngParser#chamada_print.
    def exitChamada_print(self, ctx:tngParser.Chamada_printContext):
        pass


    # Enter a parse tree produced by tngParser#term.
    def enterTerm(self, ctx:tngParser.TermContext):
        pass

    # Exit a parse tree produced by tngParser#term.
    def exitTerm(self, ctx:tngParser.TermContext):
        pass


    # Enter a parse tree produced by tngParser#factor.
    def enterFactor(self, ctx:tngParser.FactorContext):
        pass

    # Exit a parse tree produced by tngParser#factor.
    def exitFactor(self, ctx:tngParser.FactorContext):
        pass


    # Enter a parse tree produced by tngParser#number.
    def enterNumber(self, ctx:tngParser.NumberContext):
        pass

    # Exit a parse tree produced by tngParser#number.
    def exitNumber(self, ctx:tngParser.NumberContext):
        pass


    # Enter a parse tree produced by tngParser#tipo.
    def enterTipo(self, ctx:tngParser.TipoContext):
        pass

    # Exit a parse tree produced by tngParser#tipo.
    def exitTipo(self, ctx:tngParser.TipoContext):
        pass


    # Enter a parse tree produced by tngParser#comando.
    def enterComando(self, ctx:tngParser.ComandoContext):
        pass

    # Exit a parse tree produced by tngParser#comando.
    def exitComando(self, ctx:tngParser.ComandoContext):
        pass


    # Enter a parse tree produced by tngParser#inicio.
    def enterInicio(self, ctx:tngParser.InicioContext):
        pass

    # Exit a parse tree produced by tngParser#inicio.
    def exitInicio(self, ctx:tngParser.InicioContext):
        pass


    # Enter a parse tree produced by tngParser#expr_bool.
    def enterExpr_bool(self, ctx:tngParser.Expr_boolContext):
        pass

    # Exit a parse tree produced by tngParser#expr_bool.
    def exitExpr_bool(self, ctx:tngParser.Expr_boolContext):
        pass


    # Enter a parse tree produced by tngParser#fator_bool.
    def enterFator_bool(self, ctx:tngParser.Fator_boolContext):
        pass

    # Exit a parse tree produced by tngParser#fator_bool.
    def exitFator_bool(self, ctx:tngParser.Fator_boolContext):
        pass


    # Enter a parse tree produced by tngParser#cond.
    def enterCond(self, ctx:tngParser.CondContext):
        pass

    # Exit a parse tree produced by tngParser#cond.
    def exitCond(self, ctx:tngParser.CondContext):
        pass


    # Enter a parse tree produced by tngParser#if_bloco.
    def enterIf_bloco(self, ctx:tngParser.If_blocoContext):
        pass

    # Exit a parse tree produced by tngParser#if_bloco.
    def exitIf_bloco(self, ctx:tngParser.If_blocoContext):
        pass


    # Enter a parse tree produced by tngParser#else_bloco.
    def enterElse_bloco(self, ctx:tngParser.Else_blocoContext):
        pass

    # Exit a parse tree produced by tngParser#else_bloco.
    def exitElse_bloco(self, ctx:tngParser.Else_blocoContext):
        pass


    # Enter a parse tree produced by tngParser#for_bloco.
    def enterFor_bloco(self, ctx:tngParser.For_blocoContext):
        pass

    # Exit a parse tree produced by tngParser#for_bloco.
    def exitFor_bloco(self, ctx:tngParser.For_blocoContext):
        pass


    # Enter a parse tree produced by tngParser#while_bloco.
    def enterWhile_bloco(self, ctx:tngParser.While_blocoContext):
        pass

    # Exit a parse tree produced by tngParser#while_bloco.
    def exitWhile_bloco(self, ctx:tngParser.While_blocoContext):
        pass



del tngParser