class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422

try:
    print('----try----')
    raise HttpUnprocessableEntityError('Is a exception!')
except Exception as exception:
    print('----except----')
    print(exception.name)
    print(exception.status_code)
    print(exception.message)