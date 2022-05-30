import os
# import os.path


# print(os.getcwd())
# print(os.listdir())
# print(os.path.exists('os_practice.py'))
# print(os.path.exists('main'))
# print(os.path.isfile('os_practice.py'))
# print(os.path.isdir('main'))
# print(os.path.abspath('a.py'))
# os.chdir('sample')
# print(os.getcwd())
# print()
# for current_dir, dirs, files in os.walk("."):
#     print(current_dir, dirs, files)

name = 'main'
os.chdir(name)
print(os.getcwd())
dir_list = []
for current_dir, dirs, files in os.walk("."):
    for file in files:
        if file[-3:] == '.py':
            current_dir = current_dir.replace('\\', '/')
            current_dir = current_dir.replace('.', 'main')
            print(current_dir)
            dir_list.append(current_dir)
            break
print(dir_list)
