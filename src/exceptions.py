class MyException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'code 400: {self.message}'

    def __repr__(self):
        return f'code 400: {self.message!r}'


class ResourceExceptionBase(MyException):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'code 400: {self.message}'

    def __repr__(self):
        return f'code 400: {self.message!r}'


class ResourceNotFoundException(ResourceExceptionBase):
    ...


class ParameterExceptionBase(MyException):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'code 404: {self.message}'

    def __repr__(self):
        return f'code 404: {self.message!r}'


class ParameterNotFoundException(ParameterExceptionBase):
    ...


raise ParameterNotFoundException('mmd not found')
