"""
@project:   dorado
@author:    ihc
@description:
"""

import asyncio
import struct
import types
from asyncio.queues import Queue
from logging import getLogger

log = getLogger(__name__)


class StreamServer(object):

    def __init__(self, host, port):
        self._host = host
        self._port = port

    async def _run(self):
        server = await asyncio.start_server(self._client_connected_cd, self._host, self._port)
        async with server:
            await server.serve_forever()

    def serve_forever(self):
        asyncio.run(self._run())

    async def _client_connected_cd(self, client_reader, client_writer):
        raise NotImplementedError


class DefaultCodecMixin(object):

    def __init__(self):
        self._struct = struct.Struct('<II')

    def decode_header(self, reader):
        try:
            data = reader.readexactly(self._struct.size)
            protocol_number, content_len = self._struct.unpack(data)
            return protocol_number, content_len, data
        except asyncio.IncompleteReadError as e:
            log.error(e)
        except Exception as e:
            log.error(e)

    def decode_body(self):
        pass


    def encode_header(self, *args):
        return self._struct.pack(*args)



class MessageServer(StreamServer, DefaultCodecMixin):

    def __init__(self, host, port):
        super().__init__(host, port)
        self._working_queue = Queue()

    async def _client_connected_cd(self, client_reader, client_writer):
        protocol_number, content_len, data = self.decode_header(client_reader)
        # 转发


class MessageClient(object):
    pass


if __name__ == '__main__':
    s = struct.Struct('<II')
    data = s.pack(0, 1)
    print(data)
    print(s.unpack(data))
