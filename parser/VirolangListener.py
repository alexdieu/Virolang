# Generated from parser/Virolang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .VirolangParser import VirolangParser
else:
    from VirolangParser import VirolangParser

# This class defines a complete listener for a parse tree produced by VirolangParser.
class VirolangListener(ParseTreeListener):

    # Enter a parse tree produced by VirolangParser#prog.
    def enterProg(self, ctx:VirolangParser.ProgContext):
        pass

    # Exit a parse tree produced by VirolangParser#prog.
    def exitProg(self, ctx:VirolangParser.ProgContext):
        pass


    # Enter a parse tree produced by VirolangParser#stat.
    def enterStat(self, ctx:VirolangParser.StatContext):
        pass

    # Exit a parse tree produced by VirolangParser#stat.
    def exitStat(self, ctx:VirolangParser.StatContext):
        pass


    # Enter a parse tree produced by VirolangParser#assignment.
    def enterAssignment(self, ctx:VirolangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by VirolangParser#assignment.
    def exitAssignment(self, ctx:VirolangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by VirolangParser#calibrateExpr.
    def enterCalibrateExpr(self, ctx:VirolangParser.CalibrateExprContext):
        pass

    # Exit a parse tree produced by VirolangParser#calibrateExpr.
    def exitCalibrateExpr(self, ctx:VirolangParser.CalibrateExprContext):
        pass


    # Enter a parse tree produced by VirolangParser#createExpr.
    def enterCreateExpr(self, ctx:VirolangParser.CreateExprContext):
        pass

    # Exit a parse tree produced by VirolangParser#createExpr.
    def exitCreateExpr(self, ctx:VirolangParser.CreateExprContext):
        pass


    # Enter a parse tree produced by VirolangParser#designExpr.
    def enterDesignExpr(self, ctx:VirolangParser.DesignExprContext):
        pass

    # Exit a parse tree produced by VirolangParser#designExpr.
    def exitDesignExpr(self, ctx:VirolangParser.DesignExprContext):
        pass


    # Enter a parse tree produced by VirolangParser#loadGenomeExpr.
    def enterLoadGenomeExpr(self, ctx:VirolangParser.LoadGenomeExprContext):
        pass

    # Exit a parse tree produced by VirolangParser#loadGenomeExpr.
    def exitLoadGenomeExpr(self, ctx:VirolangParser.LoadGenomeExprContext):
        pass


    # Enter a parse tree produced by VirolangParser#infectExpr.
    def enterInfectExpr(self, ctx:VirolangParser.InfectExprContext):
        pass

    # Exit a parse tree produced by VirolangParser#infectExpr.
    def exitInfectExpr(self, ctx:VirolangParser.InfectExprContext):
        pass


    # Enter a parse tree produced by VirolangParser#idExpr.
    def enterIdExpr(self, ctx:VirolangParser.IdExprContext):
        pass

    # Exit a parse tree produced by VirolangParser#idExpr.
    def exitIdExpr(self, ctx:VirolangParser.IdExprContext):
        pass


    # Enter a parse tree produced by VirolangParser#type.
    def enterType(self, ctx:VirolangParser.TypeContext):
        pass

    # Exit a parse tree produced by VirolangParser#type.
    def exitType(self, ctx:VirolangParser.TypeContext):
        pass


    # Enter a parse tree produced by VirolangParser#param.
    def enterParam(self, ctx:VirolangParser.ParamContext):
        pass

    # Exit a parse tree produced by VirolangParser#param.
    def exitParam(self, ctx:VirolangParser.ParamContext):
        pass


    # Enter a parse tree produced by VirolangParser#value.
    def enterValue(self, ctx:VirolangParser.ValueContext):
        pass

    # Exit a parse tree produced by VirolangParser#value.
    def exitValue(self, ctx:VirolangParser.ValueContext):
        pass



del VirolangParser