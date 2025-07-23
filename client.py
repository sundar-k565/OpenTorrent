import asyncio
from torrent import Torrent
from tracker import Tracker
from piece_manager import PieceManager
from peer import Peer

class Client:
    def __init__(self, torrent_file):
        self.torrent = Torrent(torrent_file)
        self.tracker = Tracker(self.torrent)
        self.piece_manager = PieceManager(self.torrent)
        self.peers = []

    async def start(self):
        tracker_response = await self.tracker.connect('-PC0001-706887310628')
        self.peers = tracker_response['peers']
        peer_connections = [Peer(peer['ip'], peer['port']) for peer in self.peers]
        await asyncio.gather(*[peer.connect() for peer in peer_connections])