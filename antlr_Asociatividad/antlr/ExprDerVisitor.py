# Generated from ExprDer.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprDerParser import ExprDerParser
else:
    from ExprDerParser import ExprDerParser

# This class defines a complete generic visitor for a parse tree produced by ExprDerParser.

class ExprDerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprDerParser#prog.
    def visitProg(self, ctx:ExprDerParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprDerParser#PowRight.
    def visitPowRight(self, ctx:ExprDerParser.PowRightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprDerParser#Parens.
    def visitParens(self, ctx:ExprDerParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprDerParser#MulDivRight.
    def visitMulDivRight(self, ctx:ExprDerParser.MulDivRightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprDerParser#AddSubRight.
    def visitAddSubRight(self, ctx:ExprDerParser.AddSubRightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprDerParser#Int.
    def visitInt(self, ctx:ExprDerParser.IntContext):
        return self.visitChildren(ctx)



del ExprDerParser