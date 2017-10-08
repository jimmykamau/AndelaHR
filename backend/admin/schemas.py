from marshmallow import Schema, fields


class AdminSchema(Schema):
    id = fields.Int(dump_only=True)
    full_name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    user_id = fields.Int(dump_only=True)
