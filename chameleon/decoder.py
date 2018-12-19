from base64 import decodebytes


class MailDecoder:
    def __init__(self, data: bytes):
        self.data = data
        content_type, mime_version, content_transfer_encoding, to, from_, subject, *content = data.decode().split('\n')
        print('content_type              ==>', content_type)
        print('mime_version              ==>', mime_version)
        print('content_transfer_encoding ==>', content_transfer_encoding)
        print('to                        ==>', to)
        print('from_                     ==>', from_)
        print('subject                   ==>', subject)
        print('content                   ==>', decodebytes(''.join(content).encode('utf-8')).decode('utf-8'))
