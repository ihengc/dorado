"""
@project:   dorado
@author:    ihc
@description:
"""
import asyncio
import struct
from asyncio.queues import Queue
from threading import Thread


class SteamClient(object):

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._working_queue = Queue()
        self._reader = None
        self._writer = None
        self._event_loop = None

    def start(self):
        self._event_loop = asyncio.new_event_loop()
        Thread(target=SteamClient._start_event_loop, args=(self._event_loop,)).start()
        asyncio.run_coroutine_threadsafe(self.do('do'), self._event_loop)


    @staticmethod
    def _start_event_loop(loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    async def do(self, name):
        await asyncio.sleep(0.5)
        print(name)


async def login():
    reader, writer = await asyncio.open_connection('localhost', 8899)
    fmt = struct.Struct('<II')
    data = fmt.pack(0, 1)
    writer.write(data)
    await writer.drain()


if __name__ == '__main__':
    client = SteamClient('localhost', 8899)
    client.start()
