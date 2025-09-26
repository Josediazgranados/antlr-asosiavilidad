from ExprIzqVisitor import ExprIzqVisitor
from ExprDerVisitor import ExprDerVisitor

class EvalIzqVisitor(ExprIzqVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            return left * right
        else:
            return left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    def visitInt(self, ctx):
        return int(ctx.getText())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

class EvalDerVisitor(ExprDerVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    def visitMulDivRight(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            return left * right
        else:
            return left / right

    def visitAddSubRight(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    def visitPowRight(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left ** right

    def visitInt(self, ctx):
        return int(ctx.getText())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
