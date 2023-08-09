import sys
import logging


def error_message_details(error, error_detail):
    # Use sys.exc_info() instead of error_detail.exc_info()
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error Occurred on Python Script [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_detail):
        error_message = error_message_details(error, error_detail)
        super().__init__(error_message)
        self.error_message = error_message  # Store the error message details

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero error")
        # Pass sys.exc_info() instead of sys
        raise CustomException(e, sys.exc_info())
