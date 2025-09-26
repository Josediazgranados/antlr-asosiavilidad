# Generated from ExprIzq.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprIzqParser import ExprIzqParser
else:
    from ExprIzqParser import ExprIzqParser

# This class defines a complete listener for a parse tree produced by ExprIzqParser.
class ExprIzqListener(ParseTreeListener):

    # Enter a parse tree produced by ExprIzqParser#prog.
    def enterProg(self, ctx:ExprIzqParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprIzqParser#prog.
    def exitProg(self, ctx:ExprIzqParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprIzqParser#MulDiv.
    def enterMulDiv(self, ctx:ExprIzqParser.MulDivContext):
        pass

    # Exit a parse tree produced by ExprIzqParser#MulDiv.
    def exitMulDiv(self, ctx:ExprIzqParser.MulDivContext):
        pass


    # Enter a parse tree produced by ExprIzqParser#AddSub.
    def enterAddSub(self, ctx:ExprIzqParser.AddSubContext):
        pass

    # Exit a parse tree produced by ExprIzqParser#AddSub.
    def exitAddSub(self, ctx:ExprIzqParser.AddSubContext):
        pass


    # Enter a parse tree produced by ExprIzqParser#Parens.
    def enterParens(self, ctx:ExprIzqParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprIzqParser#Parens.
    def exitParens(self, ctx:ExprIzqParser.ParensContext):
        pass


    # Enter a parse tree produced by ExprIzqParser#Int.
    def enterInt(self, ctx:ExprIzqParser.IntContext):
        pass

    # Exit a parse tree produced by ExprIzqParser#Int.
    def exitInt(self, ctx:ExprIzqParser.IntContext):
        pass



del ExprIzqParser