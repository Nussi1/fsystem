import os
import settings
from pathlib import Path
import pathlib
import glob
import sys
import fnmatch
import re


def list_file(args):
  if len(sys.argv) == 2 or len(sys.argv) >= 4:
    print('Input a file name correctly')
    exit()
  file_name = args[0]
  files = glob.glob(settings.PATH['path_obj'] + '/**/' + file_name, recursive=True)
  for file in files:
    splitted_file = file.split("/")
    if not splitted_file[-1] == 'hash.pickle' and not splitted_file[-1] == 'name.pickle':
      print(file)


# def list_file(args):
#   if len(sys.argv) == 2 or len(sys.argv) >= 4:
#     print('Input a file name correctly')
#     exit()
#   file_name = args[0]
#   find_of_name = open(settings.PATH['path_file'])
#   for name_of_file in find_of_name:
#     if re.search(f"{file_name}", name_of_file):
#       print(name_of_file, end= '')




# def list_file(args):
#   if len(sys.argv) == 2 or len(sys.argv) >= 4:
#     print('Input a file name correctly')
#     exit()
#   file_name = args[0]
#   walker = settings.PATH['path_obj']
#   for folder, sub_folder, files in os.walk(walker):
#     for filename in fnmatch.filter(files, file_name):
#       print(os.path.join(folder, filename))


# def list_file(args):
#   if len(sys.argv) == 2 or len(sys.argv) >= 4:
#     print('Input a file name correctly')
#     exit()
#   file_name = args[0]
#   walker = settings.PATH['path_obj']
#   for folder, sub_folder, files in os.walk(walker):
#     for file in files:
#       if not file == 'hash.pickle' and not file == 'name.pickle' and not file == '.DS_Store':
#         print(file)
#         print(glob.glob(file_name))


