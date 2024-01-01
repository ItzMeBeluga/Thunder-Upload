import sys
import os
import json
import hashlib
import bencode
import argparse
import logging
import time

def validate_conf_data(data):
    return isinstance(data, dict) and "torrent_output_path" in data and "announce_url" in data

def get_conf_data():
    if os.path.exists("conf.json"):
        with open("conf.json", "r") as json_file:
            data = json.load(json_file)
            if validate_conf_data(data):
                return data
    return None

def update_conf_file(output_path, announce_url):
    data = {"torrent_output_path": output_path, "announce_url": announce_url}
    with open("conf.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

def show_current_path():
    conf_data = get_conf_data()
    if conf_data:
        logging.info(f'Current path for .torrent file output: {conf_data["torrent_output_path"]}')
    else:
        logging.info('No current data found in conf.json')

def show_current_url():
    conf_data = get_conf_data()
    if conf_data:
        logging.info(f'Current announce URL: {conf_data["announce_url"]}')
    else:
        logging.info('No current data found in conf.json')

def set_new_path(existing_url=None):
    new_path = input("Please Enter A New Path For Where You Want Your .torrent File Is Exported: ")
    return new_path

def set_new_announce_url(existing_path=None):
    new_url = input("Please Enter A New Announce Url For Your Torrent Tracker: ")
    return new_url

def print_help():
    logging.info("""
    Usage:
    - TorrentCreator.py -p : Show current path for .torrent file output and announce URL.
    - TorrentCreator.py -np : Set a new path for .torrent file output.
    - TorrentCreator.py -a : Show current announce URL.
    - TorrentCreator.py -na : Set a new announce URL.
    - TorrentCreator.py -t : Show trackers from an existing torrent file.
    - TorrentCreator.py -d : Generate a default conf.json file.
    - TorrentCreator.py -l : List files in the torrent directory.
    - TorrentCreator.py -h or TorrentCreator.py --help : Show this help message.
    """)

def create_torrent(filename, announce_url, torrent_output_path):
    base_filename = os.path.basename(filename)
    file_size = os.path.getsize(filename)
    piece_size = 2 ** 19
    num_pieces = (file_size + piece_size - 1) // piece_size
    pieces = []

    with open(filename, 'rb') as f:
        for _ in range(num_pieces):
            piece = f.read(piece_size)
            pieces.append(hashlib.sha1(piece).digest())

    torrent = {
        'announce': announce_url,
        'info': {
            'name': base_filename,
            'piece length': piece_size,
            'pieces': b''.join(pieces),
            'length': file_size
        },
        'created by': 'bencode',
        'creation date': int(time.time())
    }

    logging.info(f'Creating torrent for Tracker: {announce_url}')
    torrent_bencoded = bencode.bencode(torrent)

    output_torrent_path = os.path.join(torrent_output_path, base_filename + '.torrent')
    with open(output_torrent_path, 'wb') as f:
        f.write(torrent_bencoded)

    logging.info('Torrent created!')
    logging.info(f'Path of the created .torrent file: {output_torrent_path}')

def generate_default_conf():
    update_conf_file("default_output_path", "default_announce_url")
    logging.info('Default conf.json file generated.')
    sys.exit(0)

def list_files():
    files = os.listdir(".")
    logging.info("Files in the current directory:")
    for file in files:
        logging.info(f"- {file}")
    sys.exit(0)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description='Torrent Creator Script')
    parser.add_argument('-p', action='store_true', help='Show current path for .torrent file output and announce URL.')
    parser.add_argument('-np', action='store_true', help='Set a new path for .torrent file output.')
    parser.add_argument('-a', action='store_true', help='Show current announce URL.')
    parser.add_argument('-na', action='store_true', help='Set a new announce URL.')
    parser.add_argument('-t', '--trackers', action='store_true', help='Show trackers from an existing torrent file.')
    parser.add_argument('-d', '--default', action='store_true', help='Generate a default conf.json file.')
    parser.add_argument('-l', '--list', action='store_true', help='List files in the torrent directory.')
    parser.add_argument('filename', nargs='?', help='File path for torrent creation.')

    args = parser.parse_args()

    # Check for no arguments or help
    if not sys.argv[1:] or (hasattr(args, 'filename') and args.filename is None):
        print_help()
        sys.exit(0)

    if args.default:
        generate_default_conf()

    if args.list:
        list_files()

    if args.trackers:
        if not args.filename:
            logging.error('Please provide the path to an existing torrent file.')
            sys.exit(1)
        
        try:
            with open(args.filename, 'rb') as torrent_file:
                torrent_data = bencode.bdecode(torrent_file.read())
                if 'announce-list' in torrent_data:
                    logging.info("Trackers in the existing torrent file:")
                    for tracker_list in torrent_data['announce-list']:
                        logging.info(f"- {tracker_list[0]}")
                elif 'announce' in torrent_data:
                    logging.info(f"- {torrent_data['announce']}")
                else:
                    logging.info('No trackers found in the existing torrent file.')
        except Exception as e:
            logging.error(f'Error reading the existing torrent file: {e}')
        sys.exit(0)

    if args.p:
        show_current_path()
        sys.exit(0)
    elif args.np:
        conf_data = get_conf_data()
        new_path = set_new_path(existing_url=conf_data["announce_url"] if conf_data else None)
        update_conf_file(new_path, conf_data["announce_url"] if conf_data else None)
        logging.info(f'New path set for .torrent file output: {new_path}')
        sys.exit(0)
    elif args.a:
        show_current_url()
        sys.exit(0)
    elif args.na:
        conf_data = get_conf_data()
        new_url = set_new_announce_url(existing_path=conf_data["torrent_output_path"] if conf_data else None)
        update_conf_file(conf_data["torrent_output_path"] if conf_data else None, new_url)
        logging.info(f'New announce URL set: {new_url}')
        sys.exit(0)
    elif args.filename:
        conf_data = get_conf_data()
        torrent_output_path = conf_data["torrent_output_path"] if conf_data else input("Please Enter the path where you want your .torrent file to be exported: ")
        announce_url = conf_data["announce_url"] if conf_data else input("Please Enter The Announce Url For Your Torrent Tracker: ")
        create_torrent(args.filename, announce_url, torrent_output_path)
    else:
        logging.error('Invalid arguments. Use -h for help.')
        sys.exit(1)
