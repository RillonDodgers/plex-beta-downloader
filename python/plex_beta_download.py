#!/usr/bin/env python3
import requests
import os
import sys
from dotenv import load_dotenv

file_name = None
save_directory = os.path.join(os.path.dirname(__file__), '../debs/')


def main():
    """main method"""
    # Load .env
    dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
    save_directory = os.path.join(os.path.dirname(__file__), '../debs/')
    load_dotenv(dotenv_path)
    plex_token = os.environ.get("PLEX_TOKEN")
    # Set the headers for the request
    options = {"channel": "8", "build": "linux-x86_64", "distro": "debian", 'X-Plex-Token': plex_token}
    response = requests.get('https://plex.tv/downloads/latest/5', params=options)
    file_name = response.url.split("/")[-1]
    # Write the response to file
    with open(os.path.join(save_directory, file_name), "wb") as f:
        f.write(response.content)


def install():
    file_path = os.path.join(save_directory, file_name)
    print("sudo apt install ./%s" % file_name)
    #os.system("sudo apt install ./%s" % file_name)


if __name__ == '__main__':
    """Runs if the file is called directly"""
    main()
    if sys.argv[1] == "install":
        install()
