# Generated from tng.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,42,175,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,5,0,38,8,0,10,0,12,0,41,
        9,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,49,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,5,4,62,8,4,10,4,12,4,65,9,4,1,5,1,5,1,5,1,5,1,
        5,3,5,72,8,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,3,8,81,8,8,1,8,1,8,1,9,
        1,9,1,9,5,9,88,8,9,10,9,12,9,91,9,9,1,9,1,9,1,9,1,10,1,10,1,10,1,
        10,1,11,3,11,101,8,11,1,11,1,11,1,11,1,11,1,11,3,11,108,8,11,1,12,
        1,12,1,12,5,12,113,8,12,10,12,12,12,116,9,12,1,13,1,13,1,13,1,13,
        1,13,1,13,5,13,124,8,13,10,13,12,13,127,9,13,1,13,1,13,3,13,131,
        8,13,1,14,1,14,1,14,1,14,5,14,137,8,14,10,14,12,14,140,9,14,1,14,
        3,14,143,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        5,15,155,8,15,10,15,12,15,158,9,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,1,16,5,16,168,8,16,10,16,12,16,171,9,16,1,16,1,16,1,16,0,0,
        17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,6,1,0,12,13,1,
        0,40,41,1,0,14,16,2,0,37,38,40,40,1,0,7,10,1,0,27,28,175,0,34,1,
        0,0,0,2,42,1,0,0,0,4,50,1,0,0,0,6,53,1,0,0,0,8,58,1,0,0,0,10,71,
        1,0,0,0,12,73,1,0,0,0,14,75,1,0,0,0,16,80,1,0,0,0,18,84,1,0,0,0,
        20,95,1,0,0,0,22,100,1,0,0,0,24,109,1,0,0,0,26,117,1,0,0,0,28,132,
        1,0,0,0,30,144,1,0,0,0,32,161,1,0,0,0,34,39,3,8,4,0,35,36,7,0,0,
        0,36,38,3,8,4,0,37,35,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,
        1,0,0,0,40,1,1,0,0,0,41,39,1,0,0,0,42,43,5,40,0,0,43,48,5,19,0,0,
        44,49,3,0,0,0,45,49,5,41,0,0,46,49,5,39,0,0,47,49,5,40,0,0,48,44,
        1,0,0,0,48,45,1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,3,1,0,0,0,50,
        51,3,14,7,0,51,52,3,2,1,0,52,5,1,0,0,0,53,54,5,6,0,0,54,55,5,30,
        0,0,55,56,7,1,0,0,56,57,5,31,0,0,57,7,1,0,0,0,58,63,3,10,5,0,59,
        60,7,2,0,0,60,62,3,10,5,0,61,59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,
        0,0,63,64,1,0,0,0,64,9,1,0,0,0,65,63,1,0,0,0,66,72,3,12,6,0,67,68,
        5,30,0,0,68,69,3,0,0,0,69,70,5,31,0,0,70,72,1,0,0,0,71,66,1,0,0,
        0,71,67,1,0,0,0,72,11,1,0,0,0,73,74,7,3,0,0,74,13,1,0,0,0,75,76,
        7,4,0,0,76,15,1,0,0,0,77,81,3,4,2,0,78,81,3,2,1,0,79,81,3,6,3,0,
        80,77,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,82,1,0,0,0,82,83,5,
        34,0,0,83,17,1,0,0,0,84,85,5,11,0,0,85,89,5,32,0,0,86,88,3,16,8,
        0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,92,
        1,0,0,0,91,89,1,0,0,0,92,93,5,33,0,0,93,94,5,0,0,1,94,19,1,0,0,0,
        95,96,3,0,0,0,96,97,5,20,0,0,97,98,3,0,0,0,98,21,1,0,0,0,99,101,
        5,29,0,0,100,99,1,0,0,0,100,101,1,0,0,0,101,107,1,0,0,0,102,103,
        5,30,0,0,103,104,3,20,10,0,104,105,5,31,0,0,105,108,1,0,0,0,106,
        108,3,20,10,0,107,102,1,0,0,0,107,106,1,0,0,0,108,23,1,0,0,0,109,
        114,3,22,11,0,110,111,7,5,0,0,111,113,3,22,11,0,112,110,1,0,0,0,
        113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,25,1,0,0,0,116,
        114,1,0,0,0,117,118,5,1,0,0,118,119,5,30,0,0,119,120,3,24,12,0,120,
        121,5,31,0,0,121,125,5,32,0,0,122,124,3,16,8,0,123,122,1,0,0,0,124,
        127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,0,127,
        125,1,0,0,0,128,130,5,33,0,0,129,131,3,28,14,0,130,129,1,0,0,0,130,
        131,1,0,0,0,131,27,1,0,0,0,132,142,5,2,0,0,133,143,3,26,13,0,134,
        138,5,32,0,0,135,137,3,16,8,0,136,135,1,0,0,0,137,140,1,0,0,0,138,
        136,1,0,0,0,138,139,1,0,0,0,139,141,1,0,0,0,140,138,1,0,0,0,141,
        143,5,33,0,0,142,133,1,0,0,0,142,134,1,0,0,0,143,29,1,0,0,0,144,
        145,5,3,0,0,145,146,5,30,0,0,146,147,3,2,1,0,147,148,5,34,0,0,148,
        149,3,24,12,0,149,150,5,34,0,0,150,151,3,2,1,0,151,152,5,31,0,0,
        152,156,5,32,0,0,153,155,3,16,8,0,154,153,1,0,0,0,155,158,1,0,0,
        0,156,154,1,0,0,0,156,157,1,0,0,0,157,159,1,0,0,0,158,156,1,0,0,
        0,159,160,5,33,0,0,160,31,1,0,0,0,161,162,5,3,0,0,162,163,5,30,0,
        0,163,164,3,24,12,0,164,165,5,31,0,0,165,169,5,32,0,0,166,168,3,
        16,8,0,167,166,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,
        0,0,0,170,172,1,0,0,0,171,169,1,0,0,0,172,173,5,33,0,0,173,33,1,
        0,0,0,15,39,48,63,71,80,89,100,107,114,125,130,138,142,156,169
    ]

