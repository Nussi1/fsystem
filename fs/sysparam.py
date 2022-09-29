import sys
import os
import list

dict_func = {
  'list': list.list_file,
  'del': list.delete_file,
  'add': list.add_file,

}

if __name__ == "__main__":

  _, command, file_name = sys.argv
  # command = sys.argv[1]
  # file_name = sys.argv[2:]

  if command in dict_func:
    dict_func.get(command)(file_name)
