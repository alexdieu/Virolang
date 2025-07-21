# Generated from parser/Virolang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .VirolangParser import VirolangParser
else:
    from VirolangParser import VirolangParser

# This class defines a complete generic visitor for a parse tree produced by VirolangParser.

class VirolangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VirolangParser#prog.
    def visitProg(self, ctx:VirolangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VirolangParser#stat.
    def visitStat(self, ctx:VirolangParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VirolangParser#assignment.
    def visitAssignment(self, ctx:VirolangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VirolangParser#calibrateExpr.
    def visitCalibrateExpr(self, ctx:VirolangParser.CalibrateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VirolangParser#createExpr.
    def visitCreateExpr(self, ctx:VirolangParser.CreateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VirolangParser#designExpr.
    def visitDesignExpr(self, ctx:VirolangParser.DesignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VirolangParser#loadGenomeExpr.
    def visitLoadGenomeExpr(self, ctx:VirolangParser.LoadGenomeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VirolangParser#infectExpr.
    def visitInfectExpr(self, ctx:VirolangParser.InfectExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VirolangParser#idExpr.
    def visitIdExpr(self, ctx:VirolangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VirolangParser#type.
    def visitType(self, ctx:VirolangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VirolangParser#param.
    def visitParam(self, ctx:VirolangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VirolangParser#value.
    def visitValue(self, ctx:VirolangParser.ValueContext):
        return self.visitChildren(ctx)



del VirolangParser