from marshmallow import Schema, fields


class TodoSerializer(Schema):
    started = fields.Boolean()
    completed = fields.Boolean()
    description = fields.String(required=True)
    due_date = fields.DateTime(required=True)
