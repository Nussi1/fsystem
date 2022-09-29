import os
import settings
import pickle

path = settings.PATH['path_obj']
os.chdir(path)
x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

for i in x:
    os.chdir(path)
    NewFolder = i
    os.makedirs(NewFolder, exist_ok=True)
    path2 = path + '/' + NewFolder
    os.chdir(path2)
    for j in x:
        os.chdir(path2)
        NewFolder_2 = j
        os.makedirs(NewFolder_2, exist_ok=True)
        path3 = path2 + '/' + NewFolder_2
        os.chdir(path3)
        for k in x:
            os.chdir(path3)
            NewFolder_3 = k
            os.makedirs(NewFolder_3, exist_ok=True)
            path4 = path3 + '/' + NewFolder_3
            os.chdir(path4)
            for l in x:
                NewFolder_4 = l
                os.makedirs(NewFolder_4, exist_ok=True)
                path5 = path4 + '/' + NewFolder_4
                file_path = path5 + '/' + 'hash.pickle'
                with open(file_path, 'wb') as file:
                    pickle.dump({}, file)
                name_path = path5 + '/' + 'name.pickle'
                with open(name_path, 'wb') as file:
                    pickle.dump({}, file)
                # for m in l:
                #     os.chdir(path5)
                #     NewFolder_5 = 'files'
                #     os.makedirs(NewFolder_5, exist_ok=True)



