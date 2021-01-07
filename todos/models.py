import datetime
import uuid

from pynamodb.models import Model
from pynamodb.attributes import (
    BooleanAttribute,
    UnicodeAttribute,
    UTCDateTimeAttribute
)


class Todo(Model):
    uid = UnicodeAttribute(hash_key=True, default=lambda: str(uuid.uuid4()))
    created = UTCDateTimeAttribute(default=datetime.datetime.now)
    started = BooleanAttribute(default=False)
    completed = BooleanAttribute(default=False)
    description = UnicodeAttribute()
    due_date = UTCDateTimeAttribute()    

    class Meta:
        table_name = 'todos'

    @property
    def overdue(self):
        """ Returns a boolean indicating if the todo is overdue """
        return datetime.datetime.now(self.due_date.tzinfo) > self.due_date
