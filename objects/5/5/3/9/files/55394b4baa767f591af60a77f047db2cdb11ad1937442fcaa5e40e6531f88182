import settings
import hashed
import pickle

def load_file():
  with open(hashed.hash_dir(), 'rb') as f2:
    stat = pickle.load(f2)
  stat[hashed.hash_file()] = 'new value'

  with open(hashed.hash_dir(), 'wb') as f2:
    pickle.dump(stat, f2)


load_file()




#
# with open(settings.PATH['path_obj'] + '0/d/2/4/hash.pickle', 'rb') as f2:
#     dicts = pickle.load(f2)
# print(dicts)


# def load_hashed_name():
#   with open(hashed.name_dir(), 'rb') as f2:
#     stat = pickle.load(f2)
#   stat[hashed.hash_name()] = 'new value'
#
#   with open(hashed.name_dir(), 'wb') as f2:
#     pickle.dump(stat, f2)
#
#
# load_hashed_name()

# with open(settings.PATH['path_obj'] + 'c/b/f/a/name.pickle', 'rb') as f2:
#   dicts = pickle.load(f2)
# print(dicts)