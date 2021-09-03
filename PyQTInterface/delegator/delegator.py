import warnings


class DelegateMessage:
    def __init__(self, arguments: list = [], arguments_dict: dict = {}, target_fcn: str = None, sender: object = None):
        self.arguments = arguments
        self.arguments_dict = arguments_dict
        self.target_fcn = target_fcn
        self.sender = sender

    def add_argument(self, value, key=None):
        if key is None:
            self.arguments.append(value)
        else:
            self.arguments_dict[key] = value

    def get_method(self, base):
        try:
            method = getattr(base, self.target_fcn)
            return method
        except Exception as e:
            try:
                method = getattr(base.main_window, self.target_fcn)
                return method
            except Exception as e:
                raise Exception(f'method name {self.target_fcn} does not defined.')

    def get_arguments(self):
        arguments_tuple = (self.arguments, self.arguments_dict)
        return arguments_tuple


class Delegator:
    """
    Main Window is too busy,,
    So, Delegator delegates main_window's roles.
    Delegator has main_window itself, for convenient implementation with legacy code.
    However, when you describes new function, I recommend you to not using main window.
    The main purpose of Delegator is supporting encapsulating.
    """

    def __init__(self, main_window):
        self.main_window = main_window

    def message_delivery(self, message: DelegateMessage):
        try:
            method = message.get_method(self)
            arguments = message.get_arguments()
            method(*arguments[0],**arguments[1])
        except Exception as e:
            warnings.warn(str(e))
