# -*- coding: utf-8 -*-
# to use comment written with korean, use above code
#import exceptions
###no exceptions for python3.7, but for python2.7 exceptions
class IncorrectInputError(Exception):
    """Input is incorrect data"""

class StatusError(Exception):
    """Improper Status"""

_InvalidInputError = "Invalid Input Error"

_UnkownError = "UnkownError Error"
