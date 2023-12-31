import sys
import argparse
import hashlib
import bencode
import os
import json

def get_conf_data():
    # Check if conf.json exists and has the necessary data
    if os.path.exists("conf.json"):
        with open("conf.json", "r") as json_file:
            data = json.load(json_file)
            if "torrent_output_path" in data and "announce_url" in data:
                return data
    return None

def update_conf_file(output_path, announce_url):
    # Update or create conf.json with the output path and announce URL
    data = {"torrent_output_path": output_path, "announce_url": announce_url}
    with open("conf.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

def show_current_path():
    conf_data = get_conf_data()
    if conf_data:
        print(f'Current path for .torrent file output: {conf_data["torrent_output_path"]}')
    else:
        print('No current data found in conf.json')

def show_current_url():
    conf_data = get_conf_data()
    if conf_data:
        print(f'Current announce URL: {conf_data["announce_url"]}')
    else:
        print('No current data found in conf.json')

def set_new_path(existing_url=None):
    new_path = input("Please Enter A New Path For Where You Want Your .torrent File Is Exported: ")
    return new_path

def set_new_announce_url(existing_path=None):
    new_url = input("Please Enter A New Announce Url For Your Torrent Tracker: ")
    return new_url

def print_help():
    print("""
    Usage:
    - TorrentCreator.py -p : Show current path for .torrent file output and announce URL.
    - TorrentCreator.py -np : Set a new path for .torrent file output.
    - TorrentCreator.py -a : Show current announce URL.
    - TorrentCreator.py -na : Set a new announce URL.
    - TorrentCreator.py -h or TorrentCreator.py -help : Show this help message.
    """)

def create_torrent(filepath, torrent_output_path, announce_url):
    # Get the name of the file and its directory
    base_filename = os.path.basename(filepath)

    # Get the total size of the file
    file_size = os.path.getsize(filepath)

    # Get the piece size
    piece_size = 2 ** 19

    # Get the number of pieces
    num_pieces = (file_size + piece_size - 1) // piece_size

    # Create an empty list to store the pieces
    pieces = []

    # Open the file and read each piece
    # Append its SHA1 hash to the pieces list
    with open(filepath, 'rb') as f:
        for i in range(num_pieces):
            piece = f.read(piece_size)
            pieces.append(hashlib.sha1(piece).digest())

    # Create a dictionary to store all the metadata
    torrent_data = {
        'announce': announce_url,
        'info': {
            'name': base_filename,
            'piece length': piece_size,
            'pieces': b''.join(pieces),
            'length': file_size
        }
    }

    # Print the announce URL while creating the .torrent file
    print(f'Creating torrent for Tracker: {announce_url}')

    # Encode the metadata as a torrent file
    torrent_bencoded = bencode.bencode(torrent_data)

    # Write the torrent file to disk in the specified directory
    output_torrent_path = os.path.join(torrent_output_path, base_filename + '.torrent')
    with open(output_torrent_path, 'wb') as f:
        f.write(torrent_bencoded)

    # Print a message to the user
    print('Torrent created!')
    # Print the path of the created .torrent file
    print(f'Path of the created .torrent file: {output_torrent_path}')

def main():
    parser = argparse.ArgumentParser(description="Create a torrent file for a given media file.")
    parser.add_argument("filepath", help="Path to the media file for which to create a torrent")
    args = parser.parse_args()

    # Check if conf.json has the necessary data
    conf_data = get_conf_data()

    # If not found or invalid, ask the user for the necessary information
    if not conf_data:
        torrent_output_path = input("Please Enter the path where you want your .torrent file to be exported: ")
        announce_url = input("Please Enter The Announce Url For Your Torrent Tracker: ")
        update_conf_file(torrent_output_path, announce_url)
    else:
        torrent_output_path = conf_data["torrent_output_path"]
        announce_url = conf_data["announce_url"]

    create_torrent(args.filepath, torrent_output_path, announce_url)

if __name__ == "__main__":
    main()
