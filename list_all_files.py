import os
from os import listdir
from os.path import isfile, join

files_list = [f for f in os.listdir("/Users") if os.path.isfile(os.path.join("/Users",f))]

print(f"\n{files_list}")