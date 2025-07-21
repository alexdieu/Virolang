# Generated from parser/Virolang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,37,8,3,10,3,12,3,40,9,3,3,
        3,42,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,51,8,3,10,3,12,3,54,9,3,
        3,3,56,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,65,8,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,5,3,76,8,3,10,3,12,3,79,9,3,1,4,1,4,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,94,8,6,10,6,12,6,97,9,
        6,3,6,99,8,6,1,6,1,6,3,6,103,8,6,1,6,0,1,6,7,0,2,4,6,8,10,12,0,1,
        1,0,11,13,113,0,17,1,0,0,0,2,22,1,0,0,0,4,25,1,0,0,0,6,64,1,0,0,
        0,8,80,1,0,0,0,10,82,1,0,0,0,12,102,1,0,0,0,14,16,3,2,1,0,15,14,
        1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,
        19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,23,3,4,2,0,23,24,5,1,
        0,0,24,3,1,0,0,0,25,26,5,17,0,0,26,27,5,2,0,0,27,28,3,6,3,0,28,5,
        1,0,0,0,29,30,6,3,-1,0,30,31,5,3,0,0,31,32,3,8,4,0,32,41,5,4,0,0,
        33,38,3,10,5,0,34,35,5,5,0,0,35,37,3,10,5,0,36,34,1,0,0,0,37,40,
        1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,
        41,33,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,44,5,6,0,0,44,65,1,
        0,0,0,45,46,5,8,0,0,46,55,5,4,0,0,47,52,3,10,5,0,48,49,5,5,0,0,49,
        51,3,10,5,0,50,48,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,
        0,0,53,56,1,0,0,0,54,52,1,0,0,0,55,47,1,0,0,0,55,56,1,0,0,0,56,57,
        1,0,0,0,57,65,5,6,0,0,58,59,5,9,0,0,59,60,5,4,0,0,60,61,3,10,5,0,
        61,62,5,6,0,0,62,65,1,0,0,0,63,65,5,17,0,0,64,29,1,0,0,0,64,45,1,
        0,0,0,64,58,1,0,0,0,64,63,1,0,0,0,65,77,1,0,0,0,66,67,10,5,0,0,67,
        68,5,7,0,0,68,76,3,6,3,6,69,70,10,2,0,0,70,71,5,10,0,0,71,72,5,4,
        0,0,72,73,3,10,5,0,73,74,5,6,0,0,74,76,1,0,0,0,75,66,1,0,0,0,75,
        69,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,7,1,0,0,
        0,79,77,1,0,0,0,80,81,7,0,0,0,81,9,1,0,0,0,82,83,5,17,0,0,83,84,
        5,14,0,0,84,85,3,12,6,0,85,11,1,0,0,0,86,103,5,18,0,0,87,103,5,19,
        0,0,88,103,5,20,0,0,89,98,5,15,0,0,90,95,3,12,6,0,91,92,5,5,0,0,
        92,94,3,12,6,0,93,91,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,
        0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,98,90,1,0,0,0,98,99,1,0,0,0,99,
        100,1,0,0,0,100,103,5,16,0,0,101,103,5,17,0,0,102,86,1,0,0,0,102,
        87,1,0,0,0,102,88,1,0,0,0,102,89,1,0,0,0,102,101,1,0,0,0,103,13,
        1,0,0,0,11,17,38,41,52,55,64,75,77,95,98,102
    ]

