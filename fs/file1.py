import os
import shutil

#--------------упорядочение файлов--------------------

# path = input('Enter Path: ')
# files = os.listdir(path)

# for file in files:
#   filename, extension = os.path.splitext(file)
#   extension = extension[1:]

#   if os.path.exists(path+'/'+extension):
#     shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
#   else:
#     os.makedirs(path+'/'+extension)
#     shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

# os.chdir('')



#-----------------------read or write file------------------

link = input('Enter the name of the file')
with open(link, 'r') as f:
  data = f.read()

with open(link, 'w') as f:
    data = 'some data to be written to the file'
    f.write(data)
