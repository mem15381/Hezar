from typing import List

from ...constants import Backends
from ...utils import verify_dependencies


class DummyObject(type):
    """
    Metaclass for the dummy objects. Any class inheriting from it will return the ImportError generated by
    `requires_backend` each time a user tries to access any method of that class.
    """
    _required_backends: List[Backends]
    _module: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        verify_dependencies(self, self._required_backends)

    def __getattr__(cls, key):
        cls()