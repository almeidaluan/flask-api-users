from marshmallow import Schema
from marshmallow.fields import Email, Str,Boolean
from apps.messages import MSG_FIELD_REQUIRED

class UserRegistrationSchema(Schema):
    full_name = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    email = Email(required=True,error_messages={'required':'Campo Obrigatorio'})
    password = Str(required=True,error_messages={'required': 'Campo Obrigatorio'})

class UserSchema(Schema):
    full_name = Str(required=True, error_messages={'required': 'Campo obrigatório'})
    email = Email(required=True, error_messages={'required': 'Campo obrigatório'})
    cpf_cnpj = Str()
    active = Boolean()
