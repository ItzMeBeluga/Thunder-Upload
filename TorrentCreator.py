import sys
import hashlib
import bencode
import os

#Make sure a file path is provided
if len(sys.argv) != 2:
    print('Usage: torrentcreate.py <filepath>')
    sys.exit(1)

# Get the path of the file to be torrented
filename = sys.argv[1]

#Get the name of the file and its directory
base_filename = os.path.basename(filename)
file_dirname = os.path.dirname(filename)

# Get the total size of the file
file_size = os.path.getsize(filename)

# Get the piece size
# Piece size should be a multiple of 2**18.
# We will use 64kb pieces
piece_size = 2 ** 24

# Get the number of pieces
# File size divided by piece size, rounded up
num_pieces = (file_size + piece_size - 1) // piece_size

# Create an empty list to store the pieces
pieces = []

# Open the file and read each piece
# Append its SHA1 hash to the pieces list
with open(filename, 'rb') as f:
    for i in range(num_pieces):
        piece = f.read(piece_size)
        pieces.append(hashlib.sha1(piece).digest())

# Create a dictionary to store all the metadata
torrent = {
    'announce': 'https://tracker.torrentbd.net/announce',
    'info': {
        'name': base_filename,
        'piece length': piece_size,
        'pieces': b''.join(pieces),
        'length': file_size
    }
}

# Encode the metadata as a torrent file
torrent_bencoded = bencode.bencode(torrent)

# Write the torrent file to disk in the same directory as the input file
with open(os.path.join(file_dirname, base_filename + '.torrent'), 'wb') as f:
    f.write(torrent_bencoded)

# Print a message to the user
print('Torrent created!')
# Print the path of the created .torrent file
print(f'Path of the created .torrent file: {os.path.join(file_dirname, base_filename + ".torrent")}')