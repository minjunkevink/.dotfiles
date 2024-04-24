from typing import Any, Callable, Literal, Self
from sympy.core import Expr
from sympy.core.function import UndefinedFunction

def add_formulae(formulae) -> None:
    ...

def add_meijerg_formulae(formulae) -> None:
    ...

def make_simp(z) -> Callable[..., Any]:
    ...

def debug(*args) -> None:
    ...

class Hyper_Function(Expr):
    def __new__(cls, ap, bq) -> Self:
        ...
    
    @property
    def args(self) -> tuple[Any, Any]:
        ...
    
    @property
    def sizes(self) -> tuple[int, int]:
        ...
    
    @property
    def gamma(self) -> int:
        ...
    
    def __call__(self, arg) -> type[UndefinedFunction]:
        ...
    
    def build_invariants(self) -> tuple[int, tuple[tuple[Any, int], ...], tuple[tuple[Any, int], ...]]:
        ...
    
    def difficulty(self, func) -> Literal[-1, 0]:
        ...
    


class G_Function(Expr):
    def __new__(cls, an, ap, bm, bq) -> Self:
        ...
    
    @property
    def args(self) -> tuple[Any, Any, Any, Any]:
        ...
    
    def __call__(self, z) -> type[UndefinedFunction]:
        ...
    
    def compute_buckets(self) -> tuple[dict[Any, list[Any]], ...]:
        ...
    
    @property
    def signature(self) -> tuple[int, int, int, int]:
        ...
    


_x = ...
class Formula:
    def __init__(self, func, z, res, symbols, B=..., C=..., M=...) -> None:
        ...
    
    @property
    def closed_form(self):
        ...
    
    def find_instantiations(self, func) -> list[Any]:
        ...
    


class FormulaCollection:
    def __init__(self) -> None:
        ...
    
    def lookup_origin(self, func) -> Formula | None:
        ...
    


class MeijerFormula:
    def __init__(self, an, ap, bm, bq, z, symbols, B, C, M, matcher) -> None:
        ...
    
    @property
    def closed_form(self):
        ...
    
    def try_instantiate(self, func) -> MeijerFormula | None:
        ...
    


class MeijerFormulaCollection:
    def __init__(self) -> None:
        ...
    
    def lookup_origin(self, func) -> None:
        ...
    


class Operator:
    def apply(self, obj, op):
        ...
    


class MultOperator(Operator):
    def __init__(self, p) -> None:
        ...
    


class ShiftA(Operator):
    def __init__(self, ai) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class ShiftB(Operator):
    def __init__(self, bi) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class UnShiftA(Operator):
    def __init__(self, ap, bq, i, z) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class UnShiftB(Operator):
    def __init__(self, ap, bq, i, z) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerShiftA(Operator):
    def __init__(self, bi) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerShiftB(Operator):
    def __init__(self, bi) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerShiftC(Operator):
    def __init__(self, bi) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerShiftD(Operator):
    def __init__(self, bi) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerUnShiftA(Operator):
    def __init__(self, an, ap, bm, bq, i, z) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerUnShiftB(Operator):
    def __init__(self, an, ap, bm, bq, i, z) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerUnShiftC(Operator):
    def __init__(self, an, ap, bm, bq, i, z) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerUnShiftD(Operator):
    def __init__(self, an, ap, bm, bq, i, z) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class ReduceOrder(Operator):
    def __new__(cls, ai, bj) -> Self | None:
        ...
    
    @classmethod
    def meijer_minus(cls, b, a) -> Self | None:
        ...
    
    @classmethod
    def meijer_plus(cls, a, b) -> Self | None:
        ...
    
    def __str__(self) -> str:
        ...
    


def reduce_order(func) -> tuple[Hyper_Function, list[Any]]:
    ...

def reduce_order_meijer(func) -> tuple[G_Function, list[Any]]:
    ...

def make_derivative_operator(M, z) -> Callable[..., Any]:
    ...

def apply_operators(obj, ops, op):
    ...

def devise_plan(target, origin, z) -> list[Any]:
    ...

def try_shifted_sum(func, z) -> tuple[Hyper_Function, list[Any], Any | int] | None:
    ...

def try_polynomial(func, z) -> None:
    ...

def try_lerchphi(func) -> Formula | None:
    ...

def build_hypergeometric_formula(func) -> Formula:
    ...

def hyperexpand_special(ap, bq, z) -> type[UndefinedFunction]:
    ...

_collection = ...
def devise_plan_meijer(fro, to, z) -> list[Any]:
    ...

_meijercollection = ...
def hyperexpand(f, allow_hyper=..., rewrite=..., place=...):
    ...

