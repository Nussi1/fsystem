import os
import pathlib
import sys
import settings
import re

# def delete_file(arg):
#   if len(sys.argv) == 2 or len(sys.argv) >= 4:
#     print('Input a file name correctly')
#     exit()
#   path = sys.argv[2:]
#   file = settings.PATH['path_from'] + str(*path)
#
#   if pathlib.Path(file).exists():
#     os.remove(file)
#   else:
#     print('No such file')
#     exit()

# def remove_file_name(file_name):
#   with open('names.txt', 'r') as f:
#       lines = f.readlines()
#   with open('names.txt', 'w') as f:
#     for line in lines:
#       if line.strip("\n") != file_name:
#         f.write(line)
#
# remove_file_name('sa')


# def list_file(args):
#   fn = open('names.txt')
#   for i in fn:
#     if re.search(args, i):
#       print(i, end= '')
#
# list_file('py')