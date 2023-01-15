from .base import MultiSelectField as MultiSelectField
from _typeshed import Incomplete
from swimlane.exceptions import ValidationError as ValidationError

class ValuesListField(MultiSelectField):
    field_type: Incomplete
    supported_types: Incomplete
    selection_to_id_map: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def validate_value(self, value) -> None: ...
    def get_batch_representation(self): ...
    def cast_to_python(self, value): ...
    def cast_to_swimlane(self, value): ...
    def cast_to_report(self, value): ...
    def cast_to_bulk_modify(self, value): ...