from flask_security.forms import ConfirmRegisterForm, Required
from wtforms import IntegerField,TextField
from wtforms.validators import *

class ExtendedConfirmRegisterForm(ConfirmRegisterForm):
    first_name = TextField('First Name', [Required()])
    last_name = TextField('Last Name', [Required()])
    cell  = TextField('Telephone',[Length(min=10,max=10,message='Not a valid Phone number')])
    gender = TextField('Gender', [Required(),AnyOf(['Male','Female','male','female'], message='Please Enter Male or Female',)])
    college = TextField('College', [Optional()])
    batch = IntegerField('Batch',[Optional(),NumberRange(min=2000, max=2015, message="Enter valid Batch")])
    branch = TextField('Branch', [Optional()])
