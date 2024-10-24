class SuperException(Exception):
    code: int
    message: str

    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.message = message
        self.code = code
