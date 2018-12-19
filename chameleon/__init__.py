import smtpd
import socket
from numbers import Integral
from typing import Tuple

from chameleon.decoder import MailDecoder
from config import HOST, PORT


class Chameleon(smtpd.SMTPServer):
    def __init__(self, host=HOST, port=PORT):
        super().__init__(
            (host, port),
            remoteaddr=None,
            data_size_limit=smtpd.DATA_SIZE_DEFAULT,
            map=None,
            enable_SMTPUTF8=False,
            decode_data=False
        )

    def handle_accepted(self, conn: socket.socket, addr: Tuple[str, Integral]):
        super().handle_accepted(conn, addr)

    def process_message(self, peer: Tuple[str, Integral], mailfrom: str, rcpttos: list, data: bytes, **kwargs):
        """
        :param peer: 客户端地址，一个包含 IP 地址和接收端口号的元组 ('127.0.0.1', 43412)
        :param mailfrom: 来自报文封装包的 `from` 信息，由客户端在报文转发时上传至服务器.它并不总是和 `From` 标题相符
        :param rcpttos: 来自报文封装包的收件人列表.同样地，它也不总是和 To 标题相符，尤其是收件人被盲目抄袭时
        :param data: 完整的 RFC 5322 报文正文
        """

        # content:

        # Content-Type: text/plain; charset="utf-8"
        # MIME-Version: 1.0
        # Content-Transfer-Encoding: base64
        # To: Sender <tester@example.com>
        # From: Receiver <ltoddy@example.com>
        # Subject: =?utf-8?b?dGVzdCDmoIfpopg=?=
        #
        # SnVzdCBmb3IgdGVzdCDmtYvor5Xpgq7ku7blhoXlrrk=

        # TODO: sender: 发送人只有一个, receivers: 接收者可以有多个
        # self.sender = mailfrom
        # self.receivers = rcpttos

        decoder = MailDecoder(data)
