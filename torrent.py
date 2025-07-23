import bencoding

class Torrent:
    def __init__(self, file_path):
        self.file_path = file_path
        self.meta_info = self.parse_torrent_file()
        self.info_hash = self.calculate_info_hash()

    def parse_torrent_file(self):
        with open(self.file_path, 'rb') as f:
            meta_info = f.read()
            return bencoding.Decoder(meta_info).decode()

    def calculate_info_hash(self):
        info_dict = self.meta_info['info']
        encoded_info = bencoding.Encoder(info_dict).encode()
        import hashlib
        return hashlib.sha1(encoded_info).digest()