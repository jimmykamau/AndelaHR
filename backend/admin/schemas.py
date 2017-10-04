from marshmallow import Schema, fields, ValidationError


def not_blank(data):
    if not data:
        raise ValidationError('Data not provided')


class UserSchema(Schema):
    """UserSchema for use with Marshmallow"""
    id = fields.Int(dump_only=True)
    full_name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
