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
        4,1,42,189,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,5,0,38,8,0,10,0,12,0,41,
        9,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,49,8,1,1,1,1,1,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,65,8,4,10,4,12,4,68,9,4,1,5,1,
        5,1,5,1,5,1,5,3,5,75,8,5,1,6,1,6,1,6,3,6,80,8,6,1,7,1,7,1,7,1,7,
        3,7,86,8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,94,8,8,1,9,1,9,1,9,5,9,99,
        8,9,10,9,12,9,102,9,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,
        112,8,10,1,11,3,11,115,8,11,1,11,1,11,1,11,1,11,1,11,3,11,122,8,
        11,1,12,1,12,1,12,5,12,127,8,12,10,12,12,12,130,9,12,1,13,1,13,1,
        13,1,13,1,13,1,13,5,13,138,8,13,10,13,12,13,141,9,13,1,13,1,13,3,
        13,145,8,13,1,14,1,14,1,14,1,14,5,14,151,8,14,10,14,12,14,154,9,
        14,1,14,3,14,157,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,5,15,169,8,15,10,15,12,15,172,9,15,1,15,1,15,1,16,1,16,1,
        16,1,16,1,16,1,16,5,16,182,8,16,10,16,12,16,185,9,16,1,16,1,16,1,
        16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,4,1,0,
        12,13,1,0,40,41,1,0,14,16,1,0,27,28,198,0,34,1,0,0,0,2,42,1,0,0,
        0,4,52,1,0,0,0,6,55,1,0,0,0,8,61,1,0,0,0,10,74,1,0,0,0,12,79,1,0,
        0,0,14,85,1,0,0,0,16,93,1,0,0,0,18,95,1,0,0,0,20,111,1,0,0,0,22,
        114,1,0,0,0,24,123,1,0,0,0,26,131,1,0,0,0,28,146,1,0,0,0,30,158,
        1,0,0,0,32,175,1,0,0,0,34,39,3,8,4,0,35,36,7,0,0,0,36,38,3,8,4,0,
        37,35,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,1,1,0,
        0,0,41,39,1,0,0,0,42,43,5,40,0,0,43,48,5,19,0,0,44,49,3,0,0,0,45,
        49,5,41,0,0,46,49,5,39,0,0,47,49,5,40,0,0,48,44,1,0,0,0,48,45,1,
        0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,50,1,0,0,0,50,51,5,34,0,0,51,
        3,1,0,0,0,52,53,3,14,7,0,53,54,3,2,1,0,54,5,1,0,0,0,55,56,5,6,0,
        0,56,57,5,30,0,0,57,58,7,1,0,0,58,59,5,31,0,0,59,60,5,34,0,0,60,
        7,1,0,0,0,61,66,3,10,5,0,62,63,7,2,0,0,63,65,3,10,5,0,64,62,1,0,
        0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,9,1,0,0,0,68,66,
        1,0,0,0,69,75,3,12,6,0,70,71,5,30,0,0,71,72,3,0,0,0,72,73,5,31,0,
        0,73,75,1,0,0,0,74,69,1,0,0,0,74,70,1,0,0,0,75,11,1,0,0,0,76,80,
        5,37,0,0,77,80,5,38,0,0,78,80,5,40,0,0,79,76,1,0,0,0,79,77,1,0,0,
        0,79,78,1,0,0,0,80,13,1,0,0,0,81,86,5,7,0,0,82,86,5,8,0,0,83,86,
        5,9,0,0,84,86,5,10,0,0,85,81,1,0,0,0,85,82,1,0,0,0,85,83,1,0,0,0,
        85,84,1,0,0,0,86,15,1,0,0,0,87,94,3,4,2,0,88,94,3,2,1,0,89,94,3,
        6,3,0,90,94,3,26,13,0,91,94,3,30,15,0,92,94,3,32,16,0,93,87,1,0,
        0,0,93,88,1,0,0,0,93,89,1,0,0,0,93,90,1,0,0,0,93,91,1,0,0,0,93,92,
        1,0,0,0,94,17,1,0,0,0,95,96,5,11,0,0,96,100,5,32,0,0,97,99,3,16,
        8,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,
        101,103,1,0,0,0,102,100,1,0,0,0,103,104,5,33,0,0,104,105,5,0,0,1,
        105,19,1,0,0,0,106,107,3,0,0,0,107,108,5,20,0,0,108,109,3,0,0,0,
        109,112,1,0,0,0,110,112,5,39,0,0,111,106,1,0,0,0,111,110,1,0,0,0,
        112,21,1,0,0,0,113,115,5,29,0,0,114,113,1,0,0,0,114,115,1,0,0,0,
        115,121,1,0,0,0,116,117,5,30,0,0,117,118,3,20,10,0,118,119,5,31,
        0,0,119,122,1,0,0,0,120,122,3,20,10,0,121,116,1,0,0,0,121,120,1,
        0,0,0,122,23,1,0,0,0,123,128,3,22,11,0,124,125,7,3,0,0,125,127,3,
        22,11,0,126,124,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,
        1,0,0,0,129,25,1,0,0,0,130,128,1,0,0,0,131,132,5,1,0,0,132,133,5,
        30,0,0,133,134,3,24,12,0,134,135,5,31,0,0,135,139,5,32,0,0,136,138,
        3,16,8,0,137,136,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,
        1,0,0,0,140,142,1,0,0,0,141,139,1,0,0,0,142,144,5,33,0,0,143,145,
        3,28,14,0,144,143,1,0,0,0,144,145,1,0,0,0,145,27,1,0,0,0,146,156,
        5,2,0,0,147,157,3,26,13,0,148,152,5,32,0,0,149,151,3,16,8,0,150,
        149,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,
        155,1,0,0,0,154,152,1,0,0,0,155,157,5,33,0,0,156,147,1,0,0,0,156,
        148,1,0,0,0,157,29,1,0,0,0,158,159,5,3,0,0,159,160,5,30,0,0,160,
        161,3,2,1,0,161,162,5,34,0,0,162,163,3,24,12,0,163,164,5,34,0,0,
        164,165,3,2,1,0,165,166,5,31,0,0,166,170,5,32,0,0,167,169,3,16,8,
        0,168,167,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,
        0,171,173,1,0,0,0,172,170,1,0,0,0,173,174,5,33,0,0,174,31,1,0,0,
        0,175,176,5,3,0,0,176,177,5,30,0,0,177,178,3,24,12,0,178,179,5,31,
        0,0,179,183,5,32,0,0,180,182,3,16,8,0,181,180,1,0,0,0,182,185,1,
        0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,186,1,0,0,0,185,183,1,
        0,0,0,186,187,5,33,0,0,187,33,1,0,0,0,18,39,48,66,74,79,85,93,100,
        111,114,121,128,139,144,152,156,170,183
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

        def PV(self):
            return self.getToken(tngParser.PV, 0)

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


            self.state = 50
            self.match(tngParser.PV)
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
            self.state = 52
            self.tipo()
            self.state = 53
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

        def PV(self):
            return self.getToken(tngParser.PV, 0)

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
            self.state = 55
            self.match(tngParser.PRINT)
            self.state = 56
            self.match(tngParser.PAR_E)
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==40 or _la==41):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 58
            self.match(tngParser.PAR_D)
            self.state = 59
            self.match(tngParser.PV)
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
            self.state = 61
            self.factor()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0):
                self.state = 62
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 63
                self.factor()
                self.state = 68
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
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37, 38, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.number()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(tngParser.PAR_E)
                self.state = 71
                self.expression()
                self.state = 72
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


        def getRuleIndex(self):
            return tngParser.RULE_number

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntegerContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tngParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(tngParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tngParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(tngParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tngParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(tngParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)



    def number(self):

        localctx = tngParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_number)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                localctx = tngParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(tngParser.INTEGER)
                pass
            elif token in [38]:
                localctx = tngParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(tngParser.FLOAT)
                pass
            elif token in [40]:
                localctx = tngParser.IdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.match(tngParser.IDENTIFIER)
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


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tngParser.RULE_tipo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TipoBoolContext(TipoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tngParser.TipoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TIPO_BOOL(self):
            return self.getToken(tngParser.TIPO_BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoBool" ):
                listener.enterTipoBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoBool" ):
                listener.exitTipoBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoBool" ):
                return visitor.visitTipoBool(self)
            else:
                return visitor.visitChildren(self)


    class TipoCharContext(TipoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tngParser.TipoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TIPO_CHAR(self):
            return self.getToken(tngParser.TIPO_CHAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoChar" ):
                listener.enterTipoChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoChar" ):
                listener.exitTipoChar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoChar" ):
                return visitor.visitTipoChar(self)
            else:
                return visitor.visitChildren(self)


    class TipoFloatContext(TipoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tngParser.TipoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TIPO_FLOAT(self):
            return self.getToken(tngParser.TIPO_FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoFloat" ):
                listener.enterTipoFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoFloat" ):
                listener.exitTipoFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoFloat" ):
                return visitor.visitTipoFloat(self)
            else:
                return visitor.visitChildren(self)


    class TipoIntContext(TipoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tngParser.TipoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TIPO_INT(self):
            return self.getToken(tngParser.TIPO_INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoInt" ):
                listener.enterTipoInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoInt" ):
                listener.exitTipoInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoInt" ):
                return visitor.visitTipoInt(self)
            else:
                return visitor.visitChildren(self)



    def tipo(self):

        localctx = tngParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tipo)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = tngParser.TipoIntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(tngParser.TIPO_INT)
                pass
            elif token in [8]:
                localctx = tngParser.TipoCharContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(tngParser.TIPO_CHAR)
                pass
            elif token in [9]:
                localctx = tngParser.TipoFloatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.match(tngParser.TIPO_FLOAT)
                pass
            elif token in [10]:
                localctx = tngParser.TipoBoolContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.match(tngParser.TIPO_BOOL)
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


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao(self):
            return self.getTypedRuleContext(tngParser.DeclaracaoContext,0)


        def atribuicao(self):
            return self.getTypedRuleContext(tngParser.AtribuicaoContext,0)


        def chamada_print(self):
            return self.getTypedRuleContext(tngParser.Chamada_printContext,0)


        def if_bloco(self):
            return self.getTypedRuleContext(tngParser.If_blocoContext,0)


        def for_bloco(self):
            return self.getTypedRuleContext(tngParser.For_blocoContext,0)


        def while_bloco(self):
            return self.getTypedRuleContext(tngParser.While_blocoContext,0)


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
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 87
                self.declaracao()
                pass

            elif la_ == 2:
                self.state = 88
                self.atribuicao()
                pass

            elif la_ == 3:
                self.state = 89
                self.chamada_print()
                pass

            elif la_ == 4:
                self.state = 90
                self.if_bloco()
                pass

            elif la_ == 5:
                self.state = 91
                self.for_bloco()
                pass

            elif la_ == 6:
                self.state = 92
                self.while_bloco()
                pass


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
            self.state = 95
            self.match(tngParser.MAIN)
            self.state = 96
            self.match(tngParser.CHAVE_E)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511629770) != 0):
                self.state = 97
                self.comando()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(tngParser.CHAVE_D)
            self.state = 104
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

        def BOOL(self):
            return self.getToken(tngParser.BOOL, 0)

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
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30, 37, 38, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.expression()
                self.state = 107
                self.match(tngParser.OP_LOGICO)
                self.state = 108
                self.expression()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.match(tngParser.BOOL)
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
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 113
                self.match(tngParser.NOT)


            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 116
                self.match(tngParser.PAR_E)
                self.state = 117
                self.expr_bool()
                self.state = 118
                self.match(tngParser.PAR_D)
                pass

            elif la_ == 2:
                self.state = 120
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
            self.state = 123
            self.fator_bool()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 124
                _la = self._input.LA(1)
                if not(_la==27 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 125
                self.fator_bool()
                self.state = 130
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
            self.state = 131
            self.match(tngParser.IF)
            self.state = 132
            self.match(tngParser.PAR_E)
            self.state = 133
            self.cond()
            self.state = 134
            self.match(tngParser.PAR_D)
            self.state = 135
            self.match(tngParser.CHAVE_E)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511629770) != 0):
                self.state = 136
                self.comando()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(tngParser.CHAVE_D)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 143
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
            self.state = 146
            self.match(tngParser.ELSE)
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 147
                self.if_bloco()
                pass
            elif token in [32]:
                self.state = 148
                self.match(tngParser.CHAVE_E)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511629770) != 0):
                    self.state = 149
                    self.comando()
                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 155
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
            self.state = 158
            self.match(tngParser.FOR)
            self.state = 159
            self.match(tngParser.PAR_E)
            self.state = 160
            self.atribuicao()
            self.state = 161
            self.match(tngParser.PV)
            self.state = 162
            self.cond()
            self.state = 163
            self.match(tngParser.PV)
            self.state = 164
            self.atribuicao()
            self.state = 165
            self.match(tngParser.PAR_D)
            self.state = 166
            self.match(tngParser.CHAVE_E)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511629770) != 0):
                self.state = 167
                self.comando()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 173
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
            self.state = 175
            self.match(tngParser.FOR)
            self.state = 176
            self.match(tngParser.PAR_E)
            self.state = 177
            self.cond()
            self.state = 178
            self.match(tngParser.PAR_D)
            self.state = 179
            self.match(tngParser.CHAVE_E)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511629770) != 0):
                self.state = 180
                self.comando()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
            self.match(tngParser.CHAVE_D)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





