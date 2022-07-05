"""
@project:   dorado
@author:    ihc
@description:
"""

import asyncio


class TcpServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def _run(self):
        server = await asyncio.start_server(self._handle, self.host, self.port)
        async with server:
            await server.serve_forever()

    def listenAndServe(self):
        asyncio.run(self._run())

    async def _handle(self, reader, writer):
        pass


if __name__ == '__main__':
    t = TcpServer("localhost", 9090)
    t.listenAndServe()
