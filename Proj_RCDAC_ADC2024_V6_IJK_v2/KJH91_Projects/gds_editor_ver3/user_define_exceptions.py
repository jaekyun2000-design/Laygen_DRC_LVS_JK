# import exceptions
#####exceptions are defined

__all__=('FormatError','EndofFileError','IncorrectRecordSize','IncorrectDataSize')

class FormatError(Exception):
    """base class for all gds exceptions""" 
class EndofFileError(FormatError):
    """raised on unexpected end of file"""
    
class IncorrectRecordSize(FormatError):
    """raised if record size is not correct"""
    
    
class IncorrectDataSize(FormatError):
    """raised if data size is not correct"""
class IncorrectDataValue(FormatError):
    """data has incorrect value"""
class IncorrecElementName(FormatError):
    """element name is incorrect"""

class IncorrectInputError(FormatError):
    """Input is incorrect"""