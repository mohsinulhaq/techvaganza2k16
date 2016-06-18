# from flask_security.forms import ConfirmRegisterForm, Required
from wtforms import *
from wtforms.validators import *

# class ExtendedConfirmRegisterForm(ConfirmRegisterForm):


class RegistrationForm(Form):
    first_name = StringField('First Name', [DataRequired()])
    last_name = StringField('Last Name', [DataRequired()])
    cell = StringField('Telephone',
                       [Length(min=10, max=10,
                               message='Not a valid Phone number')])
    gender = StringField('Gender',
                         [DataRequired(),
                          AnyOf(['Male', 'Female', 'male', 'female'],
                                message='Please Enter Male or Female',)])
    college = StringField('College', [Optional()])
    batch = IntegerField('Batch', [Optional(),
                                   NumberRange(min=2000, max=2015,
                                               message="Enter valid Batch")])
    branch = StringField('Branch', [Optional()])
