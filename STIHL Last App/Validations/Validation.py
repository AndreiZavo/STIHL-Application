from Exceptions.Errors import ValidException


class Valid(object):

    @staticmethod
    def validate_name(name):
        errors = ""
        if " " not in name:
            errors += "The name needs to be divided by a space not anything else\n"
        name_parts = name.split()
        if len(name_parts) not in [2, 3, 4]:
            errors += "The name must have at least a first name and a last name"
        for name_part in name_parts:
            if not ('A' <= name_part[0] <= 'Z'):
                errors += "First letter of name should be uppercase\n"
        if len(errors):
            raise ValidException(errors)
