// Generated from tng.g4 by ANTLR 4.12.0
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class tngParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.12.0", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IF=1, ELSE=2, FOR=3, WHILE=4, RETURN=5, PRINT=6, TIPO_INT=7, TIPO_CHAR=8, 
		TIPO_FLOAT=9, TIPO_BOOL=10, MAIN=11, MAIS=12, MENOS=13, MULT=14, DIV=15, 
		MOD=16, INC=17, DEC=18, ATRIB=19, OP_LOGICO=20, MENOR=21, MAIOR=22, MENOR_IG=23, 
		MAIOR_IG=24, IGUAL=25, N_IGUAL=26, AND=27, OR=28, NOT=29, PAR_E=30, PAR_D=31, 
		CHAVE_E=32, CHAVE_D=33, PV=34, VIRG=35, PONTO=36, INTEGER=37, FLOAT=38, 
		BOOL=39, IDENTIFIER=40, STRING=41, WS=42;
	public static final int
		RULE_expression = 0, RULE_atribuicao = 1, RULE_declaracao = 2, RULE_chamada_print = 3, 
		RULE_term = 4, RULE_factor = 5, RULE_number = 6, RULE_tipo = 7, RULE_comando = 8, 
		RULE_inicio = 9, RULE_expr_bool = 10, RULE_fator_bool = 11, RULE_cond = 12, 
		RULE_if_bloco = 13, RULE_else_bloco = 14, RULE_for_bloco = 15, RULE_while_bloco = 16;
	private static String[] makeRuleNames() {
		return new String[] {
			"expression", "atribuicao", "declaracao", "chamada_print", "term", "factor", 
			"number", "tipo", "comando", "inicio", "expr_bool", "fator_bool", "cond", 
			"if_bloco", "else_bloco", "for_bloco", "while_bloco"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'else'", "'for'", "'while'", "'return'", "'print'", "'int'", 
			"'char'", "'float'", "'bool'", "'main'", "'+'", "'-'", "'*'", "'/'", 
			"'%'", "'++'", "'--'", "'='", null, "'<'", "'>'", "'<='", "'>='", "'=='", 
			"'!='", null, null, null, "'('", "')'", "'{'", "'}'", "';'", "','", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IF", "ELSE", "FOR", "WHILE", "RETURN", "PRINT", "TIPO_INT", "TIPO_CHAR", 
			"TIPO_FLOAT", "TIPO_BOOL", "MAIN", "MAIS", "MENOS", "MULT", "DIV", "MOD", 
			"INC", "DEC", "ATRIB", "OP_LOGICO", "MENOR", "MAIOR", "MENOR_IG", "MAIOR_IG", 
			"IGUAL", "N_IGUAL", "AND", "OR", "NOT", "PAR_E", "PAR_D", "CHAVE_E", 
			"CHAVE_D", "PV", "VIRG", "PONTO", "INTEGER", "FLOAT", "BOOL", "IDENTIFIER", 
			"STRING", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "tng.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public tngParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> MAIS() { return getTokens(tngParser.MAIS); }
		public TerminalNode MAIS(int i) {
			return getToken(tngParser.MAIS, i);
		}
		public List<TerminalNode> MENOS() { return getTokens(tngParser.MENOS); }
		public TerminalNode MENOS(int i) {
			return getToken(tngParser.MENOS, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			term();
			setState(39);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MAIS || _la==MENOS) {
				{
				{
				setState(35);
				_la = _input.LA(1);
				if ( !(_la==MAIS || _la==MENOS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(36);
				term();
				}
				}
				setState(41);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtribuicaoContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(tngParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(tngParser.IDENTIFIER, i);
		}
		public TerminalNode ATRIB() { return getToken(tngParser.ATRIB, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode STRING() { return getToken(tngParser.STRING, 0); }
		public TerminalNode BOOL() { return getToken(tngParser.BOOL, 0); }
		public AtribuicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atribuicao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterAtribuicao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitAtribuicao(this);
		}
	}

	public final AtribuicaoContext atribuicao() throws RecognitionException {
		AtribuicaoContext _localctx = new AtribuicaoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_atribuicao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			match(IDENTIFIER);
			setState(43);
			match(ATRIB);
			setState(48);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(44);
				expression();
				}
				break;
			case 2:
				{
				setState(45);
				match(STRING);
				}
				break;
			case 3:
				{
				setState(46);
				match(BOOL);
				}
				break;
			case 4:
				{
				setState(47);
				match(IDENTIFIER);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracaoContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public AtribuicaoContext atribuicao() {
			return getRuleContext(AtribuicaoContext.class,0);
		}
		public DeclaracaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterDeclaracao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitDeclaracao(this);
		}
	}

	public final DeclaracaoContext declaracao() throws RecognitionException {
		DeclaracaoContext _localctx = new DeclaracaoContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaracao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			tipo();
			setState(51);
			atribuicao();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Chamada_printContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(tngParser.PRINT, 0); }
		public TerminalNode PAR_E() { return getToken(tngParser.PAR_E, 0); }
		public TerminalNode PAR_D() { return getToken(tngParser.PAR_D, 0); }
		public TerminalNode STRING() { return getToken(tngParser.STRING, 0); }
		public TerminalNode IDENTIFIER() { return getToken(tngParser.IDENTIFIER, 0); }
		public Chamada_printContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_chamada_print; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterChamada_print(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitChamada_print(this);
		}
	}

	public final Chamada_printContext chamada_print() throws RecognitionException {
		Chamada_printContext _localctx = new Chamada_printContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_chamada_print);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(PRINT);
			setState(54);
			match(PAR_E);
			setState(55);
			_la = _input.LA(1);
			if ( !(_la==IDENTIFIER || _la==STRING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(56);
			match(PAR_D);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> MULT() { return getTokens(tngParser.MULT); }
		public TerminalNode MULT(int i) {
			return getToken(tngParser.MULT, i);
		}
		public List<TerminalNode> DIV() { return getTokens(tngParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(tngParser.DIV, i);
		}
		public List<TerminalNode> MOD() { return getTokens(tngParser.MOD); }
		public TerminalNode MOD(int i) {
			return getToken(tngParser.MOD, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitTerm(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			factor();
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 114688L) != 0)) {
				{
				{
				setState(59);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 114688L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(60);
				factor();
				}
				}
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public TerminalNode PAR_E() { return getToken(tngParser.PAR_E, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode PAR_D() { return getToken(tngParser.PAR_D, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitFactor(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_factor);
		try {
			setState(71);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER:
			case FLOAT:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(66);
				number();
				}
				break;
			case PAR_E:
				enterOuterAlt(_localctx, 2);
				{
				setState(67);
				match(PAR_E);
				setState(68);
				expression();
				setState(69);
				match(PAR_D);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumberContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(tngParser.INTEGER, 0); }
		public TerminalNode FLOAT() { return getToken(tngParser.FLOAT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(tngParser.IDENTIFIER, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterNumber(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitNumber(this);
		}
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_number);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1511828488192L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TerminalNode TIPO_INT() { return getToken(tngParser.TIPO_INT, 0); }
		public TerminalNode TIPO_CHAR() { return getToken(tngParser.TIPO_CHAR, 0); }
		public TerminalNode TIPO_FLOAT() { return getToken(tngParser.TIPO_FLOAT, 0); }
		public TerminalNode TIPO_BOOL() { return getToken(tngParser.TIPO_BOOL, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterTipo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitTipo(this);
		}
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1920L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComandoContext extends ParserRuleContext {
		public TerminalNode PV() { return getToken(tngParser.PV, 0); }
		public DeclaracaoContext declaracao() {
			return getRuleContext(DeclaracaoContext.class,0);
		}
		public AtribuicaoContext atribuicao() {
			return getRuleContext(AtribuicaoContext.class,0);
		}
		public Chamada_printContext chamada_print() {
			return getRuleContext(Chamada_printContext.class,0);
		}
		public ComandoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterComando(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitComando(this);
		}
	}

	public final ComandoContext comando() throws RecognitionException {
		ComandoContext _localctx = new ComandoContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_comando);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TIPO_INT:
			case TIPO_CHAR:
			case TIPO_FLOAT:
			case TIPO_BOOL:
				{
				setState(77);
				declaracao();
				}
				break;
			case IDENTIFIER:
				{
				setState(78);
				atribuicao();
				}
				break;
			case PRINT:
				{
				setState(79);
				chamada_print();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(82);
			match(PV);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InicioContext extends ParserRuleContext {
		public TerminalNode MAIN() { return getToken(tngParser.MAIN, 0); }
		public TerminalNode CHAVE_E() { return getToken(tngParser.CHAVE_E, 0); }
		public TerminalNode CHAVE_D() { return getToken(tngParser.CHAVE_D, 0); }
		public TerminalNode EOF() { return getToken(tngParser.EOF, 0); }
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public InicioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inicio; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterInicio(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitInicio(this);
		}
	}

	public final InicioContext inicio() throws RecognitionException {
		InicioContext _localctx = new InicioContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_inicio);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(MAIN);
			setState(85);
			match(CHAVE_E);
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1099511629760L) != 0)) {
				{
				{
				setState(86);
				comando();
				}
				}
				setState(91);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(92);
			match(CHAVE_D);
			setState(93);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_boolContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode OP_LOGICO() { return getToken(tngParser.OP_LOGICO, 0); }
		public Expr_boolContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_bool; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterExpr_bool(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitExpr_bool(this);
		}
	}

	public final Expr_boolContext expr_bool() throws RecognitionException {
		Expr_boolContext _localctx = new Expr_boolContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_expr_bool);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			expression();
			setState(96);
			match(OP_LOGICO);
			setState(97);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Fator_boolContext extends ParserRuleContext {
		public TerminalNode PAR_E() { return getToken(tngParser.PAR_E, 0); }
		public Expr_boolContext expr_bool() {
			return getRuleContext(Expr_boolContext.class,0);
		}
		public TerminalNode PAR_D() { return getToken(tngParser.PAR_D, 0); }
		public TerminalNode NOT() { return getToken(tngParser.NOT, 0); }
		public Fator_boolContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fator_bool; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterFator_bool(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitFator_bool(this);
		}
	}

	public final Fator_boolContext fator_bool() throws RecognitionException {
		Fator_boolContext _localctx = new Fator_boolContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_fator_bool);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NOT) {
				{
				setState(99);
				match(NOT);
				}
			}

			setState(107);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(102);
				match(PAR_E);
				setState(103);
				expr_bool();
				setState(104);
				match(PAR_D);
				}
				break;
			case 2:
				{
				setState(106);
				expr_bool();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondContext extends ParserRuleContext {
		public List<Fator_boolContext> fator_bool() {
			return getRuleContexts(Fator_boolContext.class);
		}
		public Fator_boolContext fator_bool(int i) {
			return getRuleContext(Fator_boolContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(tngParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(tngParser.AND, i);
		}
		public List<TerminalNode> OR() { return getTokens(tngParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(tngParser.OR, i);
		}
		public CondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterCond(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitCond(this);
		}
	}

	public final CondContext cond() throws RecognitionException {
		CondContext _localctx = new CondContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_cond);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			fator_bool();
			setState(114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND || _la==OR) {
				{
				{
				setState(110);
				_la = _input.LA(1);
				if ( !(_la==AND || _la==OR) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(111);
				fator_bool();
				}
				}
				setState(116);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class If_blocoContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(tngParser.IF, 0); }
		public TerminalNode PAR_E() { return getToken(tngParser.PAR_E, 0); }
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public TerminalNode PAR_D() { return getToken(tngParser.PAR_D, 0); }
		public TerminalNode CHAVE_E() { return getToken(tngParser.CHAVE_E, 0); }
		public TerminalNode CHAVE_D() { return getToken(tngParser.CHAVE_D, 0); }
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public Else_blocoContext else_bloco() {
			return getRuleContext(Else_blocoContext.class,0);
		}
		public If_blocoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_bloco; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterIf_bloco(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitIf_bloco(this);
		}
	}

	public final If_blocoContext if_bloco() throws RecognitionException {
		If_blocoContext _localctx = new If_blocoContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_if_bloco);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(IF);
			setState(118);
			match(PAR_E);
			setState(119);
			cond();
			setState(120);
			match(PAR_D);
			setState(121);
			match(CHAVE_E);
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1099511629760L) != 0)) {
				{
				{
				setState(122);
				comando();
				}
				}
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(128);
			match(CHAVE_D);
			setState(130);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(129);
				else_bloco();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Else_blocoContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(tngParser.ELSE, 0); }
		public If_blocoContext if_bloco() {
			return getRuleContext(If_blocoContext.class,0);
		}
		public TerminalNode CHAVE_E() { return getToken(tngParser.CHAVE_E, 0); }
		public TerminalNode CHAVE_D() { return getToken(tngParser.CHAVE_D, 0); }
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public Else_blocoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_bloco; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterElse_bloco(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitElse_bloco(this);
		}
	}

	public final Else_blocoContext else_bloco() throws RecognitionException {
		Else_blocoContext _localctx = new Else_blocoContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_else_bloco);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(ELSE);
			setState(142);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				{
				setState(133);
				if_bloco();
				}
				break;
			case CHAVE_E:
				{
				setState(134);
				match(CHAVE_E);
				setState(138);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1099511629760L) != 0)) {
					{
					{
					setState(135);
					comando();
					}
					}
					setState(140);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(141);
				match(CHAVE_D);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_blocoContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(tngParser.FOR, 0); }
		public TerminalNode PAR_E() { return getToken(tngParser.PAR_E, 0); }
		public List<AtribuicaoContext> atribuicao() {
			return getRuleContexts(AtribuicaoContext.class);
		}
		public AtribuicaoContext atribuicao(int i) {
			return getRuleContext(AtribuicaoContext.class,i);
		}
		public List<TerminalNode> PV() { return getTokens(tngParser.PV); }
		public TerminalNode PV(int i) {
			return getToken(tngParser.PV, i);
		}
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public TerminalNode PAR_D() { return getToken(tngParser.PAR_D, 0); }
		public TerminalNode CHAVE_E() { return getToken(tngParser.CHAVE_E, 0); }
		public TerminalNode CHAVE_D() { return getToken(tngParser.CHAVE_D, 0); }
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public For_blocoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_bloco; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterFor_bloco(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitFor_bloco(this);
		}
	}

	public final For_blocoContext for_bloco() throws RecognitionException {
		For_blocoContext _localctx = new For_blocoContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_for_bloco);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			match(FOR);
			setState(145);
			match(PAR_E);
			setState(146);
			atribuicao();
			setState(147);
			match(PV);
			setState(148);
			cond();
			setState(149);
			match(PV);
			setState(150);
			atribuicao();
			setState(151);
			match(PAR_D);
			setState(152);
			match(CHAVE_E);
			setState(156);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1099511629760L) != 0)) {
				{
				{
				setState(153);
				comando();
				}
				}
				setState(158);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(159);
			match(CHAVE_D);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class While_blocoContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(tngParser.FOR, 0); }
		public TerminalNode PAR_E() { return getToken(tngParser.PAR_E, 0); }
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public TerminalNode PAR_D() { return getToken(tngParser.PAR_D, 0); }
		public TerminalNode CHAVE_E() { return getToken(tngParser.CHAVE_E, 0); }
		public TerminalNode CHAVE_D() { return getToken(tngParser.CHAVE_D, 0); }
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public While_blocoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_bloco; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).enterWhile_bloco(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tngListener ) ((tngListener)listener).exitWhile_bloco(this);
		}
	}

	public final While_blocoContext while_bloco() throws RecognitionException {
		While_blocoContext _localctx = new While_blocoContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_while_bloco);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			match(FOR);
			setState(162);
			match(PAR_E);
			setState(163);
			cond();
			setState(164);
			match(PAR_D);
			setState(165);
			match(CHAVE_E);
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1099511629760L) != 0)) {
				{
				{
				setState(166);
				comando();
				}
				}
				setState(171);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(172);
			match(CHAVE_D);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001*\u00af\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000"+
		"&\b\u0000\n\u0000\f\u0000)\t\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u00011\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004>\b\u0004"+
		"\n\u0004\f\u0004A\t\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0003\u0005H\b\u0005\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0003\bQ\b\b\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\t\u0005\tX\b\t\n\t\f\t[\t\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0003\u000be\b\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000bl\b\u000b"+
		"\u0001\f\u0001\f\u0001\f\u0005\fq\b\f\n\f\f\ft\t\f\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0005\r|\b\r\n\r\f\r\u007f\t\r\u0001\r\u0001"+
		"\r\u0003\r\u0083\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0005"+
		"\u000e\u0089\b\u000e\n\u000e\f\u000e\u008c\t\u000e\u0001\u000e\u0003\u000e"+
		"\u008f\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f"+
		"\u009b\b\u000f\n\u000f\f\u000f\u009e\t\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0005"+
		"\u0010\u00a8\b\u0010\n\u0010\f\u0010\u00ab\t\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0000\u0000\u0011\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e \u0000\u0006\u0001\u0000\f"+
		"\r\u0001\u0000()\u0001\u0000\u000e\u0010\u0002\u0000%&((\u0001\u0000\u0007"+
		"\n\u0001\u0000\u001b\u001c\u00af\u0000\"\u0001\u0000\u0000\u0000\u0002"+
		"*\u0001\u0000\u0000\u0000\u00042\u0001\u0000\u0000\u0000\u00065\u0001"+
		"\u0000\u0000\u0000\b:\u0001\u0000\u0000\u0000\nG\u0001\u0000\u0000\u0000"+
		"\fI\u0001\u0000\u0000\u0000\u000eK\u0001\u0000\u0000\u0000\u0010P\u0001"+
		"\u0000\u0000\u0000\u0012T\u0001\u0000\u0000\u0000\u0014_\u0001\u0000\u0000"+
		"\u0000\u0016d\u0001\u0000\u0000\u0000\u0018m\u0001\u0000\u0000\u0000\u001a"+
		"u\u0001\u0000\u0000\u0000\u001c\u0084\u0001\u0000\u0000\u0000\u001e\u0090"+
		"\u0001\u0000\u0000\u0000 \u00a1\u0001\u0000\u0000\u0000\"\'\u0003\b\u0004"+
		"\u0000#$\u0007\u0000\u0000\u0000$&\u0003\b\u0004\u0000%#\u0001\u0000\u0000"+
		"\u0000&)\u0001\u0000\u0000\u0000\'%\u0001\u0000\u0000\u0000\'(\u0001\u0000"+
		"\u0000\u0000(\u0001\u0001\u0000\u0000\u0000)\'\u0001\u0000\u0000\u0000"+
		"*+\u0005(\u0000\u0000+0\u0005\u0013\u0000\u0000,1\u0003\u0000\u0000\u0000"+
		"-1\u0005)\u0000\u0000.1\u0005\'\u0000\u0000/1\u0005(\u0000\u00000,\u0001"+
		"\u0000\u0000\u00000-\u0001\u0000\u0000\u00000.\u0001\u0000\u0000\u0000"+
		"0/\u0001\u0000\u0000\u00001\u0003\u0001\u0000\u0000\u000023\u0003\u000e"+
		"\u0007\u000034\u0003\u0002\u0001\u00004\u0005\u0001\u0000\u0000\u0000"+
		"56\u0005\u0006\u0000\u000067\u0005\u001e\u0000\u000078\u0007\u0001\u0000"+
		"\u000089\u0005\u001f\u0000\u00009\u0007\u0001\u0000\u0000\u0000:?\u0003"+
		"\n\u0005\u0000;<\u0007\u0002\u0000\u0000<>\u0003\n\u0005\u0000=;\u0001"+
		"\u0000\u0000\u0000>A\u0001\u0000\u0000\u0000?=\u0001\u0000\u0000\u0000"+
		"?@\u0001\u0000\u0000\u0000@\t\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000"+
		"\u0000BH\u0003\f\u0006\u0000CD\u0005\u001e\u0000\u0000DE\u0003\u0000\u0000"+
		"\u0000EF\u0005\u001f\u0000\u0000FH\u0001\u0000\u0000\u0000GB\u0001\u0000"+
		"\u0000\u0000GC\u0001\u0000\u0000\u0000H\u000b\u0001\u0000\u0000\u0000"+
		"IJ\u0007\u0003\u0000\u0000J\r\u0001\u0000\u0000\u0000KL\u0007\u0004\u0000"+
		"\u0000L\u000f\u0001\u0000\u0000\u0000MQ\u0003\u0004\u0002\u0000NQ\u0003"+
		"\u0002\u0001\u0000OQ\u0003\u0006\u0003\u0000PM\u0001\u0000\u0000\u0000"+
		"PN\u0001\u0000\u0000\u0000PO\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000"+
		"\u0000RS\u0005\"\u0000\u0000S\u0011\u0001\u0000\u0000\u0000TU\u0005\u000b"+
		"\u0000\u0000UY\u0005 \u0000\u0000VX\u0003\u0010\b\u0000WV\u0001\u0000"+
		"\u0000\u0000X[\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000\u0000YZ\u0001"+
		"\u0000\u0000\u0000Z\\\u0001\u0000\u0000\u0000[Y\u0001\u0000\u0000\u0000"+
		"\\]\u0005!\u0000\u0000]^\u0005\u0000\u0000\u0001^\u0013\u0001\u0000\u0000"+
		"\u0000_`\u0003\u0000\u0000\u0000`a\u0005\u0014\u0000\u0000ab\u0003\u0000"+
		"\u0000\u0000b\u0015\u0001\u0000\u0000\u0000ce\u0005\u001d\u0000\u0000"+
		"dc\u0001\u0000\u0000\u0000de\u0001\u0000\u0000\u0000ek\u0001\u0000\u0000"+
		"\u0000fg\u0005\u001e\u0000\u0000gh\u0003\u0014\n\u0000hi\u0005\u001f\u0000"+
		"\u0000il\u0001\u0000\u0000\u0000jl\u0003\u0014\n\u0000kf\u0001\u0000\u0000"+
		"\u0000kj\u0001\u0000\u0000\u0000l\u0017\u0001\u0000\u0000\u0000mr\u0003"+
		"\u0016\u000b\u0000no\u0007\u0005\u0000\u0000oq\u0003\u0016\u000b\u0000"+
		"pn\u0001\u0000\u0000\u0000qt\u0001\u0000\u0000\u0000rp\u0001\u0000\u0000"+
		"\u0000rs\u0001\u0000\u0000\u0000s\u0019\u0001\u0000\u0000\u0000tr\u0001"+
		"\u0000\u0000\u0000uv\u0005\u0001\u0000\u0000vw\u0005\u001e\u0000\u0000"+
		"wx\u0003\u0018\f\u0000xy\u0005\u001f\u0000\u0000y}\u0005 \u0000\u0000"+
		"z|\u0003\u0010\b\u0000{z\u0001\u0000\u0000\u0000|\u007f\u0001\u0000\u0000"+
		"\u0000}{\u0001\u0000\u0000\u0000}~\u0001\u0000\u0000\u0000~\u0080\u0001"+
		"\u0000\u0000\u0000\u007f}\u0001\u0000\u0000\u0000\u0080\u0082\u0005!\u0000"+
		"\u0000\u0081\u0083\u0003\u001c\u000e\u0000\u0082\u0081\u0001\u0000\u0000"+
		"\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u001b\u0001\u0000\u0000"+
		"\u0000\u0084\u008e\u0005\u0002\u0000\u0000\u0085\u008f\u0003\u001a\r\u0000"+
		"\u0086\u008a\u0005 \u0000\u0000\u0087\u0089\u0003\u0010\b\u0000\u0088"+
		"\u0087\u0001\u0000\u0000\u0000\u0089\u008c\u0001\u0000\u0000\u0000\u008a"+
		"\u0088\u0001\u0000\u0000\u0000\u008a\u008b\u0001\u0000\u0000\u0000\u008b"+
		"\u008d\u0001\u0000\u0000\u0000\u008c\u008a\u0001\u0000\u0000\u0000\u008d"+
		"\u008f\u0005!\u0000\u0000\u008e\u0085\u0001\u0000\u0000\u0000\u008e\u0086"+
		"\u0001\u0000\u0000\u0000\u008f\u001d\u0001\u0000\u0000\u0000\u0090\u0091"+
		"\u0005\u0003\u0000\u0000\u0091\u0092\u0005\u001e\u0000\u0000\u0092\u0093"+
		"\u0003\u0002\u0001\u0000\u0093\u0094\u0005\"\u0000\u0000\u0094\u0095\u0003"+
		"\u0018\f\u0000\u0095\u0096\u0005\"\u0000\u0000\u0096\u0097\u0003\u0002"+
		"\u0001\u0000\u0097\u0098\u0005\u001f\u0000\u0000\u0098\u009c\u0005 \u0000"+
		"\u0000\u0099\u009b\u0003\u0010\b\u0000\u009a\u0099\u0001\u0000\u0000\u0000"+
		"\u009b\u009e\u0001\u0000\u0000\u0000\u009c\u009a\u0001\u0000\u0000\u0000"+
		"\u009c\u009d\u0001\u0000\u0000\u0000\u009d\u009f\u0001\u0000\u0000\u0000"+
		"\u009e\u009c\u0001\u0000\u0000\u0000\u009f\u00a0\u0005!\u0000\u0000\u00a0"+
		"\u001f\u0001\u0000\u0000\u0000\u00a1\u00a2\u0005\u0003\u0000\u0000\u00a2"+
		"\u00a3\u0005\u001e\u0000\u0000\u00a3\u00a4\u0003\u0018\f\u0000\u00a4\u00a5"+
		"\u0005\u001f\u0000\u0000\u00a5\u00a9\u0005 \u0000\u0000\u00a6\u00a8\u0003"+
		"\u0010\b\u0000\u00a7\u00a6\u0001\u0000\u0000\u0000\u00a8\u00ab\u0001\u0000"+
		"\u0000\u0000\u00a9\u00a7\u0001\u0000\u0000\u0000\u00a9\u00aa\u0001\u0000"+
		"\u0000\u0000\u00aa\u00ac\u0001\u0000\u0000\u0000\u00ab\u00a9\u0001\u0000"+
		"\u0000\u0000\u00ac\u00ad\u0005!\u0000\u0000\u00ad!\u0001\u0000\u0000\u0000"+
		"\u000f\'0?GPYdkr}\u0082\u008a\u008e\u009c\u00a9";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}