class tngParser ( Parser ):

    grammarFileName = "tng.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'while'", 
                     "'return'", "'print'", "'int'", "'char'", "'float'", 
                     "'bool'", "'main'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'++'", "'--'", "'='", "<INVALID>", "'<'", "'>'", "'<='", 
                     "'>='", "'=='", "'!='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "WHILE", "RETURN", 
                      "PRINT", "TIPO_INT", "TIPO_CHAR", "TIPO_FLOAT", "TIPO_BOOL", 
                      "MAIN", "MAIS", "MENOS", "MULT", "DIV", "MOD", "INC", 
                      "DEC", "ATRIB", "OP_LOGICO", "MENOR", "MAIOR", "MENOR_IG", 
                      "MAIOR_IG", "IGUAL", "N_IGUAL", "AND", "OR", "NOT", 
                      "PAR_E", "PAR_D", "CHAVE_E", "CHAVE_D", "PV", "VIRG", 
                      "PONTO", "INTEGER", "FLOAT", "BOOL", "IDENTIFIER", 
                      "STRING", "WS" ]

    RULE_expression = 0
    RULE_atribuicao = 1
    RULE_declaracao = 2
    RULE_chamada_print = 3
    RULE_term = 4
    RULE_factor = 5
    RULE_number = 6
    RULE_tipo = 7
    RULE_comando = 8
    RULE_inicio = 9
    RULE_expr_bool = 10
    RULE_fator_bool = 11
    RULE_cond = 12
    RULE_if_bloco = 13
    RULE_else_bloco = 14
    RULE_for_bloco = 15
    RULE_while_bloco = 16

    ruleNames =  [ "expression", "atribuicao", "declaracao", "chamada_print", 
                   "term", "factor", "number", "tipo", "comando", "inicio", 
                   "expr_bool", "fator_bool", "cond", "if_bloco", "else_bloco", 
                   "for_bloco", "while_bloco" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    WHILE=4
    RETURN=5
    PRINT=6
    TIPO_INT=7
    TIPO_CHAR=8
    TIPO_FLOAT=9
    TIPO_BOOL=10
    MAIN=11
    MAIS=12
    MENOS=13
    MULT=14
    DIV=15
    MOD=16
    INC=17
    DEC=18
    ATRIB=19
    OP_LOGICO=20
    MENOR=21
    MAIOR=22
    MENOR_IG=23
    MAIOR_IG=24
    IGUAL=25
    N_IGUAL=26
    AND=27
    OR=28
    NOT=29
    PAR_E=30
    PAR_D=31
    CHAVE_E=32
    CHAVE_D=33
    PV=34
    VIRG=35
    PONTO=36
    INTEGER=37
    FLOAT=38
    BOOL=39
    IDENTIFIER=40
    STRING=41
    WS=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tngParser.TermContext)
            else:
                return self.getTypedRuleContext(tngParser.TermContext,i)


        def MAIS(self, i:int=None):
            if i is None:
                return self.getTokens(tngParser.MAIS)
            else:
                return self.getToken(tngParser.MAIS, i)

        def MENOS(self, i:int=None):
            if i is None:
                return self.getTokens(tngParser.MENOS)
            else:
                return self.getToken(tngParser.MENOS, i)

        def getRuleIndex(self):
            return tngParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = tngParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.term()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==13:
                self.state = 35
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 36
                self.term()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(tngParser.IDENTIFIER)
            else:
                return self.getToken(tngParser.IDENTIFIER, i)

        def ATRIB(self):
            return self.getToken(tngParser.ATRIB, 0)

        def expression(self):
            return self.getTypedRuleContext(tngParser.ExpressionContext,0)


        def STRING(self):
            return self.getToken(tngParser.STRING, 0)

        def BOOL(self):
            return self.getToken(tngParser.BOOL, 0)

        def getRuleIndex(self):
            return tngParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = tngParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(tngParser.IDENTIFIER)
            self.state = 43
            self.match(tngParser.ATRIB)
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 44
                self.expression()
                pass

            elif la_ == 2:
                self.state = 45
                self.match(tngParser.STRING)
                pass

            elif la_ == 3:
                self.state = 46
                self.match(tngParser.BOOL)
                pass

            elif la_ == 4:
                self.state = 47
                self.match(tngParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(tngParser.TipoContext,0)


        def atribuicao(self):
            return self.getTypedRuleContext(tngParser.AtribuicaoContext,0)


        def getRuleIndex(self):
            return tngParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = tngParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.tipo()
            self.state = 51
            self.atribuicao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Chamada_printContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(tngParser.PRINT, 0)

        def PAR_E(self):
            return self.getToken(tngParser.PAR_E, 0)

        def PAR_D(self):
            return self.getToken(tngParser.PAR_D, 0)

        def STRING(self):
            return self.getToken(tngParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(tngParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return tngParser.RULE_chamada_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChamada_print" ):
                listener.enterChamada_print(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChamada_print" ):
                listener.exitChamada_print(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChamada_print" ):
                return visitor.visitChamada_print(self)
            else:
                return visitor.visitChildren(self)




    def chamada_print(self):

        localctx = tngParser.Chamada_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_chamada_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(tngParser.PRINT)
            self.state = 54
            self.match(tngParser.PAR_E)
            self.state = 55
            _la = self._input.LA(1)
            if not(_la==40 or _la==41):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 56
            self.match(tngParser.PAR_D)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tngParser.FactorContext)
            else:
                return self.getTypedRuleContext(tngParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(tngParser.MULT)
            else:
                return self.getToken(tngParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(tngParser.DIV)
            else:
                return self.getToken(tngParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(tngParser.MOD)
            else:
                return self.getToken(tngParser.MOD, i)

        def getRuleIndex(self):
            return tngParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = tngParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.factor()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0):
                self.state = 59
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 60
                self.factor()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(tngParser.NumberContext,0)


        def PAR_E(self):
            return self.getToken(tngParser.PAR_E, 0)

        def expression(self):
            return self.getTypedRuleContext(tngParser.ExpressionContext,0)


        def PAR_D(self):
            return self.getToken(tngParser.PAR_D, 0)

        def getRuleIndex(self):
            return tngParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = tngParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37, 38, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.number()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(tngParser.PAR_E)
                self.state = 68
                self.expression()
                self.state = 69
                self.match(tngParser.PAR_D)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(tngParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(tngParser.FLOAT, 0)

        def IDENTIFIER(self):
            return self.getToken(tngParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return tngParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = tngParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1511828488192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO_INT(self):
            return self.getToken(tngParser.TIPO_INT, 0)

        def TIPO_CHAR(self):
            return self.getToken(tngParser.TIPO_CHAR, 0)

        def TIPO_FLOAT(self):
            return self.getToken(tngParser.TIPO_FLOAT, 0)

        def TIPO_BOOL(self):
            return self.getToken(tngParser.TIPO_BOOL, 0)

        def getRuleIndex(self):
            return tngParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = tngParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PV(self):
            return self.getToken(tngParser.PV, 0)

        def declaracao(self):
            return self.getTypedRuleContext(tngParser.DeclaracaoContext,0)


        def atribuicao(self):
            return self.getTypedRuleContext(tngParser.AtribuicaoContext,0)


        def chamada_print(self):
            return self.getTypedRuleContext(tngParser.Chamada_printContext,0)


        def getRuleIndex(self):
            return tngParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = tngParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comando)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 10]:
                self.state = 77
                self.declaracao()
                pass
            elif token in [40]:
                self.state = 78
                self.atribuicao()
                pass
            elif token in [6]:
                self.state = 79
                self.chamada_print()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 82
            self.match(tngParser.PV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(tngParser.MAIN, 0)

        def CHAVE_E(self):
            return self.getToken(tngParser.CHAVE_E, 0)

        def CHAVE_D(self):
            return self.getToken(tngParser.CHAVE_D, 0)

        def EOF(self):
            return self.getToken(tngParser.EOF, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tngParser.ComandoContext)
            else:
                return self.getTypedRuleContext(tngParser.ComandoContext,i)


        def getRuleIndex(self):
            return tngParser.RULE_inicio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicio" ):
                listener.enterInicio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicio" ):
                listener.exitInicio(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicio" ):
                return visitor.visitInicio(self)
            else:
                return visitor.visitChildren(self)




    def inicio(self):

        localctx = tngParser.InicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_inicio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(tngParser.MAIN)
            self.state = 85
            self.match(tngParser.CHAVE_E)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511629760) != 0):
                self.state = 86
                self.comando()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(tngParser.CHAVE_D)
            self.state = 93
            self.match(tngParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tngParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(tngParser.ExpressionContext,i)


        def OP_LOGICO(self):
            return self.getToken(tngParser.OP_LOGICO, 0)

        def getRuleIndex(self):
            return tngParser.RULE_expr_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_bool" ):
                listener.enterExpr_bool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_bool" ):
                listener.exitExpr_bool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_bool" ):
                return visitor.visitExpr_bool(self)
            else:
                return visitor.visitChildren(self)




    def expr_bool(self):

        localctx = tngParser.Expr_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.expression()
            self.state = 96
            self.match(tngParser.OP_LOGICO)
            self.state = 97
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fator_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAR_E(self):
            return self.getToken(tngParser.PAR_E, 0)

        def expr_bool(self):
            return self.getTypedRuleContext(tngParser.Expr_boolContext,0)


        def PAR_D(self):
            return self.getToken(tngParser.PAR_D, 0)

        def NOT(self):
            return self.getToken(tngParser.NOT, 0)

        def getRuleIndex(self):
            return tngParser.RULE_fator_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator_bool" ):
                listener.enterFator_bool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator_bool" ):
                listener.exitFator_bool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFator_bool" ):
                return visitor.visitFator_bool(self)
            else:
                return visitor.visitChildren(self)




    def fator_bool(self):

        localctx = tngParser.Fator_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_fator_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 99
                self.match(tngParser.NOT)


            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 102
                self.match(tngParser.PAR_E)
                self.state = 103
                self.expr_bool()
                self.state = 104
                self.match(tngParser.PAR_D)
                pass

            elif la_ == 2:
                self.state = 106
                self.expr_bool()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator_bool(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tngParser.Fator_boolContext)
            else:
                return self.getTypedRuleContext(tngParser.Fator_boolContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(tngParser.AND)
            else:
                return self.getToken(tngParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(tngParser.OR)
            else:
                return self.getToken(tngParser.OR, i)

        def getRuleIndex(self):
            return tngParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = tngParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.fator_bool()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 110
                _la = self._input.LA(1)
                if not(_la==27 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 111
                self.fator_bool()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_blocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(tngParser.IF, 0)

        def PAR_E(self):
            return self.getToken(tngParser.PAR_E, 0)

        def cond(self):
            return self.getTypedRuleContext(tngParser.CondContext,0)


        def PAR_D(self):
            return self.getToken(tngParser.PAR_D, 0)

        def CHAVE_E(self):
            return self.getToken(tngParser.CHAVE_E, 0)

        def CHAVE_D(self):
            return self.getToken(tngParser.CHAVE_D, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tngParser.ComandoContext)
            else:
                return self.getTypedRuleContext(tngParser.ComandoContext,i)


        def else_bloco(self):
            return self.getTypedRuleContext(tngParser.Else_blocoContext,0)


        def getRuleIndex(self):
            return tngParser.RULE_if_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_bloco" ):
                listener.enterIf_bloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_bloco" ):
                listener.exitIf_bloco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_bloco" ):
                return visitor.visitIf_bloco(self)
            else:
                return visitor.visitChildren(self)




    def if_bloco(self):

        localctx = tngParser.If_blocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(tngParser.IF)
            self.state = 118
            self.match(tngParser.PAR_E)
            self.state = 119
            self.cond()
            self.state = 120
            self.match(tngParser.PAR_D)
            self.state = 121
            self.match(tngParser.CHAVE_E)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511629760) != 0):
                self.state = 122
                self.comando()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self.match(tngParser.CHAVE_D)
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 129
                self.else_bloco()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_blocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(tngParser.ELSE, 0)

        def if_bloco(self):
            return self.getTypedRuleContext(tngParser.If_blocoContext,0)


        def CHAVE_E(self):
            return self.getToken(tngParser.CHAVE_E, 0)

        def CHAVE_D(self):
            return self.getToken(tngParser.CHAVE_D, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tngParser.ComandoContext)
            else:
                return self.getTypedRuleContext(tngParser.ComandoContext,i)


        def getRuleIndex(self):
            return tngParser.RULE_else_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_bloco" ):
                listener.enterElse_bloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_bloco" ):
                listener.exitElse_bloco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_bloco" ):
                return visitor.visitElse_bloco(self)
            else:
                return visitor.visitChildren(self)




    def else_bloco(self):

        localctx = tngParser.Else_blocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_else_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(tngParser.ELSE)
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 133
                self.if_bloco()
                pass
            elif token in [32]:
                self.state = 134
                self.match(tngParser.CHAVE_E)
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511629760) != 0):
                    self.state = 135
                    self.comando()
                    self.state = 140
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 141
                self.match(tngParser.CHAVE_D)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_blocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(tngParser.FOR, 0)

        def PAR_E(self):
            return self.getToken(tngParser.PAR_E, 0)

        def atribuicao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tngParser.AtribuicaoContext)
            else:
                return self.getTypedRuleContext(tngParser.AtribuicaoContext,i)


        def PV(self, i:int=None):
            if i is None:
                return self.getTokens(tngParser.PV)
            else:
                return self.getToken(tngParser.PV, i)

        def cond(self):
            return self.getTypedRuleContext(tngParser.CondContext,0)


        def PAR_D(self):
            return self.getToken(tngParser.PAR_D, 0)

        def CHAVE_E(self):
            return self.getToken(tngParser.CHAVE_E, 0)

        def CHAVE_D(self):
            return self.getToken(tngParser.CHAVE_D, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tngParser.ComandoContext)
            else:
                return self.getTypedRuleContext(tngParser.ComandoContext,i)


        def getRuleIndex(self):
            return tngParser.RULE_for_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_bloco" ):
                listener.enterFor_bloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_bloco" ):
                listener.exitFor_bloco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_bloco" ):
                return visitor.visitFor_bloco(self)
            else:
                return visitor.visitChildren(self)




    def for_bloco(self):

        localctx = tngParser.For_blocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_for_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(tngParser.FOR)
            self.state = 145
            self.match(tngParser.PAR_E)
            self.state = 146
            self.atribuicao()
            self.state = 147
            self.match(tngParser.PV)
            self.state = 148
            self.cond()
            self.state = 149
            self.match(tngParser.PV)
            self.state = 150
            self.atribuicao()
            self.state = 151
            self.match(tngParser.PAR_D)
            self.state = 152
            self.match(tngParser.CHAVE_E)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511629760) != 0):
                self.state = 153
                self.comando()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
            self.match(tngParser.CHAVE_D)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_blocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(tngParser.FOR, 0)

        def PAR_E(self):
            return self.getToken(tngParser.PAR_E, 0)

        def cond(self):
            return self.getTypedRuleContext(tngParser.CondContext,0)


        def PAR_D(self):
            return self.getToken(tngParser.PAR_D, 0)

        def CHAVE_E(self):
            return self.getToken(tngParser.CHAVE_E, 0)

        def CHAVE_D(self):
            return self.getToken(tngParser.CHAVE_D, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tngParser.ComandoContext)
            else:
                return self.getTypedRuleContext(tngParser.ComandoContext,i)


        def getRuleIndex(self):
            return tngParser.RULE_while_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_bloco" ):
                listener.enterWhile_bloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_bloco" ):
                listener.exitWhile_bloco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_bloco" ):
                return visitor.visitWhile_bloco(self)
            else:
                return visitor.visitChildren(self)




    def while_bloco(self):

        localctx = tngParser.While_blocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_while_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(tngParser.FOR)
            self.state = 162
            self.match(tngParser.PAR_E)
            self.state = 163
            self.cond()
            self.state = 164
            self.match(tngParser.PAR_D)
            self.state = 165
            self.match(tngParser.CHAVE_E)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511629760) != 0):
                self.state = 166
                self.comando()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
            self.match(tngParser.CHAVE_D)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





