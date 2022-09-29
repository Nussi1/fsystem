import sys
import list, delete, add

dict_func = {
  'list': list.list_file,
  'del': delete.delete_file,
  'add': add.add_file,
}

_, command, *args = sys.argv

if command not in dict_func:
  print('No such command')
  exit()


dict_func[command](args)
