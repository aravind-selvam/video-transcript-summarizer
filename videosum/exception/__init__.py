import sys


class CustomException(Exception):

    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = CustomException.get_detailed_error_message(error_message=error_message,
                                                                        error_detail=error_detail
                                                                        )

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detail: sys) -> str:
        """
        It takes an error message and the error detail as input and returns a detailed error message

        Returns:
          the error message.
        """
        _, _, exec_tb = error_detail.exc_info()
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occurred in script: [ {file_name} ] at line number: [{try_block_line_number}] error " \
                        f"message: [{error_message}] "

        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return str(CustomException.__name__)
