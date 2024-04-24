from typing import Any, Generator, List as tList, Literal, Self, Tuple as tTuple, Union as tUnion
from sympy import Equality, Integral, Ne, Piecewise, Sum
from sympy.core.add import Add
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core.function import Lambda
from sympy.core.logic import And
from sympy.core.mul import Mul
from sympy.core.numbers import Integer
from sympy.core.relational import Eq, Relational
from sympy.core.symbol import Symbol
from sympy.logic.boolalg import Boolean
from sympy.matrices.immutable import ImmutableMatrix
from sympy.series.order import Order
from sympy.sets.conditionset import ConditionSet
from sympy.sets.fancysets import Range
from sympy.sets.sets import FiniteSet
from sympy.stats.crv_types import GammaDistribution, NormalDistribution
from sympy.stats.drv_types import PoissonDistribution
from sympy.stats.frv_types import BernoulliDistribution
from sympy.stats.joint_rv import JointDistribution, JointRandomSymbol
from sympy.stats.joint_rv_types import JointDistributionHandmade
from sympy.stats.symbolic_multivariate_probability import ExpectationMatrix
from sympy.stats.symbolic_probability import Expectation, Probability
from sympy.tensor.indexed import Indexed
from sympy.stats.rv import Density, Distribution, RandomIndexedSymbol, RandomSymbol, is_random

EmptySet = ...
__all__ = ['StochasticProcess', 'DiscreteTimeStochasticProcess', 'DiscreteMarkovChain', 'TransitionMatrixOf', 'StochasticStateSpaceOf', 'GeneratorMatrixOf', 'ContinuousMarkovChain', 'BernoulliProcess', 'PoissonProcess', 'WienerProcess', 'GammaProcess']
@is_random.register(Indexed)
def _(x) -> bool:
    ...

@is_random.register(RandomIndexedSymbol)
def _(x) -> Literal[True]:
    ...

class StochasticProcess(Basic):
    index_set = ...
    def __new__(cls, sym, state_space=..., **kwargs) -> Self:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    @property
    def state_space(self) -> tUnion[FiniteSet, Range]:
        ...
    
    def distribution(self, key=...) -> Distribution:
        ...
    
    def density(self, x) -> Density:
        ...
    
    def __call__(self, time):
        ...
    
    def __getitem__(self, time):
        ...
    
    def probability(self, condition):
        ...
    
    def joint_distribution(self, *args) -> JointDistribution | JointDistributionHandmade:
        ...
    
    def expectation(self, condition, given_condition):
        ...
    
    def sample(self):
        ...
    


class DiscreteTimeStochasticProcess(StochasticProcess):
    def __getitem__(self, time) -> RandomIndexedSymbol:
        ...
    


class ContinuousTimeStochasticProcess(StochasticProcess):
    def __call__(self, time) -> RandomIndexedSymbol:
        ...
    


class TransitionMatrixOf(Boolean):
    def __new__(cls, process, matrix) -> Self:
        ...
    
    process = ...
    matrix = ...


class GeneratorMatrixOf(TransitionMatrixOf):
    def __new__(cls, process, matrix) -> Self:
        ...
    


class StochasticStateSpaceOf(Boolean):
    def __new__(cls, process, state_space) -> Self:
        ...
    
    process = ...
    state_index = ...


class MarkovProcess(StochasticProcess):
    @property
    def number_of_states(self) -> tUnion[Integer, Symbol]:
        ...
    
    def replace_with_index(self, condition) -> Relational | Eq | Ne:
        ...
    
    def probability(self, condition, given_condition=..., evaluate=..., **kwargs):
        ...
    
    def expectation(self, expr, condition=..., evaluate=..., **kwargs) -> ExpectationMatrix | Expectation | int:
        ...
    


