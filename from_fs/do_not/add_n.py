import pathlib
import sys
import os
import shutil
import settings
import hashlib
import pickle



# def hash_file():
#
#   walker = os.walk(settings.PATH['path_from'])
#   for folder, sub_folder, files in walker:
#     for file in files:
#       filepath = os.path.join(folder, file)
#       filehash = hashlib.sha256(open(filepath, "rb").read()).hexdigest()
#       s = '/'.join(list(filehash[:4]))
#       path = settings.PATH['path_obj'] + s + '/hash.pickle'
#       with open(path, 'rb') as f2:
#         stat = pickle.load(f2)
#       stat[filehash] = 'new value'
#
#       with open(path, 'wb') as f2:
#         pickle.dump(stat, f2)
#
#
# hash_file()

# with open(settings.PATH['path_obj'] + '0/d/2/4/hash.pickle', 'rb') as f2:
#     dicts = pickle.load(f2)
# print(dicts)

# def hash_file(filename):
#     filehash = hashlib.sha256(open(filename, "rb").read()).hexdigest()
#     s = '/'.join(list(filehash[:4]))
#     path = settings.PATH['path_obj'] + s + '/hash.pickle'
#     with open(path, 'rb') as f2:
#         stat = pickle.load(f2)
#     stat[filehash] = 'size'
#
#     with open(path, 'wb') as f2:
#         pickle.dump(stat, f2)
#     print(filehash)
#
# hash_file('/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/fs/male.txt')

# def hash_name():
#   walker = os.walk(settings.PATH['path_from'])
#   for folder, sub_folder, files in walker:
#     for name in files:
#       namepath = os.path.join(folder, name)
#       namehash = hashlib.sha256(namepath.encode('UTF-8')).hexdigest()
#       s = '/'.join(list(namehash[:4]))
#       print(s)
#       path = settings.PATH['path_obj'] + s + '/name.pickle'
#       with open(path, 'rb') as f2:
#         stat = pickle.load(f2)
#       stat[namehash] = 'new value'
#
#       with open(path, 'wb') as f2:
#         pickle.dump(stat, f2)
#
#
# hash_name()


def remove_file_name(file):
  with open('/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/names.txt', "r") as f:
    lines = f.readlines()
    lines.remove(file)
    with open("/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/names.txt", "w") as new_f:
      for line in lines:
        new_f.write(line)

remove_file_name('na1.txt')

import pathlib
import sys
import os
import shutil
import settings
import hashlib
import pickle


# stat = {}
# hash_path = {}
#
# with open("hashed.txt", "r") as f:
#   for _ in range(39):
#     hash_string = next(f).strip('\n')
#     s = '/'.join(list(hash_string[:4]))
#     path = '/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/' + s + '/hash.pickle'
#     with open(path, 'rb') as f2:
#       stat = pickle.load(f2)
#
#     stat[hash_string] = 1
#     with open(path, 'wb') as f2:
#       pickle.dump(stat, f2)
#
# with open('/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/8/7/6/9/hash.pickle', 'rb') as f2:
#   stat = pickle.load(f2)
# print(stat)



# def add_file(arg):
#   path_s = sys.argv[2:]
#   original = settings.PATH['path_from'] + str(*path_s)
#   target =settings.PATH['path'] + str(*path_s)
#   walker = os.walk(settings.PATH['root_path'])
#   unique_files = dict()
#
#   for folder, sub_folder, files in walker:
#     for file in files:
#       filepath = os.path.join(folder, file)
#       filehash = hashlib.sha256(open(filepath, "rb").read()).hexdigest()
#       if filehash not in unique_files:
#         shutil.copyfile(original, target)
#         with open(settings.PATH['path_file'], "a") as f:
#           f.write(filehash)
#           f.write("\n")
#       else:
#         print(f"{filepath} such file is already existed")













