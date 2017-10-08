from marshmallow import Schema, fields


class UserSchema(Schema):
    """UserSchema for use with Marshmallow"""
    id = fields.Int(dump_only=True)
    full_name = fields.Str(required=True)
    email = fields.Email(required=True)
