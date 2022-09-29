import settings
import hashlib
import pickle
import os
import time
import sys


def add_file(args):
  # if len(sys.argv) == 2 or len(sys.argv) >= 4:
  #   print('Input a file name correctly')
  #   exit()
  file_name = "/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/hashed.py"
  get_file_path(file_name)
  hash_name = get_hash_name(file_name)
  name_dir(hash_name)
  path = get_hash_file(get_file_path(file_name))
  hash_dir(path)
  load_name = load_hashed_name(name_dir(hash_name))
  load_content = load_hashed_name(hash_dir(path))
  load_name.update({hash_name: file_name})
  load_content.update({path : {getfilesize(file_name), get_time(file_name), reference(file_name)}})
  dump_file(load_name, name_dir(hash_name))
  dump_file(load_content, hash_dir(path))
  print(load_name)
  print(load_content)


def get_file_path(file):
  path =  settings.PATH['path_from'] + str(file)
  if not os.path.exists(path):
    with open(path, 'w') as f:
      f.write('Create a new text file!')
  else:
    return path


def getfilesize(filename):
  return os.stat(get_file_path(filename)).st_size


def get_time(file_time):
  return time.ctime(os.path.getctime(get_file_path(file_time)))


def reference(file_ref):
  return sys.getrefcount(file_ref)


def get_hash_name(file):
  return hashlib.sha256(get_file_path(file).encode('UTF-8')).hexdigest()


def name_dir(hash_name):
  s = '/'.join(list(hash_name[:4]))
  return settings.PATH['path_obj'] + s + '/name.pickle'


def get_hash_file(a):
  return hashlib.sha256(open(a, "rb").read()).hexdigest()


def hash_dir(arg):
  s = '/'.join(list(arg[:4]))
  return settings.PATH['path_obj'] + s + '/hash.pickle'


def load_hashed_name(path):
  with open(path, 'rb') as f2:
    return pickle.load(f2)


def dump_file(arg, path):
  with open(path, 'wb') as f2:
    pickle.dump(arg, f2)