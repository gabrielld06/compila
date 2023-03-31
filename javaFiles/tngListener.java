// Generated from tng.g4 by ANTLR 4.12.0
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link tngParser}.
 */
public interface tngListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link tngParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(tngParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(tngParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#atribuicao}.
	 * @param ctx the parse tree
	 */
	void enterAtribuicao(tngParser.AtribuicaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#atribuicao}.
	 * @param ctx the parse tree
	 */
	void exitAtribuicao(tngParser.AtribuicaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#declaracao}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracao(tngParser.DeclaracaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#declaracao}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracao(tngParser.DeclaracaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#chamada_print}.
	 * @param ctx the parse tree
	 */
	void enterChamada_print(tngParser.Chamada_printContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#chamada_print}.
	 * @param ctx the parse tree
	 */
	void exitChamada_print(tngParser.Chamada_printContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(tngParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(tngParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(tngParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(tngParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#number}.
	 * @param ctx the parse tree
	 */
	void enterNumber(tngParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#number}.
	 * @param ctx the parse tree
	 */
	void exitNumber(tngParser.NumberContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(tngParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(tngParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComando(tngParser.ComandoContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComando(tngParser.ComandoContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#inicio}.
	 * @param ctx the parse tree
	 */
	void enterInicio(tngParser.InicioContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#inicio}.
	 * @param ctx the parse tree
	 */
	void exitInicio(tngParser.InicioContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#expr_bool}.
	 * @param ctx the parse tree
	 */
	void enterExpr_bool(tngParser.Expr_boolContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#expr_bool}.
	 * @param ctx the parse tree
	 */
	void exitExpr_bool(tngParser.Expr_boolContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#fator_bool}.
	 * @param ctx the parse tree
	 */
	void enterFator_bool(tngParser.Fator_boolContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#fator_bool}.
	 * @param ctx the parse tree
	 */
	void exitFator_bool(tngParser.Fator_boolContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#cond}.
	 * @param ctx the parse tree
	 */
	void enterCond(tngParser.CondContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#cond}.
	 * @param ctx the parse tree
	 */
	void exitCond(tngParser.CondContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#if_bloco}.
	 * @param ctx the parse tree
	 */
	void enterIf_bloco(tngParser.If_blocoContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#if_bloco}.
	 * @param ctx the parse tree
	 */
	void exitIf_bloco(tngParser.If_blocoContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#else_bloco}.
	 * @param ctx the parse tree
	 */
	void enterElse_bloco(tngParser.Else_blocoContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#else_bloco}.
	 * @param ctx the parse tree
	 */
	void exitElse_bloco(tngParser.Else_blocoContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#for_bloco}.
	 * @param ctx the parse tree
	 */
	void enterFor_bloco(tngParser.For_blocoContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#for_bloco}.
	 * @param ctx the parse tree
	 */
	void exitFor_bloco(tngParser.For_blocoContext ctx);
	/**
	 * Enter a parse tree produced by {@link tngParser#while_bloco}.
	 * @param ctx the parse tree
	 */
	void enterWhile_bloco(tngParser.While_blocoContext ctx);
	/**
	 * Exit a parse tree produced by {@link tngParser#while_bloco}.
	 * @param ctx the parse tree
	 */
	void exitWhile_bloco(tngParser.While_blocoContext ctx);
}