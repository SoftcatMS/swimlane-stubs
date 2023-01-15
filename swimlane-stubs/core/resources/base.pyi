from swimlane.core.resolver import SwimlaneResolver as SwimlaneResolver

class APIResourceMetaclass(type):
    def __call__(cls, *args, **kwargs): ...

class APIResource:
    def __init__(self, swimlane, raw) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def get_cache_internal_key(self): ...
    def get_cache_index_keys(self) -> None: ...