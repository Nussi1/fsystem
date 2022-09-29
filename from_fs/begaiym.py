import sys
import shutil
import config
import hashlib
import pickle

from os.path import getsize
from pathlib import Path


def addFunction(src_path):

    if not Path(src_path).is_file():
        exit('Error: no such file ' + src_path)

    file_name = src_path.split('/')[-1]

    with open(config.INDEX_FILE, 'rb') as f:
        files = pickle.load(f)

    if file_name in files:
        exit('Error: file exists in the destination directory')

    with open(src_path, 'rb') as f:
        data = f.read()
        src_hash = hashlib.sha256(data).hexdigest()

    file_size = getsize(src_path)

    hash_path = config.HASH_PATH + '/'.join(list(src_hash[:4])) + '/hashes.pickle'