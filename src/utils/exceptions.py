class MissingDataException(Exception):
    """
    Exception raised when required input data is missing.
    """

    def __init__(self, message="No input data provided."):
        self.message = message
        super().__init__(self.message)


class MissingCredentialsException(Exception):
    """
    Exception raised when credentials are missing from the request.
    """

    def __init__(self, message="Missing credentials."):
        self.message = message
        super().__init__(self.message)


class CredentialsUnauthorizedException(Exception):
    """
    Exception raised for unauthorized access due to invalid credentials
    or an inactive account.
    """

    def __init__(self, message="Unauthorized Access."):
        self.message = message
        super().__init__(self.message)


class TokenUnauthorizedException(Exception):
    """
    Exception raised for unauthorized access due to invalid token.
    """
    def __init__(self, message="Invalid or Expired Token."):
        self.message = message
        super().__init__(self.message)


class MethodNotAllowedException(Exception):
    """
    Exception raised when a method is not allowed for the requested URL.
    """

    def __init__(self, message="Method not allowed."):
        self.message = message
        super().__init__(self.message)


class NotFoundException(Exception):
    """
    Exception raised when a requested resource is not found.
    """

    def __init__(self, message="Resource not found."):
        self.message = message
        super().__init__(self.message)


class ConflictException(Exception):
    """
    Exception raised when there is a conflict with the current state of the resource.
    """

    def __init__(self, message="Conflict occurred."):
        self.message = message
        super().__init__(self.message)


class UnprocessableEntityException(Exception):
    """
    Exception raised when the request is well-formed but unable to be followed
    due to semantic errors.
    """

    def __init__(self, message="Unprocessable entity."):
        self.message = message
        super().__init__(self.message)


class PreconditionFailedException(Exception):
    """
    Exception raised when a precondition in the request headers is not met.
    """

    def __init__(self, message="Precondition failed."):
        self.message = message
        super().__init__(self.message)


class GatewayTimeoutException(Exception):
    """
    Exception raised when a gateway or proxy server does not receive a timely
    response from an upstream server.
    """

    def __init__(self, message="Gateway timeout."):
        self.message = message
        super().__init__(self.message)


class BadRequestException(Exception):
    """
    Exception raised when there is bad request occur.
    """

    def __init__(self, message="Bad Request."):
        self.message = message
        super().__init__(self.message)


class InternalServerException(Exception):
    """
    Exception raised when there is an internal server error.
    """
    def __init__(self, message="Internal Server Error."):
        self.message = message
        super().__init__(self.message)


class UnsupportedMediaTypeException(Exception):
    """
    Exception raised when there is an unsupported media type.
    """
    def __init__(self, message="Unsupported Media Type."):
        self.message = message
        super().__init__(self.message)
