from marshmallow import Schema, fields


class TodoSerializer(Schema):
    uid = fields.String(dump_only=True)
    created = fields.DateTime(dump_only=True)
    started = fields.Boolean()
    completed = fields.Boolean()
    overdue = fields.Boolean(dump_only=True)
    description = fields.String(required=True)
    due_date = fields.DateTime(required=True)
