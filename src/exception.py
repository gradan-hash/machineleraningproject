import sys


def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error Occurred on Python Script [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message


class CustomException(Exception):

    def __init__(self, error_message, error, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(
            error, error_detail)

    def __str__(self):
        return self.error_message


# try:
#     # Some code that might raise an exception
#     raise CustomException("Custom error message",
#                           ValueError("Something went wrong"))
# except CustomException as ce:
#     print(ce.error_message)
