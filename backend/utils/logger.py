# region IMPORT
import logging, os
import settings.py.system as settings

# endregion IMPORT


# region CODE
class Logger:
    """Handles logging and CMD printouts"""

    capped = False
    counter = 100

    try:
        logging.basicConfig(
            level=logging.INFO,
            format="%(levelname)s %(message)s",
            handlers=[logging.FileHandler(settings.Paths.LOGS), logging.StreamHandler()],
        )
    except FileNotFoundError:
        os.mkdir(settings.Paths.FOLDER_LOGS)
        logging.basicConfig(
            level=logging.INFO,
            format="%(levelname)s %(message)s",
            handlers=[logging.FileHandler(settings.Paths.LOGS), logging.StreamHandler()],
        )

    @staticmethod
    def __printlines(cat, counter, message, numberOfDashes):
        """prints the lines and handles the line cap"""
        if Logger.capped:
            if len(message) > 60:
                message = message[:55] + "..."
        logging.info(" |--- {} {} {} {}".format(cat.upper(), counter, "--- " * numberOfDashes, message))

    @staticmethod
    def print_as_header(message):
        """Prints message as a header"""
        logging.info("*********")
        logging.info(f" | {message.upper()}")
        logging.info(" |--------------------------------")

    @staticmethod
    def print_as_message(cat, message):
        """
        Prints message as a message
        - Args:
            - cat : 'in the format 'xxx-x'
            - message : 'The message to be printed'
        """
        counter = Logger.counter
        Logger.__printlines(cat=cat, counter=counter, message=message, numberOfDashes=1)
        Logger.counter += 1

    @staticmethod
    def print_as_submessage(cat, message):
        """
        Prints submessage as submessage
        - Args:
            - cat : 'in the format 'xxx-x'
            - message : 'The message to be printed'
        """
        counter = Logger.counter
        Logger.__printlines(cat=cat, counter=counter, message=message, numberOfDashes=2)
        Logger.counter += 1

    @staticmethod
    def print_as_subdetail(cat, message):
        """
        Prints message as a code
        - Args:
            - cat : 'in the format 'xxx-x'
            - message : 'The message to be printed'
        """
        counter = Logger.counter
        Logger.__printlines(cat=cat, counter=counter, message=message, numberOfDashes=4)
        Logger.counter += 1

    @staticmethod
    def eol_marker():
        """Marks the End of line of a segment"""
        logging.info(" | ***************** ***************** ***************** COMPLETED!!! ")

    @staticmethod
    def linebreak():
        """Marks the End of line of a segment"""
        logging.info(" | ------------------------------------------------------------------- \n")

    @staticmethod
    def print_as_error(cat, message):
        """
        Prints message as Error
        - Args:
            - cat : 'in the format 'xxx-x'
            - message : 'The message to be printed'
        """
        counter = Logger.counter
        logging.error(" >>> {} {} {} {}".format(cat.upper(), counter, "--- --- --- --- --- ", message))
        Logger.counter += 1


# endregion CODE
