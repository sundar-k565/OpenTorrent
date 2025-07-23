import asyncio
import struct

class Peer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    async def connect(self):
        reader, writer = await asyncio.open_connection(self.ip, self.port)
        # implement handshake and message exchange
        pass