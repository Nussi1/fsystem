import pathlib
import sys
import os
import shutil
import settings
import hashlib
import pickle


def hash_file():
    walker = os.walk(settings.PATH['path_from'])
    for folder, sub_folder, files in walker:
        for file in files:
            filepath = os.path.join(folder, file)
            filehash = hashlib.sha256(open(filepath, "rb").read()).hexdigest()
            s = '/'.join(list(filehash[:4]))
            print(s)
            path = settings.PATH['path_obj'] + s + '/hash.pickle'
            with open(path, 'rb') as f2:
                stat = pickle.load(f2)
            stat[filehash] = 'new value'

            with open(path, 'wb') as f2:
                pickle.dump(stat, f2)


hash_file()
# for _ in range(7):
#     hash_string = next(filehash).strip('\n')
#     s = '/'.join(list(filehash[:4]))
#     print(s)
    # path = '/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/' + s + '/hash.pickle'
    # with open(path, 'rb') as f2:
    #     stat = pickle.load(f2)

#     stat[hash_string] = 1
#     with open(path, 'wb') as f2:
#         pickle.dump(stat, f2)
#
# with open('/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/8/7/6/9/hash.pickle', 'rb') as f2:
#     stat = pickle.load(f2)
# print(stat)