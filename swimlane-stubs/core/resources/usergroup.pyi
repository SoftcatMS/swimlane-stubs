from typing import Any, Dict, List, Optional, TypedDict

from swimlane.core.client import Swimlane
from swimlane.core.cursor import Cursor as Cursor
from swimlane.core.resolver import SwimlaneResolver as SwimlaneResolver
from swimlane.core.resources.base import APIResource as APIResource

class UserGroupForJson(TypedDict):
    id: str
    name: str

class UserGroup(APIResource):
    id: str
    name: str
    def __init__(self, swimlane: Swimlane, raw: Dict[str, Any]) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other: Any): ...
    def __lt__(self, other: Any): ...
    def resolve(self): ...
    def as_usergroup_selection(self): ...
    def for_json(self) -> UserGroupForJson: ...

class Group(UserGroup):
    description: Optional[str]

    def __init__(self, swimlane: Swimlane, raw: Dict[str, Any]) -> None: ...
    @property
    def users(self): ...
    def get_cache_index_keys(self): ...

class User(UserGroup):
    username: str
    display_name: str
    email: str
    def __init__(self, swimlane: Swimlane, raw) -> None: ...
    def get_cache_index_keys(self): ...

class GroupUsersCursor(SwimlaneResolver, Cursor):
    def __init__(self, swimlane: Swimlane, user_ids: List[str]) -> None: ...
