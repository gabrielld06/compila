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



del tngParser