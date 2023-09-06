# region IMPORT
import functools
from .logger import Logger

# endregion IMPORT


class ErrorHandler:
    def generic_errorhandler(func):
        """
        - Handles Generic Errors and returns '-'
        """

        printError = lambda e: Logger.print_as_error(cat="err-r", message=f"ERROR: {e.__class__.__name__.upper()} - {e} ")

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result

            except Exception as e:
                printError(e)
                return "-"

        return wrapper
