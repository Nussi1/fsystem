import settings
import hashlib
import os
import time
import sys
import pickle

#
# def add_file():
#   # file = 'hashed.py'
#   # get_file_path(file)
#   path = get_hash_file(get_file_path())
#   print(path)
#   return path
#
# add_file()
#   # path = get_hash_file(get_file_path(file_name))
#   # print(path)
#   # return path
#
# add = add_file(get_file_path('hashed.py'))
# print(add)

# def get_file_path():
#   path = settings.PATH['path_from']
#   file_name =  "/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/create.py"
#   if not os.path.exists(file_name):
#     with open(path, 'w') as f:
#       f.write('Create a new text file!')
#   else:
#     return file_name
#
# print(get_file_path())

# def get_ref_count(ref_c):
#   return sys.getrefcount(ref_c)
#
# print(get_ref_count("/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/from_fs/na.txt"))

# def create_file():
#   path = settings.PATH['path_from']
#   file_path = "/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/hashed.py"
#   if not os.path.get_file_path(file_path):
#     with open(file_path, 'w') as f:
#       f.write('Create a new text file!')

# print(create_file())



# def check_if_file_exists(file):
#   if os.path.isfile(file):
#     return True
#   else:
#     return False





# def get_hash_file(a):
#   return hashlib.sha256(open(a, "rb").read()).hexdigest()

# print(hash_file())
# get_hash_file(get_file_path('add.py'))
#
#
# def hash_dir():
#   s = '/'.join(list(hash_file()[:4]))
#   path = settings.PATH['path_obj'] + s + '/hash.pickle'
#   return path
#
# # print(hash_dir())
# hash_dir()
#
#
# def hash_name():
#   namehash = hashlib.sha256(get_file_path().encode('UTF-8')).hexdigest()
#   return namehash
#
# # print(hash_name())
# hash_name()
#
#
# def name_dir():
#   s = '/'.join(list(hash_name()[:4]))
#   path = settings.PATH['path_obj'] + s + '/name.pickle'
#   return path
#
# # print(name_dir())
# name_dir()
#
#
# def load_file():
#   with open(hash_dir(), 'rb') as f2:
#     stat = pickle.load(f2)
#   stat[hash_file()] = 'n val'
#
#   with open(hash_dir(), 'wb') as f2:
#     pickle.dump(stat, f2)
#
# load_file()
#
# with open(settings.PATH['path_obj'] + '0/d/2/4/hash.pickle', 'rb') as f2:
#     dicts = pickle.load(f2)
# print(dicts)
#
#
# def load_hashed_name():
#   with open(name_dir(), 'rb') as f2:
#     stat = pickle.load(f2)
#   stat[hash_name()] = 'file name'
#
#   with open(name_dir(), 'wb') as f2:
#     pickle.dump(stat, f2)
#
# load_hashed_name()
#
#
# with open(settings.PATH['path_obj'] + 'c/b/f/a/name.pickle', 'rb') as f2:
#   dicts = pickle.load(f2)
# print(dicts)


# def getfilesize(filename):
#   size =  os.stat(filename).st_size
#   print(size)
#   return size


# def get_time(file_time):
#   return time.ctime(os.path.getctime(file_time))
#
# print(get_time('/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/from_fs/hashed.txt'))
