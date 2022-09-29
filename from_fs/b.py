import zipfile
import pickle


stat = {}
hash_path = {}

# with open('/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/6/1/7/2/hash.txt', 'w') as f:
#     f.write('hash_string')
#     # f.write("\n")
# exit()

with open("hashed.txt", "r") as f:
    for _ in range(39):
        hash_string = next(f).strip('\n')
        print(hash_string)
        s = '/'.join(list(hash_string[:4]))
        # print(s)
        path = '/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/objects/' + s + '/hash.pickle'
        with open(path, 'rb') as f2:
            stat = pickle.load(f2)
        print(stat)
        stat[hash_string] = 1
        print(stat)
    with open(path, 'wb') as f2:
         pickle.dump(stat, f2)


with open('/Users/nuraim/Desktop/my_projects/zeonithub_july/zeon_fs/objects/8/7/6/9/hash.pickle', 'rb') as f2:
    stat = pickle.load(f2)
print(stat)

        # with open(path, 'a') as fa:
        #     fa.write(hash_string + '\n')
        # # print(path)
# print(stat)
# for key in stat:
#     with open(path, 'w') as f:
#         f.write('hash_string')
