
from ._decorators import (
    ThreadsafeIter,
    lazy_property
)
try:
    del _decorators
except NameError:
    pass
