# BitTorrent Client

This project implements a basic BitTorrent client in Python. It is structured to parse `.torrent` files, interact with BitTorrent trackers, manage peers, and request pieces of files. It uses asynchronous programming (via `asyncio` and `aiohttp`) to manage connections and data transfers in a non-blocking manner.

## Project Structure

The project is organized into the following files and directories:

bencoding.py # Implements Bencoding for decoding and encoding

torrent.py # Handles parsing of torrent files and generating info_hash

tracker.py # Handles communication with the BitTorrent tracker

peer.py # Implements Peer class for managing peer connections

piece_manager.py # Manages pieces of the torrent during download

client.py # Main client logic to interact with tracker and peers

main.py # Entry point for running the client

requirements.txt # List of required Python packages


## How it Works

1. **Bencoding**: The `bencoding.py` file contains classes for decoding and encoding Bencoded data (used in `.torrent` files). The `Decoder` class is used to parse the data, while the `Encoder` class is used for encoding data.

2. **Torrent**: The `torrent.py` file defines the `Torrent` class, which parses `.torrent` files and calculates the info hash used in the BitTorrent protocol.

3. **Tracker**: The `tracker.py` file defines the `Tracker` class, which communicates with the BitTorrent tracker to get peer information. It uses `aiohttp` for making asynchronous HTTP requests.

4. **Peer**: The `peer.py` file defines the `Peer` class for establishing and managing peer connections. The peer connects using TCP/IP and performs the necessary handshakes and message exchanges.

5. **PieceManager**: The `piece_manager.py` file manages the pieces of the torrent. It determines which pieces to request next, adds blocks to pieces as they are received, and checks if the download is complete.

6. **Client**: The `client.py` file defines the `Client` class, which manages the interaction between the tracker, peers, and pieces. It handles starting the download process, interacting with peers, and organizing the download of pieces.

7. **Main**: The `main.py` file is the entry point of the client. It creates a `Client` object and starts the torrent download process.

## Requirements

Before running the client, you need to install the required dependencies. Create a virtual environment (optional but recommended), and then install the dependencies from `requirements.txt`.

```bash
pip install -r requirements.txt
```

Running the Client

To run the BitTorrent client, you can execute the main.py file. This will start the client, connect to the tracker, and attempt to download the file described in the specified torrent.

```bash
python3 main.py
```

Example Usage

    Replace 'path_to_torrent_file.torrent' in main.py with the path to your .torrent file.

    Run the script, and the client will attempt to connect to the tracker and start downloading the file.

Contributing

Feel free to contribute to this project by opening an issue or submitting a pull request. Contributions are welcome, especially for extending the functionality and implementing missing features such as piece downloading, error handling, and more efficient peer management.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
Disclaimer

This is a simplified implementation and may not cover all edge cases or implement all features of the BitTorrent protocol. It is meant for educational purposes and as a starting point for further development. Use it at your own risk.
