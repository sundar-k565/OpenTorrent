class PieceManager:
    def __init__(self, torrent):
        self.torrent = torrent
        self.pieces = []
        self.blocks = []

    def next_request(self):
        # implement logic to determine the next block to request
        pass

    def add_block(self, block):
        # implement logic to add a received block to the piece
        pass

    def is_complete(self):
        # implement logic to check if the download is complete
        pass