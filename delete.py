import pathlib
import add
import os
import sys


def delete_file(args):
  if len(sys.argv) == 2 or len(sys.argv) >= 4:
    print('Input a file name correctly')
    exit()
  file_name = args[0]
  add.get_file_path(file_name)
  hash_name = add.get_hash_name(file_name)
  add.name_dir(hash_name)
  path = add.get_hash_file(add.get_file_path(file_name))
  add.hash_dir(path)
  if pathlib.Path(add.file_dir(path)+file_name).exists():
    os.remove(add.file_dir(path)+file_name)
  else:
    print('No such file')
  remove_file_name(file_name)
  load_name = add.load_hashed_name(add.name_dir(hash_name))
  load_content = add.load_hashed_name(add.hash_dir(path))
  print(load_name)
  print(load_content)
  del load_name[hash_name]
  del load_content[path]
  print(load_name)
  print(load_content)
  add.dump_file(load_name, add.name_dir(hash_name))
  add.dump_file(load_content, add.hash_dir(path))
  print(load_name)
  print(load_content)

def remove_file_name(file_name):
  with open('names.txt', 'r') as f:
      lines = f.readlines()
  with open('names.txt', 'w') as f:
    for line in lines:
      if line.strip("\n") != file_name:
        f.write(line)