class DiscreteMarkovChain(DiscreteTimeStochasticProcess, MarkovProcess):
    index_set = ...
    def __new__(cls, sym, state_space=..., trans_probs=...) -> Self:
        ...
    
    @property
    def transition_probabilities(self) -> Basic:
        ...
    
    def communication_classes(self) -> tList[tTuple[tList[Basic], Boolean, Integer]]:
        ...
    
    def fundamental_matrix(self):
        ...
    
    def absorbing_probabilities(self) -> None:
        ...
    
    def absorbing_probabilites(self) -> None:
        ...
    
    def is_regular(self) -> And:
        ...
    
    def is_ergodic(self):
        ...
    
    def is_absorbing_state(self, state) -> bool | None:
        ...
    
    def is_absorbing_chain(self) -> And:
        ...
    
    def stationary_distribution(self, condition_set=...) -> tUnion[ImmutableMatrix, ConditionSet, Lambda]:
        ...
    
    def fixed_row_vector(self) -> ImmutableMatrix | ConditionSet | Lambda:
        ...
    
    @property
    def limiting_distribution(self) -> ImmutableMatrix | ConditionSet | Lambda:
        ...
    
    def decompose(self) -> tTuple[tList[Basic], ImmutableMatrix, ImmutableMatrix, ImmutableMatrix]:
        ...
    
    def canonical_form(self) -> tTuple[tList[Basic], ImmutableMatrix]:
        ...
    
    def sample(self) -> Generator[Basic, Any, None]:
        ...
    


class ContinuousMarkovChain(ContinuousTimeStochasticProcess, MarkovProcess):
    index_set = ...
    def __new__(cls, sym, state_space=..., gen_mat=...) -> Self:
        ...
    
    @property
    def generator_matrix(self) -> Basic:
        ...
    
    @cacheit
    def transition_probabilities(self, gen_mat=...) -> Lambda | None:
        ...
    
    def limiting_distribution(self) -> Lambda | ImmutableMatrix | None:
        ...
    


class BernoulliProcess(DiscreteTimeStochasticProcess):
    index_set = ...
    def __new__(cls, sym, p, success=..., failure=...) -> Self:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    @property
    def p(self) -> Basic:
        ...
    
    @property
    def success(self) -> Basic:
        ...
    
    @property
    def failure(self) -> Basic:
        ...
    
    @property
    def state_space(self) -> FiniteSet:
        ...
    
    def distribution(self, key=...) -> BernoulliDistribution:
        ...
    
    def simple_rv(self, rv) -> RandomSymbol:
        ...
    
    def expectation(self, expr, condition=..., evaluate=..., **kwargs) -> Order | tuple[Any, ...] | Sum | Any | Piecewise | Basic | Equality | Relational | Ne | Integral | bool | None:
        ...
    
    def probability(self, condition, given_condition=..., evaluate=..., **kwargs) -> BernoulliDistribution | Probability | Any | Equality | Lambda | Order | Relational | Ne | int:
        ...
    
    def density(self, x) -> Piecewise:
        ...
    


class _SubstituteRV:
    ...


def get_timerv_swaps(expr, condition) -> tuple[list[Any], dict[Any, Any]]:
    ...

class CountingProcess(ContinuousTimeStochasticProcess):
    index_set = ...
    @property
    def symbol(self) -> Basic:
        ...
    
    def expectation(self, expr, condition=..., evaluate=..., **kwargs) -> Add | ExpectationMatrix | Expectation | Order | tuple[Any, ...] | Sum | Any | Piecewise | Basic | Equality | Relational | Ne | Integral | bool | None:
        ...
    
    def probability(self, condition, given_condition=..., evaluate=..., **kwargs) -> Add | Mul | Probability | BernoulliDistribution | Any | Equality | Lambda | Order | Relational | Ne | int:
        ...
    


class PoissonProcess(CountingProcess):
    def __new__(cls, sym, lamda) -> Self:
        ...
    
    @property
    def lamda(self) -> Basic:
        ...
    
    @property
    def state_space(self):
        ...
    
    def distribution(self, key) -> PoissonDistribution:
        ...
    
    def density(self, x):
        ...
    
    def simple_rv(self, rv) -> RandomSymbol:
        ...
    
    def __add__(self, other) -> PoissonProcess:
        ...
    
    def split(self, l1, l2) -> tuple[PoissonProcess, PoissonProcess]:
        ...
    


class WienerProcess(CountingProcess):
    def __new__(cls, sym) -> Self:
        ...
    
    @property
    def state_space(self):
        ...
    
    def distribution(self, key) -> NormalDistribution:
        ...
    
    def density(self, x):
        ...
    
    def simple_rv(self, rv) -> RandomSymbol | JointRandomSymbol:
        ...
    


class GammaProcess(CountingProcess):
    def __new__(cls, sym, lamda, gamma) -> Self:
        ...
    
    @property
    def lamda(self) -> Basic:
        ...
    
    @property
    def gamma(self) -> Basic:
        ...
    
    @property
    def state_space(self) -> FiniteSet:
        ...
    
    def distribution(self, key) -> GammaDistribution:
        ...
    
    def density(self, x):
        ...
    
    def simple_rv(self, rv) -> RandomSymbol:
        ...
    


