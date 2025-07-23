import struct

class Decoder:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def decode(self):
        if self.data[self.index] == ord('i'):
            return self.decode_int()
        elif self.data[self.index] == ord('l'):
            return self.decode_list()
        elif self.data[self.index] == ord('d'):
            return self.decode_dict()
        else:
            return self.decode_str()

    def decode_int(self):
        self.index += 1
        end = self.data.find(b'e', self.index)
        num = int(self.data[self.index:end])
        self.index = end + 1
        return num

    def decode_str(self):
        colon = self.data.find(b':', self.index)
        length = int(self.data[self.index:colon])
        self.index = colon + 1
        str_data = self.data[self.index:self.index + length]
        self.index += length
        return str_data

    def decode_list(self):
        self.index += 1
        lst = []
        while self.data[self.index] != ord('e'):
            lst.append(self.decode())
        self.index += 1
        return lst

    def decode_dict(self):
        self.index += 1
        dct = {}
        while self.data[self.index] != ord('e'):
            key = self.decode_str()
            value = self.decode()
            dct[key] = value
        self.index += 1
        return dct

class Encoder:
    def __init__(self, data):
        self.data = data

    def encode(self):
        if isinstance(self.data, int):
            return self.encode_int()
        elif isinstance(self.data, str):
            return self.encode_str()
        elif isinstance(self.data, list):
            return self.encode_list()
        elif isinstance(self.data, dict):
            return self.encode_dict()

    def encode_int(self):
        return b'i' + str(self.data).encode('utf-8') + b'e'

    def encode_str(self):
        return str(len(self.data)).encode('utf-8') + b':' + self.data.encode('utf-8')

    def encode_list(self):
        encoded_list = b'l'
        for item in self.data:
            encoded_list += Encoder(item).encode()
        encoded_list += b'e'
        return encoded_list

    def encode_dict(self):
        encoded_dict = b'd'
        for key, value in self.data.items():
            encoded_dict += Encoder(key).encode() + Encoder(value).encode()
        encoded_dict += b'e'
        return encoded_dict