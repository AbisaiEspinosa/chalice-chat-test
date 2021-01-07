import inspect

from pynamodb.models import Model

from . import models


cls_members = inspect.getmembers(models, inspect.isclass)

for name, obj in cls_members:
    if issubclass(obj, Model) and name != 'Model':
        if not obj.exists():
            obj.create_table(
                read_capacity_units=1,
                write_capacity_units=1,
                wait=True
            )
