#!python3

import os
import pyperclip
import subprocess
import sys
import time

import Helper
from Settings import Settings
from ReleaseInfo import ReleaseInfo
from ScreenshotGenerator import ScreenshotGenerator
from ImageUploader import ImageUploader

CLEAR_FN = 'cls' if os.name == 'nt' else 'clear'


def main():
    Settings.load_settings()
    image_host = Settings.get_preferred_host()

    assert len(sys.argv) > 1, 'Error, need input file'

    subprocess.run(CLEAR_FN, shell=True)

    print( 'Image host "{}" will be used for uploading\n'.format(image_host['name']) )
    print('Gathering media info')
    rls = ReleaseInfo( os.path.abspath(sys.argv[1]) )
    release_info = rls.get_complete_mediainfo()

    print('Generating screenshots')
    images = ScreenshotGenerator().generate_screenshots(rls)

    print( 'Uploading images to {}'.format(image_host['name']) )
    gallery_name = Helper.get_gallery_name(sys.argv[1])
    uploader = ImageUploader(images, gallery_name, image_host)
    uploader.upload()
    formatted_urls = uploader.get_formatted_urls()

    if Settings.print_not_copy:
        subprocess.run(CLEAR_FN, shell=True)
        print("[mediainfo]{}[/mediainfo]{}".format(release_info, formatted_urls))
    else:
        pyperclip.copy(release_info + formatted_urls)
        print('\nMediainfo + image URLs have been copied to clipboard')
        time.sleep(5)

    # Run the Toc.py script with the same input file
    toc_script_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "TorrentCreator.py")
    subprocess.run(['python', toc_script_path, sys.argv[1]])

if __name__ == '__main__':
    main()
