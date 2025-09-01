import sys
import traceback

class customexception(Exception):
    def __init__(self, error_message, error_details: sys):
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.error_message = error_message

    def __str__(self):
        return f"Error occured in python script name [{self.file_name}] line number [{self.lineno}] error message [{self.error_message}]"

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        raise customexception(e, sys)
