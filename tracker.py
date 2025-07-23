import aiohttp
import asyncio
import urllib.parse
import bencoding

class Tracker:
    def __init__(self, torrent):
        self.torrent = torrent

    async def connect(self, peer_id):
        params = {
            'info_hash': self.torrent.info_hash,
            'peer_id': peer_id,
            'uploaded': 0,
            'downloaded': 0,
            'left': self.torrent.meta_info['info']['length'],
            'port': 6889,
            'compact': 1
        }
        url = self.torrent.meta_info['announce'] + '?' + urllib.parse.urlencode(params)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.read()
                return bencoding.Decoder(data).decode()