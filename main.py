import asyncio
from client import Client

async def main():
    client = Client('path_to_torrent_file.torrent')
    await client.start()

asyncio.run(main())