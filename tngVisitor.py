# Generated from tng.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tngParser import tngParser
else:
    from tngParser import tngParser

# This class defines a complete generic visitor for a parse tree produced by tngParser.

class tngVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tngParser#expression.
    def visitExpression(self, ctx:tngParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#atribuicao.
    def visitAtribuicao(self, ctx:tngParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#declaracao.
    def visitDeclaracao(self, ctx:tngParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#chamada_print.
    def visitChamada_print(self, ctx:tngParser.Chamada_printContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#term.
    def visitTerm(self, ctx:tngParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#factor.
    def visitFactor(self, ctx:tngParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#Integer.
    def visitInteger(self, ctx:tngParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#Float.
    def visitFloat(self, ctx:tngParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#Identifier.
    def visitIdentifier(self, ctx:tngParser.IdentifierContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#expr_bool.
    def visitExpr_bool(self, ctx:tngParser.Expr_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#fator_bool.
    def visitFator_bool(self, ctx:tngParser.Fator_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#cond.
    def visitCond(self, ctx:tngParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tngParser#if_bloco.
    def visitIf_bloco(self, ctx:tngParser.If_blocoContext):
        return self.visitChildren(ctx)


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