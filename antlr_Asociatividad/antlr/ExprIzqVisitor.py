# Generated from ExprLeft.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprLeftParser import ExprLeftParser
else:
    from ExprLeftParser import ExprLeftParser

# This class defines a complete generic visitor for a parse tree produced by ExprLeftParser.

class ExprLeftVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprLeftParser#prog.
    def visitProg(self, ctx:ExprLeftParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprLeftParser#MulDiv.
    def visitMulDiv(self, ctx:ExprLeftParser.MulDivContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprLeftParser#AddSub.
    def visitAddSub(self, ctx:ExprLeftParser.AddSubContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprLeftParser#Parens.
    def visitParens(self, ctx:ExprLeftParser.ParensContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprLeftParser#Int.
    def visitInt(self, ctx:ExprLeftParser.IntContext):
        return self.visitChildren(ctx)


del ExprLeftParser