class VirolangParser ( Parser ):

    grammarFileName = "Virolang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'create'", "'('", "','", 
                     "')'", "'!'", "'design'", "'load_genome'", "'calibrate'", 
                     "'virus'", "'host'", "'population'", "':'", "'['", 
                     "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "STRING", "NUMBER", "BOOL", "WS", 
                      "COMMENT" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_type = 4
    RULE_param = 5
    RULE_value = 6

    ruleNames =  [ "prog", "stat", "assignment", "expression", "type", "param", 
                   "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    ID=17
    STRING=18
    NUMBER=19
    BOOL=20
    WS=21
    COMMENT=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(VirolangParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VirolangParser.StatContext)
            else:
                return self.getTypedRuleContext(VirolangParser.StatContext,i)


        def getRuleIndex(self):
            return VirolangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = VirolangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 14
                self.stat()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(VirolangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(VirolangParser.AssignmentContext,0)


        def getRuleIndex(self):
            return VirolangParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = VirolangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.assignment()
            self.state = 23
            self.match(VirolangParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VirolangParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(VirolangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return VirolangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = VirolangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(VirolangParser.ID)
            self.state = 26
            self.match(VirolangParser.T__1)
            self.state = 27
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VirolangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CalibrateExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VirolangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(VirolangParser.ExpressionContext,0)

        def param(self):
            return self.getTypedRuleContext(VirolangParser.ParamContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalibrateExpr" ):
                listener.enterCalibrateExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalibrateExpr" ):
                listener.exitCalibrateExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalibrateExpr" ):
                return visitor.visitCalibrateExpr(self)
            else:
                return visitor.visitChildren(self)


    class CreateExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VirolangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(VirolangParser.TypeContext,0)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VirolangParser.ParamContext)
            else:
                return self.getTypedRuleContext(VirolangParser.ParamContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateExpr" ):
                listener.enterCreateExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateExpr" ):
                listener.exitCreateExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateExpr" ):
                return visitor.visitCreateExpr(self)
            else:
                return visitor.visitChildren(self)


    class DesignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VirolangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VirolangParser.ParamContext)
            else:
                return self.getTypedRuleContext(VirolangParser.ParamContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDesignExpr" ):
                listener.enterDesignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDesignExpr" ):
                listener.exitDesignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDesignExpr" ):
                return visitor.visitDesignExpr(self)
            else:
                return visitor.visitChildren(self)


    class LoadGenomeExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VirolangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def param(self):
            return self.getTypedRuleContext(VirolangParser.ParamContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadGenomeExpr" ):
                listener.enterLoadGenomeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadGenomeExpr" ):
                listener.exitLoadGenomeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadGenomeExpr" ):
                return visitor.visitLoadGenomeExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfectExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VirolangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VirolangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(VirolangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfectExpr" ):
                listener.enterInfectExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfectExpr" ):
                listener.exitInfectExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfectExpr" ):
                return visitor.visitInfectExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VirolangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(VirolangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VirolangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = VirolangParser.CreateExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 30
                self.match(VirolangParser.T__2)
                self.state = 31
                self.type_()
                self.state = 32
                self.match(VirolangParser.T__3)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 33
                    self.param()
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 34
                        self.match(VirolangParser.T__4)
                        self.state = 35
                        self.param()
                        self.state = 40
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 43
                self.match(VirolangParser.T__5)
                pass
            elif token in [8]:
                localctx = VirolangParser.DesignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(VirolangParser.T__7)
                self.state = 46
                self.match(VirolangParser.T__3)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 47
                    self.param()
                    self.state = 52
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 48
                        self.match(VirolangParser.T__4)
                        self.state = 49
                        self.param()
                        self.state = 54
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 57
                self.match(VirolangParser.T__5)
                pass
            elif token in [9]:
                localctx = VirolangParser.LoadGenomeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.match(VirolangParser.T__8)
                self.state = 59
                self.match(VirolangParser.T__3)
                self.state = 60
                self.param()
                self.state = 61
                self.match(VirolangParser.T__5)
                pass
            elif token in [17]:
                localctx = VirolangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(VirolangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 75
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = VirolangParser.InfectExprContext(self, VirolangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 66
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 67
                        self.match(VirolangParser.T__6)
                        self.state = 68
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = VirolangParser.CalibrateExprContext(self, VirolangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 69
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 70
                        self.match(VirolangParser.T__9)
                        self.state = 71
                        self.match(VirolangParser.T__3)
                        self.state = 72
                        self.param()
                        self.state = 73
                        self.match(VirolangParser.T__5)
                        pass

             
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VirolangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = VirolangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VirolangParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(VirolangParser.ValueContext,0)


        def getRuleIndex(self):
            return VirolangParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = VirolangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(VirolangParser.ID)
            self.state = 83
            self.match(VirolangParser.T__13)
            self.state = 84
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(VirolangParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(VirolangParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(VirolangParser.BOOL, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VirolangParser.ValueContext)
            else:
                return self.getTypedRuleContext(VirolangParser.ValueContext,i)


        def ID(self):
            return self.getToken(VirolangParser.ID, 0)

        def getRuleIndex(self):
            return VirolangParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = VirolangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(VirolangParser.STRING)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(VirolangParser.NUMBER)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(VirolangParser.BOOL)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.match(VirolangParser.T__14)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1998848) != 0):
                    self.state = 90
                    self.value()
                    self.state = 95
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 91
                        self.match(VirolangParser.T__4)
                        self.state = 92
                        self.value()
                        self.state = 97
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 100
                self.match(VirolangParser.T__15)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 101
                self.match(VirolangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




