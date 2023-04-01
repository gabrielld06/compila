
@echo off
set arg=%1

if %arg%==compile (
    java -jar antlr-4.12.0-complete.jar *.g4 -Dlanguage=Python3 -visitor
)
if %arg%==tree (
    java -jar antlr-4.12.0-complete.jar tng.g4 -visitor
    javac *.java -cp antlr-4.12.0-complete.jar
    move /Y *.class javaFiles/
    move /Y *.java javaFiles/
    java -cp antlr-4.12.0-complete.jar;./javaFiles org.antlr.v4.gui.TestRig tng inicio tests/test.tng -gui
)
if %arg%==help (
    echo %~nx0 compile - Gera os arquivos com a ferramenta
    echo %~nx0 tree - exibe a arvore 
)