class GetRequestError(Exception):
    pass


class PostRequestError(Exception):
    pass


class PutRequestError(Exception):
    pass


class DeleteRequestError(Exception):
    pass


class UnknownOptionalParameter(Exception):
    pass


class WrongRequestType(Exception):
    pass
