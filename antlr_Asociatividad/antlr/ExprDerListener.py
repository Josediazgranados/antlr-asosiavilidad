# Generated from ExprDer.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprDerParser import ExprDerParser
else:
    from ExprDerParser import ExprDerParser

# This class defines a complete listener for a parse tree produced by ExprDerParser.
class ExprDerListener(ParseTreeListener):

    # Enter a parse tree produced by ExprDerParser#prog.
    def enterProg(self, ctx:ExprDerParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprDerParser#prog.
    def exitProg(self, ctx:ExprDerParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprDerParser#PowRight.
    def enterPowRight(self, ctx:ExprDerParser.PowRightContext):
        pass

    # Exit a parse tree produced by ExprDerParser#PowRight.
    def exitPowRight(self, ctx:ExprDerParser.PowRightContext):
        pass


    # Enter a parse tree produced by ExprDerParser#Parens.
    def enterParens(self, ctx:ExprDerParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprDerParser#Parens.
    def exitParens(self, ctx:ExprDerParser.ParensContext):
        pass


    # Enter a parse tree produced by ExprDerParser#MulDivRight.
    def enterMulDivRight(self, ctx:ExprDerParser.MulDivRightContext):
        pass

    # Exit a parse tree produced by ExprDerParser#MulDivRight.
    def exitMulDivRight(self, ctx:ExprDerParser.MulDivRightContext):
        pass


    # Enter a parse tree produced by ExprDerParser#AddSubRight.
    def enterAddSubRight(self, ctx:ExprDerParser.AddSubRightContext):
        pass

    # Exit a parse tree produced by ExprDerParser#AddSubRight.
    def exitAddSubRight(self, ctx:ExprDerParser.AddSubRightContext):
        pass


    # Enter a parse tree produced by ExprDerParser#Int.
    def enterInt(self, ctx:ExprDerParser.IntContext):
        pass

    # Exit a parse tree produced by ExprDerParser#Int.
    def exitInt(self, ctx:ExprDerParser.IntContext):
        pass



del ExprDerParser