from swimlane.core.cursor import Cursor as Cursor
from swimlane.core.resolver import SwimlaneResolver as SwimlaneResolver
from swimlane.core.resources.base import APIResource as APIResource

class UserGroup(APIResource):
    id: str
    name: str
    def __init__(self, swimlane, raw) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def resolve(self): ...
    def as_usergroup_selection(self): ...
    def for_json(self): ...

class Group(UserGroup):
    description: str
    def __init__(self, swimlane, raw) -> None: ...
    @property
    def users(self): ...
    def get_cache_index_keys(self): ...

class User(UserGroup):
    username: str
    display_name: str
    email: str
    def __init__(self, swimlane, raw) -> None: ...
    def get_cache_index_keys(self): ...

class GroupUsersCursor(SwimlaneResolver, Cursor):
    def __init__(self, swimlane, user_ids) -> None: ...
