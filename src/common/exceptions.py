from src.common.dtos import ErrorResponse


class APIException(Exception):
    def __init__(self, status_code: int, error_response: ErrorResponse):
        self.status_code = status_code
        self.error_response = error_response
        super().__init__(error_response.error_message)
