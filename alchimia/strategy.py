from __future__ import absolute_import, division

from sqlalchemy.engine.strategies import MockEngineStrategy

from alchimia.engine import TwistedEngine


TWISTED_STRATEGY = "_twisted"


class TwistedEngineStrategy(MockEngineStrategy):
    """
    An EngineStrategy for use with Twisted. Many of the Engine's methods will
    return Deferreds instead of results. See the documentation of
    ``TwistedEngine`` for more details.
    """

    name = TWISTED_STRATEGY
    engine_cls = TwistedEngine


TwistedEngineStrategy()
