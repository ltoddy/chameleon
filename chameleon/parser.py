# content:
# content_type              ==> Content-Type: text/plain; charset="utf-8"
# mime_version              ==> MIME-Version: 1.0
# content_transfer_encoding ==> Content-Transfer-Encoding: base64

from typing import Dict


class ParseException(ValueError):
    pass


class ContentTypeException(ParseException):
    # It may not be necessary
    pass


class MimeTypeException(ParseException):
    # It may not be necessary
    pass


class ContentTransferEncodingException(ParseException):
    # It may not be necessary
    pass


def parser(content_type: str, mime_version: str, content_transfer_encoding: str) -> Dict[str, str]:
    # TODO
    return {
        'Content-Type': 'text/plain',
        'charset': 'utf-8',
        'MIME-Version': '1.0',
        'Content-Transfer-Encoding': 'base64',
    }  # fake result
