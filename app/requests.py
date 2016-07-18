import re


class Request(object):
    """
        This 'Request' class will represent the handler for all POST requests that will
        come through forms on our website. To create a validator for any form, simply
        inherit from this class and implement the 'validate' method.
    """
    rules = {
        'text': '^[a-zA-Z0-9 ]+$',
        'numbers': '^[0-9]+$',
        'characters': '^[a-zA-Z ]+$',
        'email': '^[a-zA-Z@._]+$'  # this is temp, hans mat mohsin mujhe regex nahin atey
    }
    errors = {}


# For all classes which inherit from 'Request' class and implement the validate method:-
#
# ARGUMENTS: (String[] data)
#       => data is the form object received from the post request.
#
# RETURN: (boolean validate, String[] errors)
#       => 'validate' signifies whether the form data was valid or not.
#       => 'errors' is a dict which provides an error message with the same
#           name as key as that of its original form field.


class ContactRequest(Request):
    """
        Refers to the 'Contact' form.
    """
    def validate(self, data):
        validate = True

        characters_regex = re.compile(self.rules['characters'])
        text_regex = re.compile(self.rules['text'])
        email_regex = re.compile(self.rules['email'])

        if not characters_regex.match(data['name']):
            validate = False
            self.errors['name'] = 'Name can contain only characters'
        if not email_regex.match(data['email']):
            validate = False
            self.errors['email'] = 'Not a proper email format'
        if not text_regex.match(data['msg']):
            validate = False
            self.errors['msg'] = 'Illegal input characters encountered'

        return validate, self.errors


class RegisterRequest(Request):
    """
        Refers to the 'Register' form.
    """
    def validate(self, data):
        validate = True

        characters_regex = re.compile(self.rules['characters'])
        numbers_regex = re.compile(self.rules['numbers'])
        email_regex = re.compile(self.rules['email'])

        if not characters_regex.match(data['name']):
            validate = False
            self.errors['name'] = 'Name can contain only characters'
        if not email_regex.match(data['email']):
            validate = False
            self.errors['email'] = 'Not a proper email format'
        if len(data['password']) < 8:
            validate = False
            self.errors['password'] = 'Password should be at least 8 characters long'
        if not numbers_regex.match(data['cell']):
            validate = False
            self.errors['cell'] = 'Name can contain only characters'
        if not characters_regex.match(data['college']):
            validate = False
            self.errors['college'] = 'College name can contain only characters'
        if not numbers_regex.match(data['batch']):
            validate = False
            self.errors['batch'] = 'Input your college freshman year'
        if not characters_regex.match(data['branch']):
            validate = False
            self.errors['branch'] = 'Branch name can contain only characters'

        return validate, self.errors



