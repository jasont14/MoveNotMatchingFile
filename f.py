import os, shutil

directory = 'directory1'
directory2 = 'directory2'
destination = 'destination'

list1 = os.listdir(directory)
list2 = os.listdir(directory2)

diff = set(list1).difference(list2)

if (diff.__len__()) > 0:
    for f in diff:
        shutil.move(directory + f, destination + f)

print(diff.__len__())
print(diff)