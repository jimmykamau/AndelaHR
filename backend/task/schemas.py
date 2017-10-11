from marshmallow import Schema, fields


class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    task_type = fields.Int(required=True)


class TaskDetailSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    task_id = fields.Int(required=True)
    date_due = fields.DateTime(required=True)
